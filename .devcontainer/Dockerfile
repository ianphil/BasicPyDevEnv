FROM ubuntu:16.04

ENV DEBIAN_FRONTEND=noninteractive
ARG USERNAME=vscode
ARG USER_UID=1000
ARG USER_GID=$USER_UID

EXPOSE 10000
EXPOSE 10001

RUN apt-get update \
  && apt-get install software-properties-common curl -y \
  && add-apt-repository ppa:deadsnakes/ppa \
  && apt-get update \
  && apt-get install python3.6 -y \
  && curl -sL https://aka.ms/InstallAzureCLIDeb | bash \
  && curl -sL https://deb.nodesource.com/setup_12.x | bash \
  && apt-get install -y nodejs \
  && curl https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > microsoft.gpg \
  && mv microsoft.gpg /etc/apt/trusted.gpg.d/microsoft.gpg \
  && sh -c 'echo "deb [arch=amd64] https://packages.microsoft.com/repos/microsoft-ubuntu-xenial-prod xenial main" > /etc/apt/sources.list.d/dotnetdev.list' \
  && apt-get update \
  && apt-get install vim azure-functions-core-tools -y \
  && ln -s -f /usr/bin/python3.6 /usr/bin/python \
  && curl -sL https://bootstrap.pypa.io/get-pip.py -o get-pip.py \
  && python get-pip.py \
  && pip install --upgrade pip \
  && apt-get install python3-venv python3.6-venv -y \
  && apt-get -y install --no-install-recommends apt-utils dialog 2>&1 \
  && apt-get -y install git procps lsb-release \
  && groupadd --gid $USER_GID $USERNAME \
  && useradd -s /bin/bash --uid $USER_UID --gid $USER_GID -m $USERNAME \
  && apt-get install -y sudo \
  && echo $USERNAME ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/$USERNAME \
  && chmod 0440 /etc/sudoers.d/$USERNAME \
  && apt-get autoremove -y \
  && apt-get clean -y \
  && rm -rf /var/lib/apt/lists/*

RUN mkdir -p /workspaces/azurite && chmod 777 /workspaces/azurite
RUN npm install -g azurite
ENV DEBIAN_FRONTEND=
