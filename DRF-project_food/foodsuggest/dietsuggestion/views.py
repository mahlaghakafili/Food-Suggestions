from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from .serializers import UserSerializer
from .models import User


class HomePage(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'homepage.html'

    def get(self, request):
        return Response({'profiles': {}})


class Login(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'login.html'

    def get(self, request):
        return Response({'profiles': {}})


class Bmi(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'bmi.html'

    def get(self, request):

        user = get_object_or_404(User, pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def post(self, request):
        rr = UserSerializer(data=request.data)
        print(rr.data)
        profiles = UserSerializer(data=request.data)
        return Response({'profiles': profiles})


class Result(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'result.html'

    def get(self, request):
        return Response({'profiles':{}})

    def post(self, request):
        return Response({'profiles': {}})


class Info(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'info.html'

    def get(self, request):
        return Response({'profiles':{}})

    def post(self, request):
        return Response({'profiles': {}})


class Contact(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'contact.html'

    def get(self, request):
        return Response({'profiles':{}})

    def post(self, request):
        return Response({'profiles': {}})


class LifeStyle(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'lifestyle.html'

    def get(self, request):
        return Response({'profiles':{}})

    def post(self, request):
        return Response({'profiles': {}})


class Suggestion(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'suggestion.html'

    def get(self, request):
        return Response({'profiles':{}})

    def post(self, request):
        return Response({'profiles': {}})


class Logout(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'logout.html'

    def get(self, request):
        return Response({'profiles':{}})

    def post(self, request):
        return Response({'profiles': {}})


class AdminPage(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'own_adminpage.html'

    def get(self, request):
        return Response({'profiles':{}})

    def post(self, request):
        return Response({'profiles': {}})

