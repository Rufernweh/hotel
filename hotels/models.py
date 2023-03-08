from django.db import models
from ckeditor.fields import RichTextField
from services.choices import STATUS
from services.generator import CodeGenerator
from services.mixin import DateMixin,SlugMixin
from services.slugify import slugify
from services.uploader import Uploader
from mptt.models import TreeForeignKey,MPTTModel
from django.contrib.auth import get_user_model



# Create your models here.
class Category(DateMixin, SlugMixin, MPTTModel):
    name = models.CharField(max_length=300)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ("-created_at", )
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def save(self, *args, **kwargs):
        self.code = CodeGenerator.create_slug_shortcode(
            size=20, model_=Category
        )
        self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

class Hotel(DateMixin,SlugMixin):
    name = models.CharField(max_length=120,blank=True,null=True)
    adress = RichTextField(blank=True,null=True)
    city = models.CharField(max_length=150,blank=True,null=True)
    country = models.CharField(max_length=150,blank=True,null=True)

    class Meta:
        ordering=['-created_at']
        verbose_name='Hotel'
        verbose_name_plural='Hotels'
    
    def __str__(self) -> str:
        return self.name
    
    def save(self, *args, **kwargs):
        self.code = CodeGenerator.create_slug_shortcode(
            size=20, model_=Hotel
        )
        self.slug = slugify(self.name)
        return super().save(*args, **kwargs)
    
class Room(DateMixin,SlugMixin):
    name=models.CharField(max_length=150,blank=True,null=True)
    room_no=models.PositiveIntegerField(blank=True,null=True)
    types=models.CharField(choices=STATUS,max_length=150)
    hotel=models.ForeignKey(Hotel,on_delete=models.CASCADE)
    price=models.PositiveIntegerField()
    benefits=RichTextField()
    descrtiption = RichTextField()

    def __str__(self) -> str:
        return f'{self.types} --> {self.name}|No{self.room_no}'
    
    class Meta:
        ordering=['-created_at']
        verbose_name='Room'
        verbose_name_plural='Rooms'

    def save(self, *args, **kwargs):
        self.code = CodeGenerator.create_slug_shortcode(
            size=20, model_=Room
        )
        self.slug = slugify(self.name)
        return super().save(*args, **kwargs)
    

class HotelGallery(DateMixin):
    hotel=models.ForeignKey(Hotel,on_delete=models.CASCADE)
    image=models.ImageField(upload_to=Uploader.upload_image_Hotel)


    def __str__(self) -> str:
        return self.hotel.name

    class Meta:
        ordering=['-created_at']
        verbose_name='HotelGallery'
        verbose_name_plural='HotelGalleries'


class RoomGallery(DateMixin):
    room=models.ForeignKey(Room,on_delete=models.CASCADE)
    image=models.ImageField(upload_to=Uploader.upload_image_room)


    def __str__(self) -> str:
        return self.room.types

    class Meta:
        ordering=['-created_at']
        verbose_name='RoomGallery'
        verbose_name_plural='RoomGalleries'


class Reservation(SlugMixin,DateMixin):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    guest_name = models.CharField(max_length=255)
    guest_email = models.EmailField()


    def __str__(self) -> str:
        return self.room.name

    class Meta:
        ordering=['-created_at']
        verbose_name='Reservation'
        verbose_name_plural='Reservations'