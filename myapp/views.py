
from django.shortcuts import render
import os
from django.http import FileResponse
from django.conf import settings

def index(request):
    return render(request, 'index.html')

def download_zip(request):
    # Path to the ZIP file
    zip_file_path = os.path.join(settings.BASE_DIR, 'zip_files', 'files.zip')
    
    # Serve the ZIP file
    response = FileResponse(open(zip_file_path, 'rb'), as_attachment=True, filename='files.zip')
    return response
