from rest_framework.response import Response
from rest_framework import status


def get_response(detail: str, status=status.HTTP_200_OK):
    return Response(
                    data={
                        'detail': detail
                        },
                    status=status
                )