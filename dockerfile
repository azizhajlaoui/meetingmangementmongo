# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Upgrade pip and install virtualenv
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir virtualenv

# Create and activate a virtual environment
RUN python -m venv venv
ENV PATH="/app/venv/bin:$PATH"
ENV VIRTUAL_ENV="/app/venv"

# Copy only the requirements file to leverage Docker cache
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /app
COPY ./app /app

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Run Flask application
CMD ["python", "app.py"]
