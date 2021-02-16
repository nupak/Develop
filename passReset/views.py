from django.shortcuts import render

from rest_framework import status
from rest_framework import generics
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from .serializers import ChangePasswordSerializer
from rest_framework.permissions import IsAuthenticated

class ChangePasswordView(generics.UpdateAPIView):
    """
    ЭНДПОИНТ для смены пароля
    """
    serializer_class = ChangePasswordSerializer
    model = get_user_model()
    permission_classes = (IsAuthenticated,)

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            # Проверка старого пароля
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
            # set_password also hashes the password that the user will get
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Password updated successfully',
                'data': []
            }
            return Response(response)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)