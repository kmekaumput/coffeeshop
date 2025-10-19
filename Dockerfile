FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

EXPOSE 80

ENV FLASK_APP=app.py
ENV FLASK_ENV=production

CMD ["python", "app.py"]