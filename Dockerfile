FROM python:3.9
WORKDIR /apiping
COPY ./requirements.txt /apiping/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /apiping/requirements.txt
COPY ./main.py /apiping/
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--limit-concurrency", "10"]
