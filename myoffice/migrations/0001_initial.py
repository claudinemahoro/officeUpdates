# Generated by Django 3.1.6 on 2021-02-11 03:49

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department_name', models.CharField(max_length=30)),
                ('department_unit', models.CharField(max_length=30)),
                ('director_pic', models.ImageField(blank=True, upload_to='')),
                ('employees_count', models.IntegerField(null=True)),
                ('office_contact', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('director_contact', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='auth.user')),
                ('email', models.EmailField(max_length=254)),
                ('profile_pic', models.ImageField(upload_to='')),
                ('bio', tinymce.models.HTMLField()),
                ('department', models.ManyToManyField(to='myoffice.Department')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('title', models.CharField(max_length=30)),
                ('description', tinymce.models.HTMLField(max_length=70)),
                ('post_user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='auth.user')),
                ('post_date', models.DateTimeField(auto_now_add=True)),
                ('post_department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='myoffice.department')),
            ],
        ),
    ]
