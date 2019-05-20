FROM python:3.7
ENV PYTHONUNBUFFERED 1
RUN mkdir /exchangerate
WORKDIR /exchangerate
COPY requirements.txt /exchangerate/
RUN pip install -qU pip
RUN pip install -r requirements.txt
COPY . /exchangerate/
