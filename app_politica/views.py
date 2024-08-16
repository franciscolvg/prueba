from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Partido
from .serializers import PartidoSerializer

@api_view(['GET'])
def listar_partidos(request):
    partidos = Partido.objects.all()
    serializer = PartidoSerializer(partidos, many=True)
    return Response(serializer.data)
