from django.contrib import admin
from api.models import Company, Employee


# Register your models here.

class CompanyAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Company._meta.fields]
    search_fields = ['name']


class EmployeeAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Employee._meta.fields]
    list_filter = ['position','company']


admin.site.register(Company, CompanyAdmin)
admin.site.register(Employee, EmployeeAdmin)
