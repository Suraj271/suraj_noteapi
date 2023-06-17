from .models import Note
from .serializers import NoteSerializer
from rest_framework.generics import ListCreateAPIView , RetrieveUpdateDestroyAPIView

class NoteListCreateView(ListCreateAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

class NoteRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
