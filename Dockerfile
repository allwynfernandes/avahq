FROM python:3.8
ADD server.py .
RUN pip install pymongo parsedatetime requests logging datetime os
CMD [ "python3", "./server.py" ]