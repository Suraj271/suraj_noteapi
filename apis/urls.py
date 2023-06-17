from django.urls import path
from apis import views

urlpatterns = [
    path('notes/', views.NoteListCreateView.as_view(), name='note_create'),
    path('notes/<int:pk>/', views.NoteRetrieveUpdateDestroyView.as_view(), name='notes_update'),
]
