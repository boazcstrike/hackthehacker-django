# import geoip2.database

from django.shortcuts import render
from rest_framework import status, generics, viewsets, serializers
from rest_framework.response import Response

from .models import *

class HackSerializer(serializers.Serializer):
    message = serializers.CharField(required=False)


class Hack(generics.GenericAPIView):
    queryset = HackerInfo.objects.all()
    serializer_class = HackSerializer

    def get(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')

        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        try:
            response = reader.city(str(ip))
            reader = geoip2.database.Reader('./GeoLite2-City_20190430/GeoLite2-City.mmdb')

            print(response.country.iso_code)
            print(response.country.name)
            print(response.country.names['zh-CN'])
            print(response.subdivisions.most_specific.name)
            print(response.subdivisions.most_specific.iso_code)
            print(response.city.name)
            print(response.postal.code)
            print(response.location.latitude)
            print(response.location.longitude)

            hi = HackerInfo.objects.create(
                ip = str(ip),
                country_iso=response.country.iso_code,
                country=response.country.name,
                subdivisions=response.subdivisions.most_specific.name,
                subdivisions_iso=response.subdivisions.most_specific.iso_code,
                city=response.city.name,
                postal=response.postal.code,
                lng=response.location.latitude,
                lat=response.location.longitude,
            )
        except:
            hi = HackerInfo.objects.create(
                ip = str(ip),
            )
        hi.save()
        print('hacker saved')

        return Response({
            'message': 'hacking is bad'
            }, status=status.HTTP_400_BAD_REQUEST)
