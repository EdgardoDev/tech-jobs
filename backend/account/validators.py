import os

def validate_file_extension(name):
    isValid = True
    
    ext = os.path.splitext(name)[1] # This will result on ('resume', '.pdf')
    valid_extensions = ['.pdf']
    
    if not ext.lower() in valid_extensions:
        isValid = False
        
    return isValid