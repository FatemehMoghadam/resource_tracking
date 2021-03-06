from django.contrib.admin import ModelAdmin, register
from django.contrib.gis.admin import GeoModelAdmin
from weather.models import WeatherStation, Location


@register(Location)
class LocationAdmin(GeoModelAdmin):
    list_display = ('pk', 'title', 'point', 'height')


@register(WeatherStation)
class WeatherStationAdmin(ModelAdmin):
    list_display = (
        'name', 'manufacturer', 'abbreviation', 'bom_abbreviation',
        'ip_address', 'last_reading', 'connect_every', 'active', 'upload_data')
    list_filter = ('manufacturer', 'active', 'upload_data')
