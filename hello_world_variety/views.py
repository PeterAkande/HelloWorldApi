import json

from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


# Create your views here.

@api_view(['GET', 'POST'])
def call_helloworld(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        data = {
            'message': 'Hi, You are great'
        }
        return Response(data)

    elif request.method == 'POST':
        data = {
            'message': 'Hi, Yo gave me data You are great',
            'data': json.dumps(request.data),
        }
        return Response(data)

    else:
        return Response({'error': f'Method {request.method} is not allowed'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def just_helloworld(request):
    return Response({'message': 'I just Serve a Very Nice response, Thank You'})
