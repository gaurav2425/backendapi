from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import AmazonSerializers, GoogleSerializers, MicrosoftSerializers, TeslaSerializers, TrendingSerializers, HotSerializers, NewSerializers, ContactSerializers, AppleSerializers, FacebookSerializers, PrivacySerializers, CybersecuritySerializers, NetflixSerializers, SportsSerializers, TelevisionSerializers, FilmsSerializers, GamingSerializers, PhonesSerializers, LaptopsSerializers, CamerasSerializers, HeadphonesSerializers, SpeakersSerializers, YoutubeSerializers, InstagramSerializers, LinkedinSerializers, TwitterSerializers, NasaSerializers, SpacexSerializers, HealthSerializers, EnergySerializers, EnvironmentSerializers
from .models import Amazon, Google, Microsoft, Tesla, Trending, Hot, New, Contact, Apple, Facebook, Privacy, Cybersecurity, Netflix, Sports, Television, Films, Gaming, Phones, Laptops, Cameras, Headphones, Speakers, Youtube, Instagram, Linkedin, Twitter, Nasa, Spacex, Health, Energy, Environment


@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'Trending': '/trending',
        'Hot': '/hot',
        'New': '/new',
        'Amazon': '/amazon',
        'Google': '/google',
        'Microsoft': '/microsoft',
        'Tesla': '/tesla',
        'Apple': '/apple',
        'Facebook': '/facebook',
        'Privacy': '/privacy',
        'CyberSecurity': '/cybersecurity',
        'Netflix': '/netflix',
        'Television': '/television',
        'Films': '/films',
        'Phones': '/phones',
        'Laptops': '/laptops',
        'Cameras': '/cameras',
        'Speakers': '/speakers',
        'Headphones': '/headphones',
        'Youtube': '/youtube',
        'Instagram': '/instagram',
        'Linkedin': '/linkedin',
        'Twitter': '/twitter',
        'Nasa': '/nasa',



        'Contact': '/contact'
    }
    return Response(api_urls)


# Trending

@api_view(['GET'])
def TrendingOverview(request):
    api_urls = {
        'TrendingList': '/trending-list',
        'Detail view': '/trending-detail/<str:pk>/',
        'Create': '/trending-create/',
        'Update': '/trending-update/<str:pk>/',
        'Delete': '/trending-delete/<str:pk>/'
    }

    return Response(api_urls)


@api_view(['GET'])
def TrendingList(request):
    Tasks = Trending.objects.order_by('-id')
    serializer = TrendingSerializers(Tasks, many=True)
    ordering = ['-id']
    return Response(serializer.data)


