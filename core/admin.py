from django.contrib import admin
from .models import Gallery, Photo, Category


class DateCreatedAdmin(admin.ModelAdmin):
    readonly_fields = (
        "created",
        "updated",
    )


class GalleryAdmin(DateCreatedAdmin):
    list_display = ["name", "user", "public"]


admin.site.register(Category)
admin.site.register(Gallery, GalleryAdmin)
admin.site.register(Photo, DateCreatedAdmin)
