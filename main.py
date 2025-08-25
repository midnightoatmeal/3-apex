
import sys
import os
from pdf_ingestion import ingest_pdf_from_arxiv
from agentic_core import get_initial_claims

def main(arxiv_id):
    """
    Main function to orchestrate the paper analysis process.
    """
    # 1. Ingest the PDF and get the full text
    paper_text = ingest_pdf_from_arxiv(arxiv_id)
    if not paper_text:
        print("Could not ingest the PDF. Exiting.")
        sys.exit(1)

    # 2. Pass the text to the personas and get their initial claims
    get_initial_claims = get_initial_claims(paper_text)

    # 3. Print the results in a structured format
    print("\n" + "="*50)
    print(f"Initial Analysis of Arxiv paper: {arxiv_id}")
    print("="*50 + "\n")

    for persona, claim in get_initial_claims.items():
        print(f"### {persona.upper()}")
        print(claim)
        print("\n" + "-"*50 + "\n")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please provide an arxiv ID as a command-line argument.")
        print("Example: python main.py 1706.03762")
        sys.exit(1)

    arxiv_id_to_analyze = sys.argv[1]
    main(arxiv_id_to_analyze)
    