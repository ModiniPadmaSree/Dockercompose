#Base Image
FROM python:3.9-slim

# Set Working Directory
WORKDIR /app

# Copy Dependency File
COPY requirements.txt .

# Install Dependencies
RUN pip install --no-cache-dir -r requirements.txt

#Copy Application Code
COPY app.py .

# Expose Application Port
EXPOSE 5000

# Command to run app
CMD ["python", "app.py"]
