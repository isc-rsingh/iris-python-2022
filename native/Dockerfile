# For an M1 Mac, comment the line below and uncomment the one pulling irishealth-community-arm64
#ARG IMAGE=containers.intersystems.com/intersystems/iris-community:2022.1.0.209.0
ARG IMAGE=containers.intersystems.com/intersystems/iris-community-arm64:2022.1.0.209.0

FROM $IMAGE
USER root
WORKDIR /opt/irisbuild

COPY src src
COPY Installer.cls Installer.cls
COPY iris.script iris.script

COPY intersystems_irispython-3.2.0-py3-none-any.whl intersystems_irispython-3.2.0-py3-none-any.whl

RUN chown -R ${ISC_PACKAGE_MGRUSER}:${ISC_PACKAGE_IRISGROUP} /opt/irisbuild
USER ${ISC_PACKAGE_MGRUSER}

RUN pip install intersystems_irispython-3.2.0-py3-none-any.whl

## prepare IRIS
RUN iris start IRIS \
    && iris session IRIS < iris.script \
    && iris stop IRIS quietly
