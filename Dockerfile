FROM python:3.11-slim

WORKDIR /app

COPY wetter.py .

run pip install streamlit requests

EXPOSE 8501

CMD ["streamlit", "run", "wetter.py", "--server.address=0.0.0.0"]