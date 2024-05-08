#downloading current python file
FROM python:3.12-slim 

# Set the working directory in the container
WORKDIR /app

# Copy the_solution and google_maps_info into the container
COPY the_solution.py /app/
COPY google_maps_info.py /app/

# Expose port 4444
EXPOSE 4444

# Install the dependencies
RUN pip install requests
# Install Flask
RUN pip install Flask

# Run the Python script the_solution so program would start when we run the container
CMD ["python", "the_solution.py"]
