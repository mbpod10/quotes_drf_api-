from rest_framework import generics


from .serializers import QuoteSerializer
from quotes.models import Quote
from .permissions import IsAdminOrReadOnly


class QuoteListView(generics.ListCreateAPIView):
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer
    permission_classes = [IsAdminOrReadOnly]
