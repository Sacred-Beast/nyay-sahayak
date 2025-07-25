FROM python:3.11-slim

WORKDIR /scraper

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY scraper/ ./scraper
COPY run_scraper.py .

CMD ["python", "run_scraper.py"]
