from rest_framework import serializers
from .models import Amazon, Google, Microsoft, Tesla, Trending, Hot, New, Contact, Apple, Facebook, Privacy, Cybersecurity, Netflix, Sports, Television, Films, Gaming, Phones, Laptops, Cameras, Speakers, Headphones, Youtube, Instagram, Linkedin, Twitter, Nasa, Spacex, Health, Energy, Environment


class TrendingSerializers(serializers.ModelSerializer):
    class Meta:
        model = Trending
        fields = '__all__'


class HotSerializers(serializers.ModelSerializer):
    class Meta:
        model = Hot
        fields = '__all__'


class NewSerializers(serializers.ModelSerializer):
    class Meta:
        model = New
        fields = '__all__'


class AmazonSerializers(serializers.ModelSerializer):
    class Meta:
        model = Amazon
        fields = '__all__'


class GoogleSerializers(serializers.ModelSerializer):
    class Meta:
        model = Google
        fields = '__all__'


class MicrosoftSerializers(serializers.ModelSerializer):
    class Meta:
        model = Microsoft
        fields = '__all__'


class TeslaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Tesla
        fields = '__all__'


class FacebookSerializers(serializers.ModelSerializer):
    class Meta:
        model = Facebook
        fields = '__all__'


class PrivacySerializers(serializers.ModelSerializer):
    class Meta:
        model = Privacy
        fields = '__all__'


class CybersecuritySerializers(serializers.ModelSerializer):
    class Meta:
        model = Cybersecurity
        fields = '__all__'


class AppleSerializers(serializers.ModelSerializer):
    class Meta:
        model = Apple
        fields = '__all__'


class NetflixSerializers(serializers.ModelSerializer):
    class Meta:
        model = Netflix
        fields = '__all__'


class SportsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Sports
        fields = '__all__'


class TelevisionSerializers(serializers.ModelSerializer):
    class Meta:
        model = Television
        fields = '__all__'


class FilmsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Films
        fields = '__all__'


class GamingSerializers(serializers.ModelSerializer):
    class Meta:
        model = Gaming
        fields = '__all__'


class PhonesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Phones
        fields = '__all__'


class LaptopsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Laptops
        fields = '__all__'


class CamerasSerializers(serializers.ModelSerializer):
    class Meta:
        model = Cameras
        fields = '__all__'


class SpeakersSerializers(serializers.ModelSerializer):
    class Meta:
        model = Speakers
        fields = '__all__'


class HeadphonesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Headphones
        fields = '__all__'


class YoutubeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Youtube
        fields = '__all__'


class InstagramSerializers(serializers.ModelSerializer):
    class Meta:
        model = Instagram
        fields = '__all__'


class LinkedinSerializers(serializers.ModelSerializer):
    class Meta:
        model = Linkedin
        fields = '__all__'


class TwitterSerializers(serializers.ModelSerializer):
    class Meta:
        model = Twitter
        fields = '__all__'


class NasaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Nasa
        fields = '__all__'


class SpacexSerializers(serializers.ModelSerializer):
    class Meta:
        model = Spacex
        fields = '__all__'


class HealthSerializers(serializers.ModelSerializer):
    class Meta:
        model = Health
        fields = '__all__'


class EnergySerializers(serializers.ModelSerializer):
    class Meta:
        model = Energy
        fields = '__all__'


class EnvironmentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Environment
        fields = '__all__'


class ContactSerializers(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'
