# Generated by Django 4.0.2 on 2022-02-07 13:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Experiance', models.TextField(null=True)),
                ('DateOfBirth', models.DateField()),
                ('ProfilePick', models.ImageField(blank=True, upload_to='profile_pics')),
                ('Gender', models.CharField(choices=[('M', 'F')], max_length=2)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]