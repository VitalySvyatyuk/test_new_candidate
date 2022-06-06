from django.db.models import Prefetch
from django.db.models.aggregates import Sum
from django.db.models.expressions import F, OuterRef, Subquery
from rest_framework import mixins, viewsets


from .models import MonestroUser
from .serializers import MonestroUserSerializer


class UsersViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = MonestroUser.objects.all()
    serializer_class = MonestroUserSerializer

    def get_queryset(self):
        queryset = self.queryset
        """
        Task 2. Put your code here
        """
        return queryset
