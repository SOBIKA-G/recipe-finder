# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements.txt first to leverage Docker caching
COPY requirements.txt /app/

# Install any required packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project directory to the container
COPY . /app/

# Expose the port the app runs on
EXPOSE 8000

# Run the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
