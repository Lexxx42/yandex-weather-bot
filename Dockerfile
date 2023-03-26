# base image
FROM ubuntu

# installing of work directory (by default) in image
WORKDIR /app
ARG project_path=.

# installing of requirements
RUN apt-get update && apt-get install -y python3 python3-pip

RUN touch .env

# copying of requirements
COPY $project_path/requirements.txt .

# installing requirements from pip
RUN pip3 install -r requirements.txt

# copying project to image
COPY $project_path/*.py ./

# start script after container start
ENTRYPOINT ["python3", "app.py"]
