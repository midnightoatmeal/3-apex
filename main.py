import sys
import os
from openai import OpenAI
from dotenv import load_dotenv # <-- New import

from pdf_ingestion import ingest_pdf_from_arxiv
from agentic_core import get_initial_claims

# Load environment variables from the .env file
load_dotenv()
client = OpenAI()

def main(arxiv_id):
    """
    Main function to orchestrate the paper analysis process.
    """
    # Step 1: Ingest the PDF and get the full text
    paper_text = ingest_pdf_from_arxiv(arxiv_id)
    if not paper_text:
        print("Could not ingest the PDF. Exiting.")
        sys.exit(1)

    # Step 2: Pass the text to the personas and get their initial claims
    initial_claims = get_initial_claims(paper_text)

    # Step 3: Print the results in a structured format
    print("\n" + "="*50)
    print(f"Initial Analysis of ArXiv Paper: {arxiv_id}")
    print("="*50 + "\n")

    for persona, claim in initial_claims.items():
        print(f"### {persona.upper()}")
        print(claim)
        print("\n" + "-"*50 + "\n")

if __name__ == "__main__":
    # The script now takes the arXiv ID from the command line
    if len(sys.argv) < 2:
        print("Please provide an arXiv ID as a command-line argument.")
        print("Example: python main.py 1706.03762")
        sys.exit(1)

    arxiv_id_to_analyze = sys.argv[1]
    main(arxiv_id_to_analyze)