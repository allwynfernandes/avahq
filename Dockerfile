FROM python:3.8
RUN mkdir -p /usr/scr/app
WORKDIR /usr/scr/app
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .
CMD ["python3", "server.py"]




# FROM python:3.8
# ADD server.py .
# RUN pip install pymongo parsedatetime requests
# CMD [ "python3", "./server.py" ]