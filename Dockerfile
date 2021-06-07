FROM python:3.8
ADD server.py .
RUN pip install pymongo parsedatetime 
CMD [ "python", "./server.py" ]