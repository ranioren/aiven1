FROM python
WORKDIR /aiven
COPY . /aiven/
RUN pip install sqlalchemy
RUN pip install psycopg2
RUN pip install pandas
CMD ["python3","csv_extract.py" ]