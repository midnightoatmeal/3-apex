from flask import Flask, render_template, request

# Import functions from your backend scripts
from pdf_ingestion import ingest_pdf_from_arxiv
from agentic_core import run_full_debate

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        arxiv_id = request.form["arxiv_id"]
        
        try:
            # Step 1: Ingest the PDF and get the text chunks
            text_chunks = ingest_pdf_from_arxiv(arxiv_id)

            # Step 2: Run the debate using the text chunks
    
            debate_data = run_full_debate(text_chunks)
            
            # Step 3: Render the results page with the structured debate data
            return render_template("results.html", debate=debate_data)
        
        except Exception as e:
            # A simple error handler to show the user if something goes wrong
            return f"An error occurred: {e}"
    
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
