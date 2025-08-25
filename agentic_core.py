
import os
from openai import OpenAI
client = OpenAI()

def get_initial_claims(paper_text):
    """Generates initial claims from each persona based on the paper's text
    """

    # defining the personas as a dictionary for easy iteration
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

    # A chunk of the paper's text to fit within the context window
    text_chunk = paper_text[:8000]

    claims = {}

    # Iterate through each personas and get their initial analysis
    for persona, prompt_text in personas.items():
        print(f"\n--- Generating claims for {persona} ---")

        try:
            # OpenAI uses a message-based chat completion API
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": prompt_text},
                    {"role": "user", "content": f"Based on the following paper text, provide a detailed analysis:\n\n{text_chunk}"}    
                ]
            )
            # Access the generated content from the response object
            claims[persona] = response.choices[0].message.content
        except Exception as e:
            claims[persona] = f"Error generating content for {persona}: {e}"
            print(claims[persona])

    return claims

if __name__ == "__main__":
    print("This script is ready to be integrated with the PDF ingestion module.")

