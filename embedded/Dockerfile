ARG IMAGE=arti.iscinternal.com/ç/iris:2021.1.0PYTHON.330.0
# For an M1 Mac, comment the line below and uncomment the one pulling irishealth-community-arm64
#ARG IMAGE=containers.intersystems.com/intersystems/iris-community:2022.1.0.199.0
ARG IMAGE=containers.intersystems.com/intersystems/iris-community-arm64:2022.1.0.199.0

FROM $IMAGE
USER root
WORKDIR /opt/irisbuild

COPY src src
COPY Installer.cls Installer.cls
COPY iris.script iris.script
COPY requirements.txt requirements.txt

RUN chown -R ${ISC_PACKAGE_MGRUSER}:${ISC_PACKAGE_IRISGROUP} /opt/irisbuild
USER ${ISC_PACKAGE_MGRUSER}

ENV PYTHON_PATH /usr/irissys/bin/irispython
ENV IRISUSERNAME "SuperUser"
ENV IRISPASSWORD $IRIS_PASSWORD
ENV PATH "/usr/irissys/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/home/irisowner/bin"

RUN ${PYTHON_PATH} -m pip install -r requirements.txt

## prepare IRIS
RUN iris start IRIS \
    && iris session IRIS < iris.script \
    && iris stop IRIS quietly
