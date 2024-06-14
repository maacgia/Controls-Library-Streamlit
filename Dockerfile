FROM python:3.9-slim

COPY ./app /app
WORKDIR /app
RUN pip install --no-cache-dir -r requirements.txt

# CMD ["streamlit", "run", "app.py"]
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.enableCORS=false"]
