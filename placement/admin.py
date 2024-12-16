from django.contrib import admin
from .models import Company, Saved_Company, Salary, New_Job, Saved_Job


# Register your models here.
# Register your models here.
class CompanyAdmin(admin.ModelAdmin):
    list_display=['id', 'name','desc','link', 'icon_url']
    list_editable=['name','desc', 'link', 'icon_url']
admin.site.register(Company, CompanyAdmin)

class Saved_CompanyAdmin(admin.ModelAdmin):
    list_display=['id', 'company_id','user_id','last_open']
    list_editable=['company_id','user_id']
admin.site.register(Saved_Company, Saved_CompanyAdmin)

class SalaryAdmin(admin.ModelAdmin):
    list_display=['id','company_id','position', 'base','bonus','stock', 'country']
    list_editable=['base','bonus','stock']
admin.site.register(Salary, SalaryAdmin)

class New_JobAdmin(admin.ModelAdmin):
    list_display=['id','company_id','position', 'job_id', 'location', 'link', 'date_updated']
    list_editable=['position', 'job_id','location', 'link', 'date_updated']
admin.site.register(New_Job, New_JobAdmin)

class Saved_JobAdmin(admin.ModelAdmin):
    list_display=['id','job_id','user_id', 'applied','reffred','rejected', 'selected', 'apply_date']
    list_editable=['applied','reffred','rejected', 'selected']
admin.site.register(Saved_Job, Saved_JobAdmin)

