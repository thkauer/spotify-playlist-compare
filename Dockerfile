FROM python:3.12

ARG USERNAME=vscode

RUN apt-get update && pip install --upgrade pip

# create container user
RUN groupadd -r $USERNAME && useradd -r -m -g $USERNAME $USERNAME
WORKDIR /home/$USERNAME
USER $USERNAME

# install requirements
COPY ./requirements.txt /docker/requirements.txt
RUN pip install -r /docker/requirements.txt

# Copy application code
COPY . .
