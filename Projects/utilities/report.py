FROM codercom/code-server:latest
USER root

# Set up project directory
RUN mkdir -p /home/coder/project && \
    chown -R coder:coder /home/coder/project

# Install dependencies
RUN apt-get update && \
    apt-get install -y software-properties-common libgbm-dev curl git sudo && \
    rm -rf /var/lib/apt/lists/*

# Installing Extensions
COPY ../common/config.yaml /home/coder/.config/code-server/

# Adding Config files
COPY ../common/.gitignore /home/coder/.gitignore
RUN git config --global core.excludesFile '~/.gitignore'

# Enabling Port
EXPOSE 3000 8081 8080
ENV PORT 3000

# Set bash as default shell
RUN rm /bin/sh && ln -s /bin/bash /bin/sh

# Install Miniconda
RUN curl -o miniconda.sh https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh && \
    bash miniconda.sh -b -p /opt/conda && \
    rm miniconda.sh && \
    echo "export PATH=/opt/conda/bin:${PATH}" >> /etc/bash.bashrc && \
    rm /bin/sh && ln -s /bin/bash /bin/sh

# Install python packages and dependencies
RUN apt-get update \
    && apt-get --no-install-recommends install -y python3 python3.8-dev python3-pandas python3-numpy python3-pip \
    gfortran musl-dev g++ libffi-dev libxml2 libxml2-dev libxslt-dev python3-dev build-essential \
    python3-sklearn python3-sklearn-lib time \
    && apt-get clean

# Install cython using pip3
RUN conda update -n base -c defaults conda
RUN pip3 install cython
RUN pip3 install django
RUN pip3 install pytest

# Install Node.js version 14
ENV NODE_VERSION_14 14.17.1

# Download and install Node.js
RUN curl -o- https://nodejs.org/dist/v$NODE_VERSION_14/node-v$NODE_VERSION_14-linux-x64.tar.xz | tar -Jx \
    && mv node-v$NODE_VERSION_14-linux-x64 /usr/local/nvm \
    && ln -s /usr/local/nvm/bin/node /usr/local/bin/node \
    && ln -s /usr/local/nvm/bin/npm /usr/local/bin/npm

# Download and install Mysql
RUN apt-get update && \
    apt-get --no-install-recommends -yq install default-mysql-client && \
    apt-get clean

# Download and install chromium
RUN apt-get install chromium -y && \
    apt-get clean
ENV CHROME_BIN=/usr/bin/chromium
RUN echo "export CHROME_BIN=/usr/bin/chromium" >> /home/coder/.bashrc

# Password and permissions
RUN echo "coder:examly@123" | chpasswd
RUN usermod -aG sudo coder
RUN sudo rm /etc/sudoers.d/nopasswd

# User configuration
USER coder

# Install the extension using vsix
COPY ../common/extensions/VscodeDjangoMysql/almahdi.code-django-0.5.2.vsix /tmp/almahdi.code-django-0.5.2.vsix
COPY ../common/extensions/VscodeDjangoMysql/bigonesystems.django-1.0.2.vsix /tmp/bigonesystems.django-1.0.2.vsix
COPY ../common/extensions/VscodeDjangoMysql/Emeric-Defay.django-factory-0.0.9.vsix /tmp/Emeric-Defay.django-factory-0.0.9.vsix
COPY ../common/extensions/VscodeDjangoMysql/shamanu4.django-intellisense-0.0.2.vsix /tmp/shamanu4.django-intellisense-0.0.2.vsix
COPY ../common/extension/VscodeMysqlPythonSelenium/ms-python.python-2023.20.0.vsix /tmp/ms-python.python-2023.20.0.vsix

# Install extensions using code-server command
RUN code-server --install-extension cweijan.vscode-myssql-client2 && \
    code-server --install-extension rangav.vscode-thunder-client && \
    code-server --install-extension /tmp/ms-python.python-2023.20.0.vsix && \
    code-server --install-extension almahdi.code-django && \
    code-server --install-extension Angular.ng-template && \
    code-server --install-extension dsznajder.es7-react-js-snippets && \
    code-server --install-extension johnpapa.Angular2 && \
    code-server --install-extension /tmp/almahdi.code-django-0.5.2.vsix && \
    code-server --install-extension /tmp/bigonesystems.django-1.0.2.vsix && \
    code-server --install-extension /tmp/Emeric-Defay.django-factory-0.0.9.vsix && \
    code-server --install-extension /tmp/shamanu4.django-intellisense-0.0.2.vsix

# Set up environment
WORKDIR /home/coder/project/workspace
ENV SHELL /bin/bash

# Entry point
ENTRYPOINT dumb-init fixuid -q /usr/bin/code-server --auth none --bind-addr 0.0.0.0:3000 /home/coder/project/workspace
