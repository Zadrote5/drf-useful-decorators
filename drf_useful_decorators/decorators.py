import functools
from django.db import transaction
from rest_framework import status
from .methods import get_response
    

def exceptions_endpoint(atomic: bool=True):    
    def wrapper(endpoint):
        @functools.wraps(endpoint)
        def inner(request, *args, **kwargs):
            try:
                if atomic:
                    with transaction.atomic():
                        return endpoint(request, *args, **kwargs)
                return endpoint(request, *args, **kwargs)
            except Exception as e:
                    return get_response(str(e), status.HTTP_400_BAD_REQUEST)
        return inner
    return wrapper