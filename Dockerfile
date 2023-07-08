FROM python:3.10
RUN mkdir dataQualityFramework
RUN chmod 777 dataQualityFramework
WORKDIR /dataQualityFramework
COPY . ./
RUN pip install -r requirements.txt
CMD [ "python", "fetch_api_data.py" ]