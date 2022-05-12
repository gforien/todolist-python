FROM python:3.9-alpine3.15 as base

WORKDIR /app
COPY requirements.txt .
RUN pip3 install -r requirements.txt
COPY . .

ENV FLASK_APP=app
ENV FLASK_ENV=development

EXPOSE 5000
CMD ["flask", "run", "-h", "0.0.0.0"]
