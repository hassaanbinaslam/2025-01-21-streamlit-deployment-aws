# Use the AWS Lambda Python base image
FROM public.ecr.aws/docker/library/python:3.12.1-slim

# Set the working directory
WORKDIR /app

# Copy app code and dependencies
COPY app.py requirements.txt ./

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Command to start Streamlit
CMD ["streamlit", "run", "app.py"]