# Use python as base image
FROM python:3.8

# Use working directory /app/model
WORKDIR /app/model

# Copy and install required packages
COPY requirements.txt .
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Copy all the content of current directory to working directory
COPY . .
# Run flask app
CMD ["python","app.py"]
