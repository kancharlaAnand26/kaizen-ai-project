# KAIZEN-AI: Interactive Digital Twin Assistant 🤖🔩

An intelligent, conversational assistant for complex manufacturing and assembly procedures. This project replaces static PDF manuals with an interactive chat interface powered by a 3D digital twin, enabling technicians to get precise, context-aware answers instantly.

![KAIZEN-AI Screenshot](https://i.imgur.com/your-screenshot-url.png)
*(Suggestion: Run the project, take a screenshot, upload it to a site like Imgur, and paste the link here.)*

---

## 📖 About The Project

In modern manufacturing, technicians often rely on dense, hard-to-navigate PDF manuals. Finding a specific torque value or troubleshooting step can be time-consuming and error-prone.

**KAIZEN-AI** solves this problem by creating a "second brain" for the factory floor. It leverages a Retrieval-Augmented Generation (RAG) pipeline to ingest technical documents and provide answers grounded in that specific knowledge base. The integrated 3D viewer provides immediate visual context, bridging the gap between digital instructions and the physical world.

This project was built to showcase a full-stack approach to solving real-world industrial challenges with modern AI and web technologies, directly aligning with the goals of Digital Transformation (DX) in manufacturing.

### Built With

This project brings together a powerful stack of modern technologies:

* **Backend:** Python, FastAPI
* **AI/ML:** LangChain, OpenAI API, ChromaDB (Vector Store)
* **Frontend:** React.js, JavaScript
* **3D Rendering:** React Three Fiber, Drei
* **Deployment:** Git

---

## 🚀 Getting Started

Follow these instructions to get a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

You will need the following software installed on your computer:
* [Node.js](https://nodejs.org/en/download/) (v18+)
* [Python](https://www.python.org/downloads/) (v3.9+)
* An **OpenAI API Key**

### Installation

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/YOUR_USERNAME/kaizen-ai-assistant.git](https://github.com/YOUR_USERNAME/kaizen-ai-assistant.git)
    cd kaizen-ai-assistant
    ```

2.  **Setup the Backend:**
    ```bash
    cd backend
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    pip install -r requirements.txt
    ```
    * Create a `.env` file in the `backend` folder and add your OpenAI API key: `OPENAI_API_KEY="sk-..."`

3.  **Setup the Frontend:**
    ```bash
    cd ../frontend
    npm install
    ```

---

## ⚙️ Usage

1.  **Add Your Knowledge Base:**
    * Place your technical documents (.pdf, .txt) inside the `backend/documents/` folder.

2.  **Ingest the Data:**
    * In your backend terminal, run the ingestion script once. This builds the vector database.
    ```bash
    # Make sure you are in the 'backend' directory with the venv activated
    python ingest.py
    ```

3.  **Run the Servers:**
    * **Backend Server:** In your backend terminal, start the FastAPI server.
        ```bash
        uvicorn app.main:app --reload
        ```
    * **Frontend Server:** In a second terminal, start the React development server.
        ```bash
        # Make sure you are in the 'frontend' directory
        npm start
        ```
    * Open your browser and navigate to `http://localhost:3000`.

---

## 📄 License

Distributed under the MIT License. See `LICENSE` for more information.

---

## Acknowledgements

* This project was developed as a portfolio piece to demonstrate skills in full-stack development and applied AI.
* Built with guidance from modern AI development best practices.
