# Use an official base image (e.g., Ubuntu or a Python image)
FROM ubuntu:20.04

# Install dependencies (Squish requires certain libraries)
RUN apt-get update && apt-get install -y \
    libx11-6 \
    libgl1-mesa-glx \
    libglib2.0-0 \
    wget \
    unzip \
    && rm -rf /var/lib/apt/lists/*

# Download and Install Squish using authentication
RUN wget --user= --password= https://download.froglogic.com/squish/squish-6.7.1-linux64.zip -O /tmp/squish.zip \
    && unzip /tmp/squish.zip -d /opt/squish \
    && rm /tmp/squish.zip

# Set Squish environment variables
ENV PATH="/opt/squish/squish-6.7.1/bin:$PATH"

# Set the working directory
WORKDIR /app

# Copy your project files into the container
COPY . /app

# Install Python dependencies if needed
RUN apt-get install -y python3 python3-pip
RUN pip3 install -r requirements.txt

# Define the default command to run the Squish test
CMD ["squishrunner", "--testsuite", "/app/testsuite"]
