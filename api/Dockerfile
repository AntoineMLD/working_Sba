FROM python:3.11.0-slim

ENV PYTHONUNBUFFERED 1

# create directory for the app user
RUN mkdir -p /home/app

# create the app user
RUN addgroup --system app && adduser --system --group app

# create the appropriate directories
ENV HOME=/home/app
ENV APP_HOME=/home/app/web
RUN mkdir $APP_HOME
WORKDIR $APP_HOME

COPY requirements.txt $APP_HOME
RUN python -m pip install --upgrade pip 
RUN pip install --no-cache-dir -r requirements.txt

# copy project
COPY . $APP_HOME

# chown all the files to the app user
RUN chown -R app:app $APP_HOME

# change to the app user
USER app

EXPOSE 8001

#CMD ["uvicorn", "main:app", "--proxy-headers", "--host", "0.0.0.0", "--port", "8001"]