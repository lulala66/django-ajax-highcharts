from django.contrib import admin

from import_export import resources
from import_export.admin import ImportExportActionModelAdmin

from .models import Passenger


class PassengerResource(resources.ModelResource):

    class Meta:
        model = Passenger


@admin.register(Passenger)
class PassengerAdmin(ImportExportActionModelAdmin):
    pass
