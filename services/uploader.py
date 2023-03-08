class Uploader:

    @staticmethod
    def upload_image_Hotel(instance, filename):
        return f"hotels/{instance.hotel.slug}/{filename}"


    @staticmethod
    def upload_image_room(instance, filename):
        return f"rooms/{instance.room.slug}/{filename}"