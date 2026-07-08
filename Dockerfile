# Use an official Python runtime as a parent image
FROM python:3.9.25

# Set the working directory
WORKDIR .

# Copy the current directory contents into the container at the same level
COPY . .

# Install the Python dependencies
RUN pip install -r requirements.txt
RUN python3.9.25 -m pip install pytest

# Make port 8070 available to the world outside this container
EXPOSE 8070

# Run the application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8070"]
