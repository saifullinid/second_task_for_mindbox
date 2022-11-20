FROM python:3.10.8-slim-buster
WORKDIR /app

COPY requirements.txt ./tmp/
RUN pip install --no-cache-dir --upgrade -r ./tmp/requirements.txt

COPY . .

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]