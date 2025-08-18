FROM python:3.11-slim
WORKDIR /main

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN python -c "from transformers import pipeline; pipeline('zero-shot-classification', model='typeform/distilbert-base-uncased-mnli')"

COPY . .
EXPOSE 8000
RUN useradd --create-home app && chown -R app:app /main
USER app

CMD ["python","manage.py","runserver","0.0.0.0:8000"]