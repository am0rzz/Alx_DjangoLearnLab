from django.contrib.auth.base_user import BaseUserManager

class CustomUserManager(BaseUserManager):
    def create_user(self, date_of_birth, photo, password=None, **extra_fields):
        if not date_of_birth:
            raise ValueError('Users must have a date of birth')
        user = self.model(date_of_birth=date_of_birth, profile_photo=photo, **extra_fields)
        user.set_password(password)
        return user

    def create_superuser(self, date_of_birth, photo, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(date_of_birth, photo, password, **extra_fields)


