# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install flask

# Make port available to the world outside this container
EXPOSE XXXXX

# Run app.py when the container launches
CMD ["python", "app.py"]