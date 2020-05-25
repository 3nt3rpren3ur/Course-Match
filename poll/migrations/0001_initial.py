# Generated by Django 3.0.5 on 2020-05-24 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Poll',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
                ('option_one', models.CharField(max_length=30)),
                ('option_two', models.CharField(max_length=30)),
                ('option_three', models.CharField(max_length=30)),
                ('option_four', models.CharField(max_length=30)),
                ('option_five', models.CharField(max_length=30)),
                ('option_six', models.CharField(max_length=30)),
                ('option_seven', models.CharField(max_length=30)),
                ('option_eight', models.CharField(max_length=30)),
                ('option_nine', models.CharField(max_length=30)),
                ('option_ten', models.CharField(max_length=30)),
                ('option_one_count', models.IntegerField(default=0)),
                ('option_two_count', models.IntegerField(default=0)),
                ('option_three_count', models.IntegerField(default=0)),
                ('option_four_count', models.IntegerField(default=0)),
                ('option_five_count', models.IntegerField(default=0)),
                ('option_six_count', models.IntegerField(default=0)),
                ('option_seven_count', models.IntegerField(default=0)),
                ('option_eight_count', models.IntegerField(default=0)),
                ('option_nine_count', models.IntegerField(default=0)),
                ('option_ten_count', models.IntegerField(default=0)),
            ],
        ),
    ]
