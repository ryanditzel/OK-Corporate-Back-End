from django.contrib import admin
from .models import Company, User, Review


class UserAdmin(admin.ModelAdmin):
    model = User


admin.site.register(Company)
admin.site.register(User, UserAdmin)
admin.site.register(Review)
