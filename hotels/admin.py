from django.contrib import admin
from .models import *
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "parent", "slug", "code")
    search_fields = ("name", "code")

admin.site.register(Category, CategoryAdmin)


class HotelImageInline(admin.TabularInline):
    model = HotelGallery
    extra = 1


class HotelAdmin(admin.ModelAdmin):
    inlines = (HotelImageInline, )


class RoomImageInline(admin.TabularInline):
    model = RoomGallery
    extra = 1


class RoomAdmin(admin.ModelAdmin):
    inlines = (RoomImageInline, )


admin.site.register(Hotel, HotelAdmin)
admin.site.register(Room, RoomAdmin)
admin.site.register(HotelGallery)
admin.site.register(RoomGallery)
