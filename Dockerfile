FROM python:2.7
ADD . /webapp
WORKDIR /webapp
RUN pip install -r requirements.txt
EXPOSE 8080
CMD python webapp.py
