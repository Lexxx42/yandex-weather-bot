# base image
FROM debian:bullseye-slim

# installing of work directory (by default) in image
WORKDIR /app
ARG project_path=.

# installing of requirements
RUN set -eux; \
	apt-get update; \
	apt-get install -y --no-install-recommends \
		python3-pip \
	; \
	rm -rf /var/lib/apt/lists/*

RUN touch .env

# copying of requirements
COPY $project_path/requirements.txt .

# installing requirements from pip
RUN pip3 install -r requirements.txt

# copying project to image
COPY $project_path/*.py ./

# start script after container start
ENTRYPOINT ["python3", "app.py"]
