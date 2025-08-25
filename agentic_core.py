
import os
from openai import OpenAI

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
                   "questions everything. Identify potential weaknesses, limitation, "
                   "or unsubstantiated claims in the paper. Explain your reasoning "
                   "and cite specific sentences or sections."),

        "Ethicist": ("You are the Ethicist. You are an expert in AI ethics. Identify "
                     "any potential ethical implications, both positive and negative, "
                     "including data usage, bias, or societal impact. Explain your "
                     "concerns and cite specific sentences or sections.")
    }
    