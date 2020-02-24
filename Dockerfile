FROM python:3.6
EXPOSE 5432
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD python main.py