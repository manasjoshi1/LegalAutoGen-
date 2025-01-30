Overview

LegAutoGen is an AutoGen-based AI system designed to analyze legal cases under Indian law. It automates case assessment by simulating a conversation between a victim, a junior lawyer, and a senior lawyer to provide structured legal advice.

Features

🏛 Multi-Agent System: Implements three distinct agents to handle case analysis.

⚖ Legal Expertise: Focuses on Indian law to provide relevant legal recommendations.

🤖 Automated Case Workflow: The system processes legal cases without human intervention.

🔄 Feedback & Iteration: The senior lawyer refines the junior lawyer’s analysis before presenting it to the victim.

Tech Stack

Python

AutoGen (for multi-agent communication)

OpenAI GPT-4o-mini (for legal analysis)

Virtual Environment (for dependency management)

Installation

1️⃣ Set Up Virtual Environment

python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

2️⃣ Install Dependencies

pip install autogen openai

3️⃣ Configure API Key

Modify utils.py to return your OpenAI API key:

import os

def get_openai_api_key():
    return os.getenv("OPENAI_API_KEY")  # Set API key in environment variables

Usage

Running the Project

python main.py

Case Processing Workflow

Victim shares details of their legal case.

Junior lawyer analyzes the case and proposes a legal solution.

Senior lawyer reviews the analysis and refines the response.

Victim receives final legal advice from the senior lawyer.

Example Case Handled

Case Type: Assault & RobberyJurisdiction: Indian LawWorkflow:

Victim provides incident details, witness statements, and evidence.

Junior lawyer assesses legal charges under IPC (Indian Penal Code).

Senior lawyer reviews and suggests legal remedies (e.g., FIR filing, compensation claims).

Victim receives a legal action plan with next steps.

Future Improvements

✅ Add Indian Penal Code (IPC) references automatically.✅ Integrate court case precedents.✅ Expand to other jurisdictions (e.g., US, UK laws).

Author: Manas
License: MIT

