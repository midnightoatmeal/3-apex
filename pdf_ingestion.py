import requests
import pdfplumber
import io

def get_arxiv_id(url_or_id):
    """
    Extracts the arXiv ID from a full URL or returns the ID if it's already an ID.
    Example: 'https://arxiv.org/abs/2301.00001' -> '2301.00001
    """
    if '/' in url_or_id:
        return url_or_id.split('/')[-1]
    return url_or_id

def ingest_pdf_from_arxiv(arxiv_id):
    """
    Downloads a PDF from arXiv and extracts its text.

    Args:
        arxiv_id (str): The ID of the arXiv paper (e.g., '2301.00001').
        
    Returns:
        str: The extracted text from the PDF, or None if an error occurs.
    """
    # Construct the URL for the PDF
    base_url = "https://arxiv.org/pdf/"
    pdf_url = f"{base_url}{arxiv_id}.pdf"

    print(f"Downloading PDF from: {pdf_url}")

    try:
        # Download the PDF content
        response = requests.get(pdf_url)
        response.raise_for_status()  # This will raise an HTTPError if the response was an error

        # Use BytesIO to create a file-like object from the downloaded bytes
        pdf_bytes = io.BytesIO(response.content)

        # Use pdfplumber to open and process the PDF from the in-memory stream
        with pdfplumber.open(pdf_bytes) as pdf:
            full_text = ""
            for page in pdf.pages:
                text_on_page = page.extract_text()
                if text_on_page:
                    full_text += text_on_page + "\n"
        
        print("PDF successfully ingested and text extracted.")
        return full_text
    
    except requests.exceptions.RequestException as e:
        print(f"Error downloading the PDF: {e}")
        return None
    except Exception as e:
        print(f"An error occurred during the PDF processing: {e}")
        return None

if __name__ == "__main__":
    example_id = "1706.03762"  # The ID for the "Attention Is All You Need" paper
    paper_text = ingest_pdf_from_arxiv(example_id)

    if paper_text:
        # Print the first 1000 characters to verify the text extraction
        print("\n--- Extracted Text Preview ---")
        print(paper_text[:1000])
        print("\n--- End of Preview ---")