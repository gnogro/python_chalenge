# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app
COPY ./sql.sql /docker-entrypoint-initdb.d/
# Install any needed packages specified in requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Make port 5000 available to the world outside this container
EXPOSE 6000
EXPOSE 6001
EXPOSE 5432

# Run the application
CMD ["python", "app.py"]