@api_view(['GET'])
def TrendingDetail(request, pk):
    Tasks = Trending.objects.get(id=pk)
    serializer = TrendingSerializers(Tasks, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def TrendingCreate(request):
    serializer = TrendingSerializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def TrendingUpdate(request, pk):
    Tasks = Trending.objects.get(id=pk)
    serializer = TrendingSerializers(instance=Tasks, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def TrendingDelete(request, pk):
    Tasks = Trending.objects.get(id=pk)
    Tasks.delete()
    return Response('Item Successfully Deleted')


# Hot

@api_view(['GET'])
def HotOverview(request):
    api_urls = {
        'HotList': '/hot-list',
        'Detail view': '/hot-detail/<str:pk>/',
        'Create': '/hot-create/',
        'Update': '/hot-update/<str:pk>/',
        'Delete': '/hot-delete/<str:pk>/'
    }
    return Response(api_urls)


@api_view(['GET'])
def HotList(request):
    Tasks = Hot.objects.order_by('-id')
    serializer = HotSerializers(Tasks, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def HotDetail(request, pk):
    Tasks = Hot.objects.get(id=pk)
    serializer = HotSerializers(Tasks, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def HotCreate(request):
    serializer = HotSerializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def HotUpdate(request, pk):
    Tasks = Hot.objects.get(id=pk)
    serializer = HotSerializers(instance=Tasks, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def HotDelete(request, pk):
    Tasks = Hot.objects.get(id=pk)
    Tasks.delete()
    return Response('Item Successfully Deleted')

# New


@api_view(['GET'])
def NewOverview(request):
    api_urls = {
        'NewList': '/new-list',
        'Detail view': '/new-detail/<str:pk>/',
        'Create': '/new-create/',
        'Update': '/new-update/<str:pk>/',
        'Delete': '/new-delete/<str:pk>/'
    }

    return Response(api_urls)


@api_view(['GET'])
def NewList(request):
    Tasks = New.objects.order_by('-id')
    serializer = NewSerializers(Tasks, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def NewDetail(request, pk):
    Tasks = New.objects.get(id=pk)
    serializer = NewSerializers(Tasks, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def NewCreate(request):
    serializer = NewSerializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def NewUpdate(request, pk):
    Tasks = New.objects.get(id=pk)
    serializer = NewSerializers(instance=Tasks, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def NewDelete(request, pk):
    Tasks = New.objects.get(id=pk)
    Tasks.delete()
    return Response('Item Successfully Deleted')


# Amazon


@api_view(['GET'])
def AmazonOverview(request):
    api_urls = {
        'AmazonList': '/amazon-list',
        'Detail view': '/amazon-detail/<str:pk>/',
        'Create': '/amazon-create/',
        'Update': '/amazon-update/<str:pk>/',
        'Delete': '/amazon-delete/<str:pk>/'
    }

    return Response(api_urls)


@api_view(['GET'])
def amazonList(request):
    Tasks = Amazon.objects.all()
    serializer = AmazonSerializers(Tasks, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def amazonDetail(request, pk):
    Tasks = Amazon.objects.get(id=pk)
    serializer = AmazonSerializers(Tasks, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def amazonCreate(request):
    serializer = AmazonSerializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def amazonUpdate(request, pk):
    Tasks = Amazon.objects.get(id=pk)
    serializer = AmazonSerializers(instance=Tasks, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def amazonDelete(request, pk):
    Tasks = Amazon.objects.get(id=pk)
    Tasks.delete()
    return Response('Item Successfully Deleted')


# Google


@api_view(['GET'])
def GoogleOverview(request):
    api_urls = {
        'GoogleList': '/google-list',
        'Detail view': '/google-detail/<str:pk>/',
        'Create': '/google-create/',
        'Update': '/google-update/<str:pk>/',
        'Delete': '/google-delete/<str:pk>/'
    }

    return Response(api_urls)


@api_view(['GET'])
def GoogleList(request):
    Tasks = Google.objects.all()
    serializer = GoogleSerializers(Tasks, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def GoogleDetail(request, pk):
    Tasks = Google.objects.get(id=pk)
    serializer = GoogleSerializers(Tasks, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def GoogleCreate(request):
    serializer = GoogleSerializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def GoogleUpdate(request, pk):
    Tasks = Google.objects.get(id=pk)
    serializer = GoogleSerializers(instance=Tasks, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def GoogleDelete(request, pk):
    Tasks = Google.objects.get(id=pk)
    Tasks.delete()
    return Response('Item Successfully Deleted')


# Apple


@api_view(['GET'])
def AppleOverview(request):
    api_urls = {
        'AppleList': '/apple-list',
        'Detail view': '/apple-detail/<str:pk>/',
        'Create': '/apple-create/',
        'Update': '/apple-update/<str:pk>/',
        'Delete': '/apple-delete/<str:pk>/'
    }

    return Response(api_urls)


@api_view(['GET'])
def AppleList(request):
    Tasks = Apple.objects.all()
    serializer = AppleSerializers(Tasks, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def AppleDetail(request, pk):
    Tasks = Apple.objects.get(id=pk)
    serializer = AppleSerializers(Tasks, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def AppleCreate(request):
    serializer = AppleSerializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def AppleUpdate(request, pk):
    Tasks = Apple.objects.get(id=pk)
    serializer = AppleSerializers(instance=Tasks, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def AppleDelete(request, pk):
    Tasks = Apple.objects.get(id=pk)
    Tasks.delete()
    return Response('Item Successfully Deleted')


# Microsoft
@api_view(['GET'])
def MicrosoftOverview(request):
    api_urls = {
        'MicrosoftList': '/microsoft-list',
        'Detail view': '/microsoft-detail/<str:pk>/',
        'Create': '/microsoft-create/',
        'Update': '/microsoft-update/<str:pk>/',
        'Delete': '/microsoft-delete/<str:pk>/'
    }

    return Response(api_urls)


@api_view(['GET'])
def MicrosoftList(request):
    Tasks = Microsoft.objects.all()
    serializer = MicrosoftSerializers(Tasks, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def MicrosoftDetail(request, pk):
    Tasks = Microsoft.objects.get(id=pk)
    serializer = MicrosoftSerializers(Tasks, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def MicrosoftCreate(request):
    serializer = MicrosoftSerializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def MicrosoftUpdate(request, pk):
    Tasks = Microsoft.objects.get(id=pk)
    serializer = MicrosoftSerializers(instance=Tasks, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def MicrosoftDelete(request, pk):
    Tasks = Microsoft.objects.get(id=pk)
    Tasks.delete()
    return Response('Item Successfully Deleted')


# Tesla
@api_view(['GET'])
def TeslaOverview(request):
    api_urls = {
        'TeslaList': '/tesla-list',
        'Detail view': '/tesla-detail/<str:pk>',
        'Create': '/tesla-create/',
        'Update': '/tesla-update/<str:pk>/',
        'Delete': '/tesla-delete/<str:pk>/'
    }
    return Response(api_urls)


@api_view(['GET'])
def TeslaList(request):
    Tasks = Tesla.objects.all()
    serializer = TeslaSerializers(Tasks, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def TeslaDetail(request, pk):
    Tasks = Tesla.objects.get(id=pk)
    serializer = TeslaSerializers(Tasks, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def TeslaCreate(request):
    serializer = TeslaSerializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def TeslaUpdate(request, pk):
    Tasks = Tesla.objects.get(id=pk)
    serializer = TeslaSerializers(instance=Tasks, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def TeslaDelete(request, pk):
    Tasks = Tesla.objects.get(id=pk)
    Tasks.delete()
    return Response('Item Successfully Deleted')


# Facebook

@api_view(['GET'])
def FacebookOverview(request):
    api_urls = {
        'FacebookList': '/facebook-list',
        'Detail view': '/facebook-detail/<str:pk>/',
        'Create': '/facebook-create/',
        'Update': '/facebook-update/<str:pk>/',
        'Delete': '/facebook-delete/<str:pk>/'
    }

    return Response(api_urls)


@api_view(['GET'])
def FacebookList(request):
    Tasks = Facebook.objects.all()
    serializer = FacebookSerializers(Tasks, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def FacebookDetail(request, pk):
    Tasks = Facebook.objects.get(id=pk)
    serializer = FacebookSerializers(Tasks, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def FacebookCreate(request):
    serializer = FacebookSerializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def FacebookUpdate(request, pk):
    Tasks = Facebook.objects.get(id=pk)
    serializer = FacebookSerializers(instance=Tasks, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def FacebookDelete(request, pk):
    Tasks = Facebook.objects.get(id=pk)
    Tasks.delete()
    return Response('Item Successfully Deleted')


# Privacy

@api_view(['GET'])
def PrivacyOverview(request):
    api_urls = {
        'PrivacyList': '/privacy-list',
        'Detail view': '/privacy-detail/<str:pk>/',
        'Create': '/privacy-create/',
        'Update': '/privacy-update/<str:pk>/',
        'Delete': '/privacy-delete/<str:pk>/'
    }

    return Response(api_urls)


@api_view(['GET'])
def PrivacyList(request):
    Tasks = Privacy.objects.all()
    serializer = PrivacySerializers(Tasks, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def PrivacyDetail(request, pk):
    Tasks = Privacy.objects.get(id=pk)
    serializer = PrivacySerializers(Tasks, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def PrivacyCreate(request):
    serializer = PrivacySerializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def PrivacyUpdate(request, pk):
    Tasks = Privacy.objects.get(id=pk)
    serializer = PrivacySerializers(instance=Tasks, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def PrivacyDelete(request, pk):
    Tasks = Privacy.objects.get(id=pk)
    Tasks.delete()
    return Response('Item Successfully Deleted')


# Cybersecurity

@api_view(['GET'])
def CybersecurityOverview(request):
    api_urls = {
        'CybersecurityList': '/cybersecurity-list',
        'Detail view': '/cybersecurity-detail/<str:pk>/',
        'Create': '/cybersecurity-create/',
        'Update': '/cybersecurity-update/<str:pk>/',
        'Delete': '/cybersecurity-delete/<str:pk>/'
    }

    return Response(api_urls)


@api_view(['GET'])
def CybersecurityList(request):
    Tasks = Cybersecurity.objects.all()
    serializer = CybersecuritySerializers(Tasks, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def CybersecurityDetail(request, pk):
    Tasks = Cybersecurity.objects.get(id=pk)
    serializer = CybersecuritySerializers(Tasks, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def CybersecurityCreate(request):
    serializer = CybersecuritySerializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def CybersecurityUpdate(request, pk):
    Tasks = Cybersecurity.objects.get(id=pk)
    serializer = CybersecuritySerializers(instance=Tasks, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def CybersecurityDelete(request, pk):
    Tasks = Cybersecurity.objects.get(id=pk)
    Tasks.delete()
    return Response('Item Successfully Deleted')


# Netflix

@api_view(['GET'])
def NetflixOverview(request):
    api_urls = {
        'NetflixList': '/netflix-list',
        'Detail view': '/netflix-detail/<str:pk>/',
        'Create': '/netflix-create/',
        'Update': '/netflix-update/<str:pk>/',
        'Delete': '/netflix-delete/<str:pk>/'
    }

    return Response(api_urls)


@api_view(['GET'])
def NetflixList(request):
    Tasks = Netflix.objects.all()
    serializer = NetflixSerializers(Tasks, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def NetflixDetail(request, pk):
    Tasks = Netflix.objects.get(id=pk)
    serializer = NetflixSerializers(Tasks, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def NetflixCreate(request):
    serializer = NetflixSerializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def NetflixUpdate(request, pk):
    Tasks = Netflix.objects.get(id=pk)
    serializer = NetflixSerializers(instance=Tasks, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def NetflixDelete(request, pk):
    Tasks = Netflix.objects.get(id=pk)
    Tasks.delete()
    return Response('Item Successfully Deleted')


# Sports

@api_view(['GET'])
def SportsOverview(request):
    api_urls = {
        'SportsList': '/Sports-list',
        'Detail view': '/Sports-detail/<str:pk>/',
        'Create': '/Sports-create/',
        'Update': '/Sports-update/<str:pk>/',
        'Delete': '/Sports-delete/<str:pk>/'
    }

    return Response(api_urls)


@api_view(['GET'])
def SportsList(request):
    Tasks = Sports.objects.all()
    serializer = SportsSerializers(Tasks, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def SportsDetail(request, pk):
    Tasks = Sports.objects.get(id=pk)
    serializer = SportsSerializers(Tasks, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def SportsCreate(request):
    serializer = SportsSerializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def SportsUpdate(request, pk):
    Tasks = Sports.objects.get(id=pk)
    serializer = SportsSerializers(instance=Tasks, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def SportsDelete(request, pk):
    Tasks = Sports.objects.get(id=pk)
    Tasks.delete()
    return Response('Item Successfully Deleted')


# Television

@api_view(['GET'])
def TelevisionOverview(request):
    api_urls = {
        'TelevisionList': '/television-list',
        'Detail view': '/television-detail/<str:pk>/',
        'Create': '/television-create/',
        'Update': '/television-update/<str:pk>/',
        'Delete': '/television-delete/<str:pk>/'
    }

    return Response(api_urls)


@api_view(['GET'])
def TelevisionList(request):
    Tasks = Television.objects.all()
    serializer = TelevisionSerializers(Tasks, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def TelevisionDetail(request, pk):
    Tasks = Television.objects.get(id=pk)
    serializer = TelevisionSerializers(Tasks, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def TelevisionCreate(request):
    serializer = TelevisionSerializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def TelevisionUpdate(request, pk):
    Tasks = Television.objects.get(id=pk)
    serializer = TelevisionSerializers(instance=Tasks, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def TelevisionDelete(request, pk):
    Tasks = Television.objects.get(id=pk)
    Tasks.delete()
    return Response('Item Successfully Deleted')


# Films

@api_view(['GET'])
def FilmsOverview(request):
    api_urls = {
        'FilmsList': '/films-list',
        'Detail view': '/films-detail/<str:pk>/',
        'Create': '/films-create/',
        'Update': '/films-update/<str:pk>/',
        'Delete': '/films-delete/<str:pk>/'
    }

    return Response(api_urls)


@api_view(['GET'])
def FilmsList(request):
    Tasks = Films.objects.all()
    serializer = FilmsSerializers(Tasks, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def FilmsDetail(request, pk):
    Tasks = Films.objects.get(id=pk)
    serializer = FilmsSerializers(Tasks, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def FilmsCreate(request):
    serializer = FilmsSerializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def FilmsUpdate(request, pk):
    Tasks = Films.objects.get(id=pk)
    serializer = FilmsSerializers(instance=Tasks, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def FilmsDelete(request, pk):
    Tasks = Films.objects.get(id=pk)
    Tasks.delete()
    return Response('Item Successfully Deleted')


# Gaming

@api_view(['GET'])
def GamingOverview(request):
    api_urls = {
        'GamingList': '/gaming-list',
        'Detail view': '/gaming-detail/<str:pk>/',
        'Create': '/gaming-create/',
        'Update': '/gaming-update/<str:pk>/',
        'Delete': '/gaming-delete/<str:pk>/'
    }

    return Response(api_urls)


@api_view(['GET'])
def GamingList(request):
    Tasks = Gaming.objects.all()
    serializer = GamingSerializers(Tasks, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def GamingDetail(request, pk):
    Tasks = Gaming.objects.get(id=pk)
    serializer = GamingSerializers(Tasks, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def GamingCreate(request):
    serializer = GamingSerializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def GamingUpdate(request, pk):
    Tasks = Gaming.objects.get(id=pk)
    serializer = GamingSerializers(instance=Tasks, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def GamingDelete(request, pk):
    Tasks = Gaming.objects.get(id=pk)
    Tasks.delete()
    return Response('Item Successfully Deleted')


# Phones

@api_view(['GET'])
def PhonesOverview(request):
    api_urls = {
        'PhonesList': '/phones-list',
        'Detail view': '/phones-detail/<str:pk>/',
        'Create': '/phones-create/',
        'Update': '/phones-update/<str:pk>/',
        'Delete': '/phones-delete/<str:pk>/'
    }

    return Response(api_urls)


@api_view(['GET'])
def PhonesList(request):
    Tasks = Phones.objects.all()
    serializer = PhonesSerializers(Tasks, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def PhonesDetail(request, pk):
    Tasks = Phones.objects.get(id=pk)
    serializer = PhonesSerializers(Tasks, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def PhonesCreate(request):
    serializer = PhonesSerializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def PhonesUpdate(request, pk):
    Tasks = Phones.objects.get(id=pk)
    serializer = PhonesSerializers(instance=Tasks, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def PhonesDelete(request, pk):
    Tasks = Phones.objects.get(id=pk)
    Tasks.delete()
    return Response('Item Successfully Deleted')


# Laptops

@api_view(['GET'])
def LaptopsOverview(request):
    api_urls = {
        'LaptopsList': '/laptops-list',
        'Detail view': '/laptops-detail/<str:pk>/',
        'Create': '/laptops-create/',
        'Update': '/laptops-update/<str:pk>/',
        'Delete': '/laptops-delete/<str:pk>/'
    }

    return Response(api_urls)


@api_view(['GET'])
def LaptopsList(request):
    Tasks = Laptops.objects.all()
    serializer = LaptopsSerializers(Tasks, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def LaptopsDetail(request, pk):
    Tasks = Laptops.objects.get(id=pk)
    serializer = LaptopsSerializers(Tasks, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def LaptopsCreate(request):
    serializer = LaptopsSerializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def LaptopsUpdate(request, pk):
    Tasks = Laptops.objects.get(id=pk)
    serializer = LaptopsSerializers(instance=Tasks, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def LaptopsDelete(request, pk):
    Tasks = Laptops.objects.get(id=pk)
    Tasks.delete()
    return Response('Item Successfully Deleted')


# Cameras

@api_view(['GET'])
def CamerasOverview(request):
    api_urls = {
        'CamerasList': '/cameras-list',
        'Detail view': '/cameras-detail/<str:pk>/',
        'Create': '/cameras-create/',
        'Update': '/cameras-update/<str:pk>/',
        'Delete': '/cameras-delete/<str:pk>/'
    }

    return Response(api_urls)


@api_view(['GET'])
def CamerasList(request):
    Tasks = Cameras.objects.all()
    serializer = CamerasSerializers(Tasks, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def CamerasDetail(request, pk):
    Tasks = Cameras.objects.get(id=pk)
    serializer = CamerasSerializers(Tasks, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def CamerasCreate(request):
    serializer = CamerasSerializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def CamerasUpdate(request, pk):
    Tasks = Cameras.objects.get(id=pk)
    serializer = CamerasSerializers(instance=Tasks, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def CamerasDelete(request, pk):
    Tasks = Cameras.objects.get(id=pk)
    Tasks.delete()
    return Response('Item Successfully Deleted')


# Speakers


@api_view(['GET'])
def SpeakersOverview(request):
    api_urls = {
        'SpeakersList': '/speakers-list',
        'Detail view': '/speakers-detail/<str:pk>/',
        'Create': '/speakers-create/',
        'Update': '/speakers-update/<str:pk>/',
        'Delete': '/speakers-delete/<str:pk>/'
    }

    return Response(api_urls)


@api_view(['GET'])
def SpeakersList(request):
    Tasks = Speakers.objects.all()
    serializer = SpeakersSerializers(Tasks, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def SpeakersDetail(request, pk):
    Tasks = Speakers.objects.get(id=pk)
    serializer = SpeakersSerializers(Tasks, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def SpeakersCreate(request):
    serializer = SpeakersSerializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def SpeakersUpdate(request, pk):
    Tasks = Speakers.objects.get(id=pk)
    serializer = SpeakersSerializers(instance=Tasks, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def SpeakersDelete(request, pk):
    Tasks = Speakers.objects.get(id=pk)
    Tasks.delete()
    return Response('Item Successfully Deleted')


# Headphones


@api_view(['GET'])
def HeadphonesOverview(request):
    api_urls = {
        'HeadphonesList': '/headphones-list',
        'Detail view': '/headphones-detail/<str:pk>/',
        'Create': '/headphones-create/',
        'Update': '/headphones-update/<str:pk>/',
        'Delete': '/headphones-delete/<str:pk>/'
    }

    return Response(api_urls)


@api_view(['GET'])
def HeadphonesList(request):
    Tasks = Headphones.objects.all()
    serializer = HeadphonesSerializers(Tasks, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def HeadphonesDetail(request, pk):
    Tasks = Headphones.objects.get(id=pk)
    serializer = HeadphonesSerializers(Tasks, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def HeadphonesCreate(request):
    serializer = HeadphonesSerializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def HeadphonesUpdate(request, pk):
    Tasks = Headphones.objects.get(id=pk)
    serializer = HeadphonesSerializers(instance=Tasks, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def HeadphonesDelete(request, pk):
    Tasks = Headphones.objects.get(id=pk)
    Tasks.delete()
    return Response('Item Successfully Deleted')


# Youtube


@api_view(['GET'])
def YoutubeOverview(request):
    api_urls = {
        'YoutubeList': '/youtube-list',
        'Detail view': '/youtube-detail/<str:pk>/',
        'Create': '/youtube-create/',
        'Update': '/youtube-update/<str:pk>/',
        'Delete': '/youtube-delete/<str:pk>/'
    }

    return Response(api_urls)


@api_view(['GET'])
def YoutubeList(request):
    Tasks = Youtube.objects.all()
    serializer = YoutubeSerializers(Tasks, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def YoutubeDetail(request, pk):
    Tasks = Youtube.objects.get(id=pk)
    serializer = YoutubeSerializers(Tasks, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def YoutubeCreate(request):
    serializer = YoutubeSerializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def YoutubeUpdate(request, pk):
    Tasks = Youtube.objects.get(id=pk)
    serializer = YoutubeSerializers(instance=Tasks, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def YoutubeDelete(request, pk):
    Tasks = Youtube.objects.get(id=pk)
    Tasks.delete()
    return Response('Item Successfully Deleted')


# Instagram


@api_view(['GET'])
def InstagramOverview(request):
    api_urls = {
        'InstagramList': '/instagram-list',
        'Detail view': '/instagram-detail/<str:pk>/',
        'Create': '/instagram-create/',
        'Update': '/instagram-update/<str:pk>/',
        'Delete': '/instagram-delete/<str:pk>/'
    }

    return Response(api_urls)


@api_view(['GET'])
def InstagramList(request):
    Tasks = Instagram.objects.all()
    serializer = InstagramSerializers(Tasks, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def InstagramDetail(request, pk):
    Tasks = Instagram.objects.get(id=pk)
    serializer = InstagramSerializers(Tasks, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def InstagramCreate(request):
    serializer = InstagramSerializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def InstagramUpdate(request, pk):
    Tasks = Instagram.objects.get(id=pk)
    serializer = InstagramSerializers(instance=Tasks, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def InstagramDelete(request, pk):
    Tasks = Instagram.objects.get(id=pk)
    Tasks.delete()
    return Response('Item Successfully Deleted')


# Linkedin


@api_view(['GET'])
def LinkedinOverview(request):
    api_urls = {
        'LinkedinList': '/linkedin-list',
        'Detail view': '/linkedin-detail/<str:pk>/',
        'Create': '/linkedin-create/',
        'Update': '/linkedin-update/<str:pk>/',
        'Delete': '/linkedin-delete/<str:pk>/'
    }

    return Response(api_urls)


@api_view(['GET'])
def LinkedinList(request):
    Tasks = Linkedin.objects.all()
    serializer = LinkedinSerializers(Tasks, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def LinkedinDetail(request, pk):
    Tasks = Linkedin.objects.get(id=pk)
    serializer = LinkedinSerializers(Tasks, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def LinkedinCreate(request):
    serializer = LinkedinSerializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def LinkedinUpdate(request, pk):
    Tasks = Linkedin.objects.get(id=pk)
    serializer = LinkedinSerializers(instance=Tasks, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def LinkedinDelete(request, pk):
    Tasks = Linkedin.objects.get(id=pk)
    Tasks.delete()
    return Response('Item Successfully Deleted')


# Twitter


@api_view(['GET'])
def TwitterOverview(request):
    api_urls = {
        'TwitterList': '/twitter-list',
        'Detail view': '/twitter-detail/<str:pk>/',
        'Create': '/twitter-create/',
        'Update': '/twitter-update/<str:pk>/',
        'Delete': '/twitter-delete/<str:pk>/'
    }

    return Response(api_urls)


@api_view(['GET'])
def TwitterList(request):
    Tasks = Twitter.objects.all()
    serializer = TwitterSerializers(Tasks, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def TwitterDetail(request, pk):
    Tasks = Twitter.objects.get(id=pk)
    serializer = TwitterSerializers(Tasks, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def TwitterCreate(request):
    serializer = TwitterSerializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def TwitterUpdate(request, pk):
    Tasks = Twitter.objects.get(id=pk)
    serializer = TwitterSerializers(instance=Tasks, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def TwitterDelete(request, pk):
    Tasks = Twitter.objects.get(id=pk)
    Tasks.delete()
    return Response('Item Successfully Deleted')


# Nasa


@api_view(['GET'])
def NasaOverview(request):
    api_urls = {
        'NasaList': '/nasa-list',
        'Detail view': '/nasa-detail/<str:pk>/',
        'Create': '/nasa-create/',
        'Update': '/nasa-update/<str:pk>/',
        'Delete': '/nasa-delete/<str:pk>/'
    }

    return Response(api_urls)


@api_view(['GET'])
def NasaList(request):
    Tasks = Nasa.objects.all()
    serializer = NasaSerializers(Tasks, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def NasaDetail(request, pk):
    Tasks = Nasa.objects.get(id=pk)
    serializer = NasaSerializers(Tasks, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def NasaCreate(request):
    serializer = NasaSerializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def NasaUpdate(request, pk):
    Tasks = Nasa.objects.get(id=pk)
    serializer = NasaSerializers(instance=Tasks, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def NasaDelete(request, pk):
    Tasks = Nasa.objects.get(id=pk)
    Tasks.delete()
    return Response('Item Successfully Deleted')


# Spacex


@api_view(['GET'])
def SpacexOverview(request):
    api_urls = {
        'SpacexList': '/spacex-list',
        'Detail view': '/spacex-detail/<str:pk>/',
        'Create': '/spacex-create/',
        'Update': '/spacex-update/<str:pk>/',
        'Delete': '/spacex-delete/<str:pk>/'
    }

    return Response(api_urls)


@api_view(['GET'])
def SpacexList(request):
    Tasks = Spacex.objects.all()
    serializer = SpacexSerializers(Tasks, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def SpacexDetail(request, pk):
    Tasks = Spacex.objects.get(id=pk)
    serializer = SpacexSerializers(Tasks, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def SpacexCreate(request):
    serializer = SpacexSerializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def SpacexUpdate(request, pk):
    Tasks = Spacex.objects.get(id=pk)
    serializer = SpacexSerializers(instance=Tasks, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def SpacexDelete(request, pk):
    Tasks = Spacex.objects.get(id=pk)
    Tasks.delete()
    return Response('Item Successfully Deleted')


# Health


@api_view(['GET'])
def HealthOverview(request):
    api_urls = {
        'HealthList': '/health-list',
        'Detail view': '/health-detail/<str:pk>/',
        'Create': '/health-create/',
        'Update': '/health-update/<str:pk>/',
        'Delete': '/health-delete/<str:pk>/'
    }

    return Response(api_urls)


@api_view(['GET'])
def HealthList(request):
    Tasks = Health.objects.all()
    serializer = HealthSerializers(Tasks, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def HealthDetail(request, pk):
    Tasks = Health.objects.get(id=pk)
    serializer = HealthSerializers(Tasks, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def HealthCreate(request):
    serializer = HealthSerializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def HealthUpdate(request, pk):
    Tasks = Health.objects.get(id=pk)
    serializer = HealthSerializers(instance=Tasks, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def HealthDelete(request, pk):
    Tasks = Health.objects.get(id=pk)
    Tasks.delete()
    return Response('Item Successfully Deleted')


# Energy


@api_view(['GET'])
def EnergyOverview(request):
    api_urls = {
        'EnergyList': '/energy-list',
        'Detail view': '/energy-detail/<str:pk>/',
        'Create': '/energy-create/',
        'Update': '/energy-update/<str:pk>/',
        'Delete': '/energy-delete/<str:pk>/'
    }

    return Response(api_urls)


@api_view(['GET'])
def EnergyList(request):
    Tasks = Energy.objects.all()
    serializer = EnergySerializers(Tasks, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def EnergyDetail(request, pk):
    Tasks = Energy.objects.get(id=pk)
    serializer = EnergySerializers(Tasks, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def EnergyCreate(request):
    serializer = EnergySerializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def EnergyUpdate(request, pk):
    Tasks = Energy.objects.get(id=pk)
    serializer = EnergySerializers(instance=Tasks, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def EnergyDelete(request, pk):
    Tasks = Energy.objects.get(id=pk)
    Tasks.delete()
    return Response('Item Successfully Deleted')


# Environment


@api_view(['GET'])
def EnvironmentOverview(request):
    api_urls = {
        'EnvironmentList': '/environment-list',
        'Detail view': '/environment-detail/<str:pk>/',
        'Create': '/environment-create/',
        'Update': '/environment-update/<str:pk>/',
        'Delete': '/environment-delete/<str:pk>/'
    }

    return Response(api_urls)


@api_view(['GET'])
def EnvironmentList(request):
    Tasks = Environment.objects.all()
    serializer = EnvironmentSerializers(Tasks, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def EnvironmentDetail(request, pk):
    Tasks = Environment.objects.get(id=pk)
    serializer = EnvironmentSerializers(Tasks, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def EnvironmentCreate(request):
    serializer = EnvironmentSerializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def EnvironmentUpdate(request, pk):
    Tasks = Environment.objects.get(id=pk)
    serializer = EnvironmentSerializers(instance=Tasks, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def EnvironmentDelete(request, pk):
    Tasks = Environment.objects.get(id=pk)
    Tasks.delete()
    return Response('Item Successfully Deleted')


# Contact
@api_view(['GET'])
def ContactOverview(request):
    api_urls = {
        'ContactList': '/contact-list',
        'Detail view': '/contact-detail/<str:pk>/',
        'Create': 'contact-create/',
        'Delete': '/contact-delete/<str:pk>/'
    }

    return Response(api_urls)


@api_view(['GET'])
def ContactList(request):
    Tasks = Contact.objects.all()
    serializer = ContactSerializers(Tasks, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def ContactDetail(request, pk):
    Tasks = Contact.objects.get(id=pk)
    serializer = ContactSerializers(Tasks, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def ContactCreate(request):
    serializer = ContactSerializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def ContactDelete(request, pk):
    Tasks = Contact.objects.get(id=pk)
    Tasks.delete()
    return Response('Item Successfully Deleted')
