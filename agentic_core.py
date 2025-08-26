import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize the client only once in the file
client = OpenAI()

def run_full_debate(paper_text):
    """
    Orchestrates the entire agentic debate process.

    This function is the main entry point for the web application,
    calling the other functions in the correct sequence.

    Args:
        paper_text (str): The full text of the paper.

    Returns:
        dict: A structured dictionary containing the full debate transcript
              and the final TL;DR summary, ready for the web template.
    """
    initial_claims = get_initial_claims(paper_text)
    debate_history = run_debate(initial_claims, paper_text)
    tldr_summary = generate_tldr(debate_history)
    
    formatted_rounds = {}
    for round_data in debate_history:
        round_num = str(round_data.pop("round"))
        formatted_rounds[round_num] = round_data
    
    final_output = {
        "tldr": tldr_summary,
        "rounds": formatted_rounds
    }

    return final_output

def get_initial_claims(paper_text):
    """
    Generates initial claims from each persona based on the paper's text.
    """
    personas = {
       "Optimist": ("You are the Optimist. You see the potential and positive "
                    "implications of new scinetific findings. Identify the most "
                    "promising claims and explain their significance. Be sure to "
                    "cite specific sentences or sections from the paper."),
       "Skeptic": ("You are the Skeptic. You are a critical peer reviewer who "
                   "questions everything. Identify potential weaknesses, limitations, "
                   "or unsubstantiated claims in the paper. Explain your reasoning "
                   "and cite specific sentences or sections."),
        "Ethicist": ("You are the Ethicist. You are an expert in AI ethics. Identify "
                     "any potential ethical implications, both positive and negative, "
                     "including data usage, bias, or societal impact. Explain your "
                     "concerns and cite specific sentences or sections.")
    }

    text_chunk = paper_text[:8000]
    claims = {}

    for persona, prompt_text in personas.items():
        try:
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": prompt_text},
                    {"role": "user", "content": f"Based on the following paper text, provide a detailed analysis:\n\n{text_chunk}"}    
                ]
            )
            claims[persona] = response.choices[0].message.content
        except Exception as e:
            claims[persona] = f"Error generating content for {persona}: {e}"

    return claims

def run_debate(initial_claims, paper_text, max_rounds=3):
    """
    Simulates a multi-round debate between the personas.
    """
    debate_history = []
    debate_history.append({"round": 0, "Optimist": initial_claims["Optimist"], "Skeptic": initial_claims["Skeptic"], "Ethicist": initial_claims["Ethicist"]})
    text_chunk = paper_text[:8000]

    for i in range(1, max_rounds + 1):
        previous_optimist_claim = debate_history[-1].get("Optimist", "")
        previous_skeptic_claim = debate_history[-1].get("Skeptic", "")
        previous_ethicist_claim = debate_history[-1].get("Ethicist", "")
        current_round = {}

        skeptic_prompt = (
            f"You are the Skeptic. The Optimist has made the following claim: '{previous_optimist_claim}'. "
            f"Provide a counter-argument or a point of nuance, citing the paper to suggest your position. "
            f"Here is the paper text for reference:\n\n{text_chunk}"
        )
        skeptic_response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": skeptic_prompt}]
        ).choices[0].message.content
        current_round["Skeptic"] = skeptic_response

        optimist_prompt = (
            f"You are the Optimist. The Skeptic has just made the following counter-claim: '{current_round['Skeptic']}'. "
            f"Provide a rebuttal or a different perspective that supports the paper's findings. "
            f"Here is the paper text for reference:\n\n{text_chunk}"
        )
        optimist_response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": optimist_prompt}]
        ).choices[0].message.content
        current_round["Optimist"] = optimist_response

        ethicist_prompt = (
            f"You are the Ethicist. The Optimist and Skeptic are debating. The Optimist's last point was: '{current_round['Optimist']}'. "
            f"The Skeptic's last pint was: '{current_round['Skeptic']}'. "
            f"What are the ethical implications of their debate? Add a new ethical claim or concern, citing the paper. "
            f"Here is the paper text for reference:\n\n{text_chunk}"
        )
        ethicist_response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": ethicist_prompt}]
        ).choices[0].message.content
        current_round["Ethicist"] = ethicist_response
        current_round["round"] = i
        debate_history.append(current_round)

    return debate_history

def generate_tldr(debate_history):
    """
    Generates a concise TL:DR summary of the entire debate.
    """
    formatted_debate = ""
    for round_data in debate_history:
        formatted_debate += f"\nRound {round_data['round']}:\n"
        for persona, claim in round_data.items():
            if persona != "round":
                formatted_debate += f" {persona.upper()}: {claim}\n"
    
    tldr_prompt = (
        f"Based on the following debate transcript, provide a concise, neutral "
        f"TL;DR summary of the key points and outcomes. Do not add any new information. "
        f"Focus on the core arguments from the Optimist, Skeptic, and Ethicist.\n\n"
        f"Debate Transcript:\n{formatted_debate}"
    )

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": tldr_prompt}]
        )
        return response.choices[0].message.content
    
    except Exception as e:
        return f"Error generating TL;DR: {e}"
