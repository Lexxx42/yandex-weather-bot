# base image
FROM ubuntu

# installing of work directory (by default) in image and var for project dir
WORKDIR /app
ARG project_path=./weatherbot

# installing of requirements
RUN apt-get update ;\
    apt-get install -y --no-install-recommends python3-pip;\
    apt-get clean && rm -rf /var/lib/apt/lists/* ;\
    touch .env

# copying of requirements
COPY $project_path/requirements.txt .

# installing requirements from pip
RUN pip3 install -r requirements.txt

# copying project to image
COPY $project_path/*.py ./

# start script after container start
ENTRYPOINT ["python3", "app.py"]
