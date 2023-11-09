# Use an official Python runtime as a parent image
FROM python:3.9-slim-buster

# The environment variable ensures that the python output is set straight
# to the terminal without buffering it first
ENV PYTHONUNBUFFERED=1

# create root directory for our project in the container
RUN mkdir /app

# Set the working directory in the container to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY ./ /app/

# Install pip requirements
RUN pip install --no-cache-dir -r requirements.txt

# port where the Django app runs
EXPOSE 8000

# Start server
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]