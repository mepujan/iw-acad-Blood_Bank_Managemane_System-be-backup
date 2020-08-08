# Generated by Django 3.1 on 2020-08-08 15:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('bank_hospital', '0001_initial'),
        ('blood', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='discussion',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='collectedblood',
            name='collected_from_campaign',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='blood.campaign'),
        ),
        migrations.AddField(
            model_name='campaign',
            name='blood_bank',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bank_hospital.bloodbankbranch'),
        ),
        migrations.AddField(
            model_name='campaign',
            name='sponsor',
            field=models.ManyToManyField(to='blood.Sponsor'),
        ),
        migrations.AddField(
            model_name='bloodrequest',
            name='blood_type_requested',
            field=models.ManyToManyField(to='blood.BloodType'),
        ),
        migrations.AddField(
            model_name='bloodrequest',
            name='request_from',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='bank_hospital.hospital'),
        ),
        migrations.AddField(
            model_name='bloodrequest',
            name='request_to',
            field=models.ManyToManyField(to='bank_hospital.BloodBankBranch'),
        ),
        migrations.AddField(
            model_name='bloodpacket',
            name='blood_bank',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bank_hospital.bloodbankbranch'),
        ),
        migrations.AddField(
            model_name='bloodpacket',
            name='blood_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='blood.bloodtype'),
        ),
        migrations.AddField(
            model_name='bloodpacket',
            name='campaign',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='blood.campaign'),
        ),
    ]
