# Use the AWS Lambda Python base image
FROM public.ecr.aws/docker/library/python:3.12.1-slim

# Add the AWS Lambda Web Adapter
COPY --from=public.ecr.aws/awsguru/aws-lambda-adapter:0.8.4 /lambda-adapter /opt/extensions/lambda-adapter

# Set the working directory
WORKDIR /var/task

# Copy app code and dependencies
COPY app.py requirements.txt ./

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Command to start Streamlit
CMD ["streamlit", "run", "app.py", "--server.port=8080"]