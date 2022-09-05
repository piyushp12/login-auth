# Generated by Django 4.0.6 on 2022-09-01 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_alter_signup_address_alter_signup_confirm_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('phone_number', models.CharField(max_length=10, unique=True, verbose_name='Phone Number')),
                ('full_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Full Name')),
                ('email', models.EmailField(blank=True, max_length=255, null=True, verbose_name='Email')),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='Profile/%Y/%m/%d/', verbose_name='Avatar')),
                ('address', models.TextField(blank=True, null=True, verbose_name='Address')),
                ('otp', models.CharField(blank=True, max_length=4, null=True, verbose_name='OTP')),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('otp_verify', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False, verbose_name='Super User')),
            ],
            options={
                'verbose_name_plural': 'My User',
            },
        ),
    ]
