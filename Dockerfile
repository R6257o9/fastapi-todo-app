FROM python:alpine3.17

WORKDIR /app

# COPY ./requirements.txt /app/requirements.txt
COPY requirements.txt ./
COPY ./ ./
# 
RUN pip3 install --upgrade pip
RUN pip3 install --no-cache-dir --upgrade -r requirements.txt

ENV MONGO_URI mongodb://localhost:27017/
 
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]

