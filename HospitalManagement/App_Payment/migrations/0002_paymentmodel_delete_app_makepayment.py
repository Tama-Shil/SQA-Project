# Generated by Django 5.0.2 on 2024-02-11 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_Payment', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patientId', models.CharField(default='', max_length=10)),
                ('totalAmount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('timeStamp', models.DateTimeField(auto_now_add=True, verbose_name='Timestamp')),
            ],
        ),
        migrations.DeleteModel(
            name='app_MakePayment',
        ),
    ]
