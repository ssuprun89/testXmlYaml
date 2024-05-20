FROM python:3.10-slim

RUN pip install --upgrade pip

# set workdir
WORKDIR app/

# updating PATH
ENV PATH="${PATH}:/root/.local/bin"
ENV PYTHONPATH="/app/"

# copy source and requirement files
COPY . .

# install requirements
RUN pip install -r requirements.txt

# run uvicorn
ENTRYPOINT ["python", "./main.py"]
