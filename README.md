# Nyay-Sahayak: AI-Powered Legal Analysis Platform

Nyay-Sahayak is an end-to-end AI system for Indian legal document analysis, argument mining, retrieval-augmented generation (RAG), and fact-checking. It enables users to upload Supreme Court judgments, analyze them with advanced language models, visualize knowledge graphs, and verify generated arguments—all through a modern web interface.

---

## Features

- **Document Ingestion:** Upload and parse legal PDFs, extract entities, claims, and premises.
- **Knowledge Graph:** Visualize relationships between cases, entities, claims, and premises.
- **RAG Service:** Generate structured legal arguments using retrieval-augmented LLMs.
- **Fact Checking:** Sentence-level verification of generated arguments against source documents.
- **Modern Frontend:** Intuitive React-based UI with graph visualization and interactive analysis.

---

## Architecture

- **Frontend:** React + Tailwind CSS (`frontend/`)
- **API Gateway:** FastAPI, orchestrates requests (`api-gateway/`)
- **Scraper:** Scrapy-based, downloads Supreme Court judgments (`scraper/`)
- **Ingestion Service:** FastAPI, NLP/argument mining, populates ChromaDB & Neo4j (`ingestion/`)
- **RAG Service:** FastAPI, retrieval-augmented generation with Gemini API (`rag/`)
- **Fact Checker:** FastAPI, sentence-level semantic verification (`fact_checker/`)
- **Databases:** ChromaDB (vector), Neo4j (graph)
- **Orchestration:** Docker Compose

---

## Quickstart

### 1. Prerequisites

- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)
- (Optional) [Python 3.11+](https://www.python.org/) for local development

### 2. Clone the Repository

```sh
git clone https://github.com/yourusername/nyay-sahayak.git
cd nyay-sahayak
```

### 3. Set Up Environment Variables

Create a `.env` file in the root directory:

```
GEMINI_API_KEY=your_google_gemini_api_key
```

### 4. Build and Start All Services

```sh
docker-compose up --build
```

- Frontend: [http://localhost:3000](http://localhost:3000)
- API Gateway: [http://localhost:8000](http://localhost:8000)
- ChromaDB: [http://localhost:8004](http://localhost:8004)
- Neo4j Browser: [http://localhost:7474](http://localhost:7474) (user: `neo4j`, pass: `password`)

---

## Directory Structure

```
api-gateway/      # API Gateway (FastAPI)
fact_checker/     # Fact Checking Service (FastAPI)
frontend/         # React Frontend
ingestion/        # Ingestion & Argument Mining (FastAPI)
rag/              # Retrieval-Augmented Generation (FastAPI)
scraper/          # Scrapy Spider for judgments
shared_data/      # Shared files/data
```

---

## Development

- Each service has its own `requirements.txt` or `package.json`.
- Use Docker for isolated development, or run services locally with Python/Node.js.
- Update `.env` and config files as needed for API keys and DB connections.

---

## Contributing

1. Fork the repo and create your branch (`git checkout -b feature/your-feature`)
2. Commit your changes (`git commit -am 'Add new feature'`)
3. Push to the branch (`git push origin feature/your-feature`)
4. Open a Pull Request

---

## License

MIT License. See [LICENSE](LICENSE) for details.

---

## Acknowledgements

- Indian Supreme Court Open Data
- Google Gemini API
- ChromaDB, Neo4j, FastAPI, React, Tailwind CSS

---

## Contact

For questions or support, open an issue or contact [jayofficial@gmail.com].


