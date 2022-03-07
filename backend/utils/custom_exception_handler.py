from rest_framework.views import exception_handler

def custom_exception_handler(exc, context):
    
    response = exception_handler(exc, context)
    
    exception_class = exc.__class__.__name__
    
    if exception_class == 'AuthenticationFailed':
        response.data = {
            'error': 'Invalid Email Or Password. Please Try Again!'
        }
        
    if exception_class == 'NotAuthenticated':
        response.data = {
        'error': 'Please Login First To Access This Resource!'
    }
        
    if exception_class == 'InvalidToken':
            response.data = {
        'error': 'Your Authentication Token Has Expire. Please Login Again!'
    }
    
    return response
