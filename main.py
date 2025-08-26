import sys
import os

from pdf_ingestion import ingest_pdf_from_arxiv
from agentic_core import get_initial_claims, run_debate, generate_tldr


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

    # Step 4. Run the multi-round debate
    print("\n" + "="*50)
    print(f"Starting the Debate")
    print("="*50 + "\n")

    debate_history = run_debate(initial_claims, paper_text)

    # Step 5. Print the final debate history
    for round_data in debate_history:
        print("\n" + "#"*10 + f" ROUND {round_data['round']} " + "#"*10)
        for persona. claim in round_data.items():
            if persona != "round":
                print(f"\n### {persona.upper()}")
                print(claim)
    
    # Step 6. Generate and print the TL;DR summary
    print("\n" + "="*50)
    print("TL;DR - DEBATE SUMMARY")
    print("="*50 + "\n")

    tldr_summary = generate_tldr(debate_history)
    print(tldr_summary)

if __name__ == "__main__":
    # The script now takes the arXiv ID from the command line
    if len(sys.argv) < 2:
        print("Please provide an arXiv ID as a command-line argument.")
        print("Example: python main.py 1706.03762")
        sys.exit(1)

    arxiv_id_to_analyze = sys.argv[1]
    main(arxiv_id_to_analyze)
