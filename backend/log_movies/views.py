
# Import the base ViewSet class for creating API endpoints
from rest_framework import viewsets
# Import the UserMovieList model to interact with user-movie relationships
from .models import UserMovieList
# Import the serializer to convert model instances to JSON and vice versa
from .serializers import UserMovieListSerializer
# Import permission class to restrict access to authenticated users only
from rest_framework.permissions import IsAuthenticated

# Create your views here. (Django convention comment)

# ViewSet for handling UserMovieList API endpoints (CRUD operations)
class UserMovieListViewSet(viewsets.ModelViewSet):
    # Specifies which serializer to use for this viewset
    serializer_class = UserMovieListSerializer
    # Restricts access to authenticated users only
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        Returns the queryset of UserMovieList objects for the current authenticated user only.
        self: The viewset instance
        self.request.user: The currently authenticated user making the request
        """
        return UserMovieList.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        """
        Called when a new UserMovieList object is created via POST.
        serializer: The serializer instance containing validated data
        Sets the user field to the current authenticated user before saving.
        """
        serializer.save(user=self.request.user)

