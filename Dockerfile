FROM mcr.microsoft.com/mssql/server:2019-latest

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
COPY out /usr/src/app

RUN chmod +x /usr/src/app/run-initialization.sh

ENV SA_PASSWORD CorrectHorseBatteryStapleFor$
ENV ACCEPT_EULA Y
ENV MSSQL_PID Express

EXPOSE 1433

CMD /bin/bash ./entrypoint.sh