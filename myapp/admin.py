from django.contrib import admin
from .models import StudentRegistration, Language, StudentFees, FeesAmount


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ('code', 'name')


@admin.register(FeesAmount)
class FeesAmointAdmin(admin.ModelAdmin):
    list_display = ('fees_Amount',)


@admin.register(StudentFees)
class StudentFeesAdmin(admin.ModelAdmin):
    list_display = ('mobile_number','fees','is_paid')


@admin.register(StudentRegistration)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = (
        'first_name', 'middle_name', 'last_name', 'gender', 
        'email', 'mobile_number', 'address', 'address2', 
        'city', 'state', 'zip_code', 'passport_photo', 
        'signature', 'get_languages'
    )

    def get_languages(self, obj):
        return ", ".join([lang.name for lang in obj.languages.all()])
    get_languages.short_description = 'Languages'



