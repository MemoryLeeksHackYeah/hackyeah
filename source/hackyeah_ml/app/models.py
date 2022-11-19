from django.db import models


class RemoteHub(models.Model):
    id = models.IntegerField(primary_key=True)
    disposal_service_company_ID = models.IntegerField() # Change later to foreign key
    location_longitude = models.FloatField()
    location_latitude = models.FloatField()
    address_string_1 = models.CharField(max_length=100)
    address_string_2 = models.CharField(max_length=100)
    ip_address = models.CharField(max_length=20)
    description = models.CharField(max_length=500)

class WasteType(models.Model):
    id = models.IntegerField(primary_key=True)
    description = models.CharField(max_length=100)
    max_wait_time_days = models.IntegerField()
    average_weight_per_liter = models.FloatField()

class Container(models.Model):
    id = models.IntegerField(primary_key=True)
    remote_hub_id = models.ForeignKey(WasteType, on_delete=models.CASCADE, related_name='remote_hub_id_c')
    waste_type_id = models.ForeignKey(WasteType, on_delete=models.CASCADE, related_name='waste_type_id_c')
    capacity = models.FloatField()

class WasteTypeReadiness(models.Model):
    remote_hub_id = models.ForeignKey(RemoteHub, on_delete=models.CASCADE, related_name='remote_hub_id_wtr')
    waste_type_id = models.ForeignKey(WasteType, on_delete=models.CASCADE, related_name='waste_type_id_wtr')
    ready_to_be_thrown = models.BooleanField(default=False)

class DisposalServiceCompanies(models.Model):
    id = models.IntegerField(primary_key=True)
    company_name = models.CharField(max_length=225)
    contact = models.CharField(max_length=225)

class Trucks(models.Model):
    id = models.IntegerField(primary_key=True)
    disposal_service_company_id = models.ForeignKey(DisposalServiceCompanies, on_delete=models.CASCADE)
    availability = models.BooleanField(default=False)
    registration_number = models.CharField(max_length=10)
