from django.urls import path, include
from . import views
urlpatterns = [


    path('trending/', views.TrendingOverview, name='trending-overview'),
    path('trending/trending-list', views.TrendingList, name='trending-list'),
    path('trending/trending-detail/<str:pk>/',
         views.TrendingDetail, name='trending-detail'),
    path('trending/trending-create/',
         views.TrendingCreate, name='trending-create'),
    path('trending/trending-update/<str:pk>/',
         views.TrendingUpdate, name='trending-update'),
    path('trending/trending-delete/<str:pk>/',
         views.TrendingDelete, name='trending-delete'),


    path('hot/', views.HotOverview, name='hot-overview'),
    path('hot/hot-list', views.HotList, name='hot-list'),
    path('hot/hot-detail/<str:pk>/',
         views.HotDetail, name='hot-detail'),
    path('hot/hot-create/',
         views.HotCreate, name='hot-create'),
    path('hot/hot-update/<str:pk>/',
         views.HotUpdate, name='hot-update'),
    path('hot/hot-delete/<str:pk>/',
         views.HotDelete, name='hot-delete'),


    path('new/', views.NewOverview, name='new-overview'),
    path('new/new-list', views.NewList, name='new-list'),
    path('new/new-detail/<str:pk>/',
         views.NewDetail, name='new-detail'),
    path('new/new-create/',
         views.NewCreate, name='new-create'),
    path('new/new-update/<str:pk>/',
         views.NewUpdate, name='new-update'),
    path('new/new-delete/<str:pk>/',
         views.NewDelete, name='new-delete'),


    path('amazon/', views.AmazonOverview, name='amazon-overview'),
    path('amazon/amazon-list', views.amazonList, name='amazon-list'),
    path('amazon/amazon-detail/<str:pk>/',
         views.amazonDetail, name='amazon-detail'),
    path('amazon/amazon-create/',
         views.amazonCreate, name='amazon-create'),
    path('amazon/amazon-update/<str:pk>/',
         views.amazonUpdate, name='amazon-update'),
    path('amazon/amazon-delete/<str:pk>/',
         views.amazonDelete, name='amazon-delete'),



    path('google/', views.GoogleOverview, name='google-overview'),
    path('google/google-list', views.GoogleList, name='google-list'),
    path('google/google-detail/<str:pk>/',
         views.GoogleDetail, name='google-detail'),
    path('google/google-create/',
         views.GoogleCreate, name='google-create'),
    path('google/google-update/<str:pk>/',
         views.GoogleUpdate, name='google-update'),
    path('google/google-delete/<str:pk>/',
         views.GoogleDelete, name='google-delete'),



    path('microsoft/', views.MicrosoftOverview, name='microsoft-overview'),
    path('microsoft/microsoft-list',
         views.MicrosoftList, name='microsoft-list'),
    path('microsoft/microsoft-detail/<str:pk>/',
         views.MicrosoftDetail, name='microsoft-detail'),
    path('microsoft/microsoft-create/',
         views.MicrosoftCreate, name='microsoft-create'),
    path('microsoft/microsoft-update/<str:pk>/',
         views.MicrosoftUpdate, name='microsoft-update'),
    path('microsoft/microsoft-delete/<str:pk>/',
         views.MicrosoftDelete, name='microsoft-delete'),



    path('tesla/', views.TeslaOverview, name='tesla-overview'),
    path('tesla/tesla-list', views.TeslaList, name='tesla-list'),
    path('tesla/tesla-detail/<str:pk>/',
         views.TeslaDetail, name='tesla-detail'),
    path('tesla/tesla-create/',
         views.TeslaCreate, name='tesla-create'),
    path('tesla/tesla-update/<str:pk>/',
         views.TeslaUpdate, name='tesla-update'),
    path('tesla/tesla-delete/<str:pk>/',
         views.TeslaDelete, name='tesla-delete'),





    path('apple/', views.AppleOverview, name='apple-overview'),
    path('apple/apple-list',
         views.AppleList, name='apple-list'),
    path('apple/apple-detail/<str:pk>/',
         views.AppleDetail, name='apple-detail'),
    path('apple/apple-create/',
         views.AppleCreate, name='apple-create'),
    path('apple/apple-update/<str:pk>/',
         views.AppleUpdate, name='apple-update'),
    path('apple/apple-delete/<str:pk>/',
         views.AppleDelete, name='apple-delete'),





    # Facebook
    path('facebook/', views.FacebookOverview, name='facebook-overview'),
    path('facebook/facebook-list', views.FacebookList, name='facebook-list'),
    path('facebook/facebook-detail/<str:pk>/',
         views.FacebookDetail, name='facebook-detail'),
    path('facebook/facebook-create/',
         views.FacebookCreate, name='facebook-create'),
    path('facebook/facebook-update/<str:pk>/',
         views.FacebookUpdate, name='facebook-update'),
    path('facebook/facebook-delete/<str:pk>/',
         views.FacebookDelete, name='facebook-delete'),



    # Privacy
    path('privacy/', views.PrivacyOverview, name='privacy-overview'),
    path('privacy/privacy-list', views.PrivacyList, name='privacy-list'),
    path('privacy/privacy-detail/<str:pk>/',
         views.PrivacyDetail, name='privacy-detail'),
    path('privacy/privacy-create/',
         views.PrivacyCreate, name='privacy-create'),
    path('privacy/privacy-update/<str:pk>/',
         views.PrivacyUpdate, name='privacy-update'),
    path('privacy/privacy-delete/<str:pk>/',
         views.PrivacyDelete, name='privacy-delete'),


    # Cybersecurity

    path('cybersecurity/', views.CybersecurityOverview,
         name='cybersecurity-overview'),
    path('cybersecurity/cybersecurity-list',
         views.CybersecurityList, name='cybersecurity-list'),
    path('cybersecurity/cybersecurity-detail/<str:pk>/',
         views.CybersecurityDetail, name='cybersecurity-detail'),
    path('cybersecurity/cybersecurity-create/',
         views.CybersecurityCreate, name='cybersecurity-create'),
    path('cybersecurity/cybersecurity-update/<str:pk>/',
         views.CybersecurityUpdate, name='cybersecurity-update'),
    path('cybersecurity/cybersecurity-delete/<str:pk>/',
         views.CybersecurityDelete, name='cybersecurity-delete'),





    # Netflix

    path('netflix/', views.NetflixOverview,
         name='netflix-overview'),
    path('netflix/netflix-list',
         views.NetflixList, name='netflix-list'),
    path('netflix/netflix-detail/<str:pk>/',
         views.NetflixDetail, name='netflix-detail'),
    path('netflix/netflix-create/',
         views.NetflixCreate, name='netflix-create'),
    path('netflix/netflix-update/<str:pk>/',
         views.NetflixUpdate, name='netflix-update'),
    path('netflix/netflix-delete/<str:pk>/',
         views.NetflixDelete, name='netflix-delete'),



    # Sports

    path('sports/', views.SportsOverview,
         name='sports-overview'),
    path('sports/sports-list',
         views.SportsList, name='sports-list'),
    path('sports/sports-detail/<str:pk>/',
         views.SportsDetail, name='sports-detail'),
    path('sports/sports-create/',
         views.SportsCreate, name='sports-create'),
    path('sports/sports-update/<str:pk>/',
         views.SportsUpdate, name='sports-update'),
    path('sports/sports-delete/<str:pk>/',
         views.SportsDelete, name='sports-delete'),



    # Television

    path('television/', views.TelevisionOverview,
         name='television-overview'),
    path('television/television-list',
         views.TelevisionList, name='television-list'),
    path('television/television-detail/<str:pk>/',
         views.TelevisionDetail, name='television-detail'),
    path('television/television-create/',
         views.TelevisionCreate, name='television-create'),
    path('television/television-update/<str:pk>/',
         views.TelevisionUpdate, name='sports-update'),
    path('television/television-delete/<str:pk>/',
         views.TelevisionDelete, name='television-delete'),



    # Films

    path('films/', views.FilmsOverview,
         name='films-overview'),
    path('films/films-list',
         views.FilmsList, name='films-list'),
    path('films/films-detail/<str:pk>/',
         views.FilmsDetail, name='films-detail'),
    path('films/films-create/',
         views.FilmsCreate, name='films-create'),
    path('films/films-update/<str:pk>/',
         views.FilmsUpdate, name='films-update'),
    path('films/films-delete/<str:pk>/',
         views.FilmsDelete, name='films-delete'),

    # Gaming

    path('gaming/', views.GamingOverview,
         name='gaming-overview'),
    path('gaming/gaming-list',
         views.GamingList, name='gaming-list'),
    path('gaming/gaming-detail/<str:pk>/',
         views.GamingDetail, name='gaming-detail'),
    path('gaming/gaming-create/',
         views.GamingCreate, name='gaming-create'),
    path('gaming/gaming-update/<str:pk>/',
         views.GamingUpdate, name='gaming-update'),
    path('gaming/gaming-delete/<str:pk>/',
         views.GamingDelete, name='gaming-delete'),


    # Phones

    path('phones/', views.PhonesOverview,
         name='phones-overview'),
    path('phones/phones-list',
         views.PhonesList, name='phones-list'),
    path('phones/phones-detail/<str:pk>/',
         views.PhonesDetail, name='phones-detail'),
    path('phones/phones-create/',
         views.PhonesCreate, name='phones-create'),
    path('phones/phones-update/<str:pk>/',
         views.PhonesUpdate, name='phones-update'),
    path('phones/phones-delete/<str:pk>/',
         views.PhonesDelete, name='phones-delete'),




    # Laptops

    path('laptops/', views.LaptopsOverview,
         name='laptops-overview'),
    path('laptops/laptops-list',
         views.LaptopsList, name='laptops-list'),
    path('laptops/laptops-detail/<str:pk>/',
         views.LaptopsDetail, name='laptops-detail'),
    path('laptops/laptops-create/',
         views.LaptopsCreate, name='laptops-create'),
    path('laptops/laptops-update/<str:pk>/',
         views.LaptopsUpdate, name='laptops-update'),
    path('laptops/laptops-delete/<str:pk>/',
         views.LaptopsDelete, name='laptops-delete'),




    # Cameras

    path('cameras/', views.CamerasOverview,
         name='cameras-overview'),
    path('cameras/cameras-list',
         views.CamerasList, name='cameras-list'),
    path('cameras/cameras-detail/<str:pk>/',
         views.CamerasDetail, name='cameras-detail'),
    path('cameras/cameras-create/',
         views.CamerasCreate, name='cameras-create'),
    path('cameras/cameras-update/<str:pk>/',
         views.CamerasUpdate, name='cameras-update'),
    path('cameras/cameras-delete/<str:pk>/',
         views.CamerasDelete, name='cameras-delete'),






    # Speakers

    path('speakers/', views.SpeakersOverview,
         name='speakers-overview'),
    path('speakers/speakers-list',
         views.SpeakersList, name='speakers-list'),
    path('speakers/speakers-detail/<str:pk>/',
         views.SpeakersDetail, name='speakers-detail'),
    path('speakers/speakers-create/',
         views.SpeakersCreate, name='speakers-create'),
    path('speakers/speakers-update/<str:pk>/',
         views.SpeakersUpdate, name='speakers-update'),
    path('speakers/speakers-delete/<str:pk>/',
         views.SpeakersDelete, name='speakers-delete'),





    # HeadPhones

    path('headphones/', views.HeadphonesOverview,
         name='headphones-overview'),
    path('headphones/headphones-list',
         views.HeadphonesList, name='headphones-list'),
    path('headphones/headphones-detail/<str:pk>/',
         views.HeadphonesDetail, name='headphones-detail'),
    path('headphones/headphones-create/',
         views.HeadphonesCreate, name='headphones-create'),
    path('headphones/headphones-update/<str:pk>/',
         views.HeadphonesUpdate, name='headphones-update'),
    path('headphones/headphones-delete/<str:pk>/',
         views.HeadphonesDelete, name='headphones-delete'),









    # Youtube

    path('youtube/', views.YoutubeOverview,
         name='youtube-overview'),
    path('youtube/youtube-list',
         views.YoutubeList, name='youtube-list'),
    path('youtube/youtube-detail/<str:pk>/',
         views.YoutubeDetail, name='youtube-detail'),
    path('youtube/youtube-create/',
         views.YoutubeCreate, name='youtube-create'),
    path('youtube/youtube-update/<str:pk>/',
         views.YoutubeUpdate, name='youtube-update'),
    path('youtube/youtube-delete/<str:pk>/',
         views.YoutubeDelete, name='youtube-delete'),







    # Instagram

    path('instagram/', views.InstagramOverview,
         name='instagram-overview'),
    path('instagram/instagram-list',
         views.InstagramList, name='instagram-list'),
    path('instagram/instagram-detail/<str:pk>/',
         views.InstagramDetail, name='instagram-detail'),
    path('instagram/instagram-create/',
         views.InstagramCreate, name='instagram-create'),
    path('instagram/instagram-update/<str:pk>/',
         views.InstagramUpdate, name='instagram-update'),
    path('instagram/instagram-delete/<str:pk>/',
         views.InstagramDelete, name='instagram-delete'),










    # Linkedin

    path('linkedin/', views.LinkedinOverview,
         name='linkedin-overview'),
    path('linkedin/linkedin-list',
         views.LinkedinList, name='linkedin-list'),
    path('linkedin/linkedin-detail/<str:pk>/',
         views.LinkedinDetail, name='linkedin-detail'),
    path('linkedin/linkedin-create/',
         views.LinkedinCreate, name='linkedin-create'),
    path('linkedin/linkedin-update/<str:pk>/',
         views.LinkedinUpdate, name='linkedin-update'),
    path('linkedin/linkedin-delete/<str:pk>/',
         views.LinkedinDelete, name='linkedin-delete'),





    # Twitter

    path('twitter/', views.TwitterOverview,
         name='twitter-overview'),
    path('twitter/twitter-list',
         views.TwitterList, name='twitter-list'),
    path('twitter/twitter-detail/<str:pk>/',
         views.TwitterDetail, name='twitter-detail'),
    path('twitter/twitter-create/',
         views.TwitterCreate, name='twitter-create'),
    path('twitter/twitter-update/<str:pk>/',
         views.TwitterUpdate, name='twitter-update'),
    path('twitter/twitter-delete/<str:pk>/',
         views.TwitterDelete, name='twitter-delete'),




    # Nasa

    path('nasa/', views.NasaOverview,
         name='nasa-overview'),
    path('nasa/nasa-list',
         views.NasaList, name='nasa-list'),
    path('nasa/nasa-detail/<str:pk>/',
         views.NasaDetail, name='nasa-detail'),
    path('nasa/nasa-create/',
         views.NasaCreate, name='nasa-create'),
    path('nasa/nasa-update/<str:pk>/',
         views.NasaUpdate, name='nasa-update'),
    path('nasa/nasa-delete/<str:pk>/',
         views.NasaDelete, name='nasa-delete'),







    # Spacex

    path('spacex/', views.SpacexOverview,
         name='spacex-overview'),
    path('spacex/spacex-list',
         views.SpacexList, name='spacex-list'),
    path('spacex/spacex-detail/<str:pk>/',
         views.SpacexDetail, name='spacex-detail'),
    path('spacex/spacex-create/',
         views.SpacexCreate, name='spacex-create'),
    path('spacex/spacex-update/<str:pk>/',
         views.SpacexUpdate, name='spacex-update'),
    path('spacex/spacex-delete/<str:pk>/',
         views.SpacexDelete, name='spacex-delete'),


    # Health

    path('health/', views.HealthOverview,
         name='health-overview'),
    path('health/health-list',
         views.HealthList, name='health-list'),
    path('health/health-detail/<str:pk>/',
         views.HealthDetail, name='health-detail'),
    path('health/health-create/',
         views.HealthCreate, name='health-create'),
    path('health/health-update/<str:pk>/',
         views.HealthUpdate, name='health-update'),
    path('health/health-delete/<str:pk>/',
         views.HealthDelete, name='health-delete'),



    # Energy

    path('energy/', views.EnergyOverview,
         name='energy-overview'),
    path('energy/energy-list',
         views.EnergyList, name='energy-list'),
    path('energy/energy-detail/<str:pk>/',
         views.EnergyDetail, name='energy-detail'),
    path('energy/energy-create/',
         views.EnergyCreate, name='energy-create'),
    path('energy/energy-update/<str:pk>/',
         views.EnergyUpdate, name='energy-update'),
    path('energy/energy-delete/<str:pk>/',
         views.EnergyDelete, name='energy-delete'),






    # Environment

    path('environment/', views.EnvironmentOverview,
         name='environment-overview'),
    path('environment/environment-list',
         views.EnvironmentList, name='environment-list'),
    path('environment/environment-detail/<str:pk>/',
         views.EnvironmentDetail, name='environment-detail'),
    path('environment/environment-create/',
         views.EnvironmentCreate, name='environment-create'),
    path('environment/environment-update/<str:pk>/',
         views.EnvironmentUpdate, name='environment-update'),
    path('environment/environment-delete/<str:pk>/',
         views.EnvironmentDelete, name='environment-delete'),










    path('contact/', views.ContactOverview, name='contact-overview'),
    path('contact/contact-list',
         views.ContactList, name='contact-list'),
    path('contact/contact-detail/<str:pk>/',
         views.ContactDetail, name='contact-detail'),
    path('contact/contact-create/',
         views.ContactCreate, name='contact-create'),
    path('contact/contact-delete/<str:pk>/',
         views.ContactDelete, name='contact-delete'),


]
