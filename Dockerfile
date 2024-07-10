# Use a slim python image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Install reportlab library
RUN pip install reportlab

# Copy your Python script and any other required files
COPY . .

# Define the command to run your script
CMD ["python", "master_maths.py", "{digits}", "{output_filename}"]
