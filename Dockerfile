# Use official Python base image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install Python dependencies
RUN pip install --upgrade pip
RUN pip install streamlit mysql-connector-python

# Expose the port that Streamlit listens on (default is 8501)
EXPOSE 8501

# Command to run the Streamlit app
CMD ["streamlit", "run", "main.py"]
