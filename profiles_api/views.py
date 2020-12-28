from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.

class HelloApiView(APIView):
    """Test API View"""

    def get(self, request, format=None):
        """Returns a list of API View Features"""
        an_apiview = [
            'Uses Http methods as function',
            'Is similar to a traditional Django View',
            'Gives you the most control over your app logic',
            'Is Mapped Manually to URLs',
        ]

        return Response({'message': 'Hello!', 'an_apiview': an_apiview})
