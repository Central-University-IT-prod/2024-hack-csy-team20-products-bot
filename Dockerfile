# Use the official lightweight Python image.
FROM python:3.8-slim

# Set the working directory in the container.
WORKDIR /app

# Copy the requirements.txt first to leverage Docker cache.
COPY requirements.txt /app/requirements.txt

# Install the necessary packages.
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your code into the container.
COPY . /app

# Run the application.
CMD ["python", "main.py"]
