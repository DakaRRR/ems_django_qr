from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from io import BytesIO
from django.core.files import File
from PIL import Image
from django.core.validators import RegexValidator
from django.urls import reverse
import qrcode


class Department(models.Model):
    name = models.TextField()
    sort_id = models.IntegerField(blank=True, null=True)
    date_added = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Position(models.Model):
    name = models.TextField()
    sort_id = models.IntegerField(blank=True, null=True)
    date_added = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class StatusEmployee(models.Model):
    name = models.TextField()
    date_added = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class CustomUser(AbstractUser):
    is_hr = models.BooleanField(
        _("Кадровик"),
        default=False,
        help_text=_("Указывает, кадровик ли сотрудник."),
    )
    is_mainHR = models.BooleanField(
        _("Кадровик центрального аппарата"),
        default=False,
        help_text=_("Указывает, кадровик центрального аппарата ли сотрудник."),
    )
    department_id = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True,
                                      verbose_name="Название подразделения")

    def get_user_position(self):
        if self.is_hr:
            return "Кадровик"
        elif self.is_mainHR:
            return "Кадровик центрального аппарата"
        else:
            return "Должность не выбрана"

    def get_user_name(self):
        if self.first_name:
            return self.first_name
        else:
            return "Нет данных по имени"

    def get_user_last_name(self):
        if self.first_name:
            return self.first_name
        else:
            return "Нет данных по фамилии"

    def get_user_full_name(self):
        if self.first_name:
            return self.get_full_name()
        else:
            return "Нет данных по ФИО"

    def get_user_department_id(self):
        if self.department_id:
            return self.department_id
        else:
            return "Нет данных по подразделению"


class Employees(models.Model):
    firstname = models.TextField()
    middlename = models.TextField(blank=True, null=True)
    lastname = models.TextField()
    fullname = models.TextField(blank=True, null=True)
    profile_image = models.ImageField(blank=True, null=True, upload_to="profile_image/")
    qr_code = models.ImageField(blank=True, null=True, upload_to="qr_codes/")
    department_id = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)
    position_id = models.ForeignKey(Position, on_delete=models.SET_NULL, null=True)
    status_id = models.ForeignKey(StatusEmployee, on_delete=models.SET_NULL, null=True)
    date_added = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.firstname + ' ' + self.middlename + ' ' + self.lastname + ' '

    def generate_qr(self, *args, **kwargs):
        url = f'http://your_url/{self.id}'
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(url)
        qr.make(fit=True)

        filename = f'qr_code-{self.firstname}{self.id}.png'

        img = qr.make_image()
        buffer = BytesIO()
        img.save(buffer, 'PNG')
        self.qr_code.save(filename, File(buffer), save=False)
        super().save(*args, **kwargs)

    def get_profile_image_url(self):
        if self.profile_image:
            return self.profile_image.url

        return '/static/employee_information/assets/material-admin/images/faces/ava.jpg'

    def get_absolute_url(self):
        return f'/employee/{self.id}'

    def get_status_name(self):
        if self.status_id:
            return self.status_id

        return "Нет статуса"

    def get_status_color(self):
        if str(self.status_id) == "Работает" or str(self.status_id) == "работает":
            return 1  # green
        if str(self.status_id) == "Уволен" or str(self.status_id) == "уволен":
            return 2  # red

    def get_department_name(self):
        if self.department_id:
            return self.department_id
        return "Нет подразделения"

    def get_position_name(self):
        if self.position_id:
            return self.position_id
        return "Нет должности"
