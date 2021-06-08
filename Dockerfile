FROM python:3.8
ADD server.py .
RUN pip install pymongo parsedatetime requests
CMD [ "python3", "./server.py" ]