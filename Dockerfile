FROM ubuntu:latest

# Install Python and pip
RUN apt-get update && \
    apt-get install -y python3 python3-pip

# Set the working directory
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip3 install -r requirements.txt

# Copy the FastAPI project files
COPY . .

# Expose the port that the FastAPI app will run on
EXPOSE 8000

# Start the FastAPI app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]