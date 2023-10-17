FROM python:3-alpine
# RUN mkdir app
# RUN cd app
WORKDIR /app

#Add requires
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
#ENTRYPOINT ["python"]
EXPOSE 5000
CMD ["python", "hw.py"]