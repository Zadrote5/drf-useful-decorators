import functools
from django.db import transaction
from rest_framework import status
from .methods import get_response
    
    
def exceptions_endpoint(endpoint):
    @functools.wraps(endpoint)
    def inner(request, *args, **kwargs):
        try:
            return transaction.atomic(endpoint(request, *args, **kwargs))
        except Exception as e:
                return get_response(str(e), status.HTTP_400_BAD_REQUEST)
    return inner