# Generated by Django 3.1 on 2020-08-08 15:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BloodBankBranch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blood_bank_name', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone_number', models.CharField(max_length=12)),
                ('registered_date', models.DateField()),
            ],
            options={
                'verbose_name_plural': 'BloodBankBranches',
            },
        ),
        migrations.CreateModel(
            name='CenteralBloodBank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blood_bank_name', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone_number', models.CharField(max_length=12)),
                ('registered_date', models.DateField()),
                ('pan_number', models.CharField(max_length=30, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hospital_name', models.CharField(max_length=100)),
                ('hospital_location', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone_number', models.CharField(max_length=12)),
                ('pan_number', models.CharField(max_length=30, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='HospitalSocialMediaUrl',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('facebook_url', models.URLField(null=True, unique=True)),
                ('instagram_url', models.URLField(null=True, unique=True)),
                ('youtube_url', models.URLField(null=True, unique=True)),
                ('blood_bank', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='bank_hospital.hospital')),
            ],
        ),
        migrations.CreateModel(
            name='BloodBankSocialMediaUrl',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('facebook_url', models.URLField(null=True, unique=True)),
                ('instagram_url', models.URLField(null=True, unique=True)),
                ('youtube_url', models.URLField(null=True, unique=True)),
                ('blood_bank', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='bank_hospital.bloodbankbranch')),
            ],
        ),
        migrations.AddField(
            model_name='bloodbankbranch',
            name='main_branch',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bank_hospital.centeralbloodbank'),
        ),
    ]
