FROM python:alpine3.17

WORKDIR /app

# COPY ./requirements.txt /app/requirements.txt
COPY requirements.txt ./
COPY main.py ./
# 
# RUN pip install --upgrade pip


RUN pip install --no-cache-dir --upgrade -r requirements.txt

 
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

