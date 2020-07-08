FROM python:3.7
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install -r --quiet requirements.txt
COPY . .
EXPOSE 7000
CMD uvicorn /app/webcalc.main:app --reload
