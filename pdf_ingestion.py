import requests
import pdfplumber

def get_arxiv_id(url_or_id):
    """Extracts the arxiv ID from a full URL or returns the ID if there's
    already an ID.
    Example: 'https://arxiv.org/abs/2301.00001' -> '2301.00001
    """

    if '/' in url_or_id:
        return url_or_id.split('/')[-1]
    return url_or_id

def ingest_pdf_from_arxiv(arxiv_id):
    """Downloads a PDF from arxiv and extracts its text.
    Args:
        arxiv_id (str): The ID of the arxiv paper (eg., '2301.00001).
        
    Returns:
        str: The extracted text from the PDF, or None if an error occurs.
        """
    
    # Construct the URL for the PDF
    base_url = "https://arxiv.org/pdf/"
    pdf_url = f"{base_url}{arxiv_id}.pdf"

    print(f"Donwloading PDF from: {pdf_url}")
    