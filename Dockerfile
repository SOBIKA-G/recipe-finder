# Use an official Python runtime as a parent image
FROM python:3.9

# Set environment variables to prevent .pyc files and buffered output
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory in the container to /app
WORKDIR /app

# Copy the requirements.txt file into the container
COPY requirements.txt /app/

# Install any dependencies
RUN pip install -r requirements.txt

# Copy the rest of the project files into the container
COPY . /app/

# Expose port 8000 to the outside world
EXPOSE 8000

# Run the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
