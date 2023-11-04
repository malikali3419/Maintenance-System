# Generated by Django 4.2.6 on 2023-11-01 20:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Andrede',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('andrede_name', models.CharField(blank=True, default=None, max_length=155, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Land',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('land_name', models.CharField(blank=True, default=None, max_length=155, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Stadt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('stadt_name', models.CharField(blank=True, default=None, max_length=155, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Records',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, default=None, max_length=155, null=True)),
                ('last_name', models.CharField(blank=True, default=None, max_length=155, null=True)),
                ('company_name', models.CharField(blank=True, default=None, max_length=155, null=True)),
                ('email', models.EmailField(blank=True, default=None, max_length=254, null=True)),
                ('news_accept', models.BooleanField(default=False)),
                ('telefone', models.CharField(blank=True, default=None, max_length=20, null=True)),
                ('starBe', models.TextField(blank=True, default=None, null=True)),
                ('nr', models.CharField(blank=True, default=None, max_length=155)),
                ('postal_code', models.CharField(blank=True, max_length=50, null=True)),
                ('birthdate', models.DateField(blank=True, default=None, null=True)),
                ('uid_number', models.CharField(blank=True, max_length=55, null=True)),
                ('ammerkung', models.TextField(blank=True, default=None, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('andrede_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='record_andred_name', to='maintenance.andrede')),
                ('land_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='record_city_name', to='maintenance.land')),
                ('stadt_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='record_stadt_name', to='maintenance.stadt')),
            ],
        ),
    ]
