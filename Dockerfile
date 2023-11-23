# Use the official Python image as the base image
FROM python:3.9

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SUPERUSER_PASSWORD 'admin'
ENV DJANGO_SUPERUSER_USERNAME 'admin'
ENV DJANGO_SUPERUSER_EMAIL 'admin@gmail.com'

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file to the working directory
COPY requirements.txt /app/

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code to the working directory
COPY . /app/

# Expose port 8000 for the Django application
EXPOSE 8000

# Command to run the application
#CMD ["python", "migrate", "&&", "python", "manage.py", "createsuperuser", "--no-input"]
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
