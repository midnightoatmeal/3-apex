## arXiv agent: A Multi-Perspective Research Analyzer

This project is an agentic AI system that provides a structured, multi-perspective analysis of academic papers. By taking an arXiv ID as input, the agent ingests a paper, and then three distinct AI personas—the Optimist, Skeptic, and Ethicist—debate its claims. The final output is a cited, claim-by-claim debate summary and a concise TL;DR.


## Features

- **PDF Ingestion**: Automatically downloads and parses papers from arXiv using only the paper’s ID.  
- **Persona-Driven Analysis**: Utilizes three specialized AI agents to analyze a paper from optimistic, skeptical, and ethical viewpoints.  
- **Structured Debate**: Simulates a multi-round debate where agents respond to each other’s claims and counter-claims.  
- **Cited Arguments**: All claims are grounded in the original paper’s text to minimize hallucination.  
- **Concise Summarization**: Generates a final TL;DR that distills the entire debate into a clear, neutral summary.  



## Getting Started

Prerequisites:
	•	Python 3.10 or higher
	•	An OpenAI API Key

## Installation

Clone the repository:
```
git clone https://github.com/midnightoatmeal/arxiv-agent.git
cd arxiv-agent
```

Create a virtual environment:

```
python3 -m venv venv
source venv/bin/activate
```
```  
venv\Scripts\activate #windows
```

Install the required dependencies:
```
pip install -r requirements.txt
```


## Configuration

In the root directory, you will find a template file named `.env.example`.

Make a copy of this file and rename it to `.env`. You can do this with the following command in your terminal:
```
cp .env.example .env
```

Add your OpenAI API Key to `.env` in the following format:

OPENAI_API_KEY="sk-your-key-here"

The `.env` file is already included in `.gitignore` to keep your API key safe.



## Usage

To run the agent and analyze a paper, execute the main script from your terminal:
```
python3 main.py <arxiv_id>
```

Example:
To analyze the seminal “Attention Is All You Need” paper, use the ID 1706.03762.
```
python3 main.py 1706.03762
```
The script will download the paper and print a structured, claim-by-claim analysis and debate to your terminal.


## Project Structure
```
arxiv-agent/
├── .env.example          # Template for environment variables
├── main.py               # Main script to run the project
├── pdf_ingestion.py      # Handles PDF downloading and parsing
├── agentic_core.py       # Contains the LLM agent logic and debate engine
├── requirements.txt      # Project dependencies
└── .gitignore            # Specifies files to ignore
```


## Contributing

Contributions are welcome!
If you have ideas for new personas, better prompts, or improved debate logic, please open an issue or submit a pull request.


## License

This project is licensed under the Apache-2.0 License.
See the LICENSE file for details.