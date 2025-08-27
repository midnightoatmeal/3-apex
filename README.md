arXiv agent: A Multi-Perspective Research Analyzer

This project is an agentic AI system that provides a structured, multi-perspective analysis of academic papers. By taking an arXiv ID as input, the agent ingests a paper, and then three distinct AI personas—the Optimist, Skeptic, and Ethicist—debate its claims. The final output is a cited, claim-by-claim debate summary and a concise TL;DR.

⸻

Features:
	•	PDF Ingestion: Automatically downloads and parses papers from arXiv using only the paper’s ID.
	•	Persona-Driven Analysis: Utilizes three specialized AI agents to analyze a paper from optimistic, skeptical, and ethical viewpoints.
	•	Structured Debate: Simulates a multi-round debate where agents respond to each other’s claims and counter-claims.
	•	Cited Arguments: All claims are grounded in the original paper’s text to minimize hallucination.
	•	Concise Summarization: Generates a final TL;DR that distills the entire debate into a clear, neutral summary.

⸻

Getting Started

Follow these steps to get a local copy of the project up and running.

Prerequisites:
	•	Python 3.10 or higher
	•	An OpenAI API Key

Installation:

Clone the repository:

git clone https://github.com/midnightoatmeal/3-apex.git
cd 3-apex

Create a virtual environment:

python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

Install the required dependencies:

pip install -r requirements.txt

Note: You will need to create a requirements.txt file with the following contents:

requests
pdfplumber
openai
python-dotenv


⸻

Configuration:

Create a .env file in the root directory of your project.

Add your OpenAI API Key to .env in the following format:

OPENAI_API_KEY="sk-your-key-here"

The .env file is already included in .gitignore to keep your API key safe.

⸻

Usage:

To run the agent and analyze a paper, execute the main script from your terminal:

python3 main.py <arxiv_id>

Example:
To analyze the seminal “Attention Is All You Need” paper, use the ID 1706.03762.

python3 main.py 1706.03762

The script will download the paper and print a structured, claim-by-claim analysis and debate to your terminal.

⸻

Project Structure

3-apex/
├── .env
├── .gitignore
├── main.py
├── pdf_ingestion.py
├── agentic_core.py 
└── requirements.txt


⸻

Contributing

Contributions are welcome!
If you have ideas for new personas, better prompts, or improved debate logic, please open an issue or submit a pull request.

⸻

License

This project is licensed under the MIT License.
See the LICENSE file for details.