FROM python:3.12

# Set work directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Collect static files (optional, for production)
RUN python manage.py collectstatic --noinput

# Expose port
EXPOSE 80

# Run the Django app using Gunicorn
CMD ["gunicorn", "politicalsite.wsgi:application", "--bind", "0.0.0.0:80"]