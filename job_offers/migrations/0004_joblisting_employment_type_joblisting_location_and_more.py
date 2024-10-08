# Generated by Django 5.0.6 on 2024-09-23 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job_offers', '0003_alter_category_options_remove_joblisting_offered_pay_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='joblisting',
            name='employment_type',
            field=models.CharField(choices=[('FT', 'Full-time'), ('PT', 'Part-time')], default='FT', max_length=2),
        ),
        migrations.AddField(
            model_name='joblisting',
            name='location',
            field=models.CharField(max_length=511, null=True),
        ),
        migrations.AddField(
            model_name='joblisting',
            name='work_model',
            field=models.CharField(choices=[('OS', 'On-Site'), ('HB', 'Hybrid'), ('RM', 'Remote')], default='OS', max_length=2),
        ),
    ]
