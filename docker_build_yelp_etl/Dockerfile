FROM python:3.8
COPY yelp_etl_pkg .
RUN pip install dist/yelp_etl_pkg-0.1.0-py3-none-any.whl
CMD ["python", "yelp_etl_pkg/cli.py"]
