# Generated by Django 4.1.7 on 2023-03-01 08:58

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("issue_tracker", "0003_auto_20230301_0825"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="issue",
            name="type_old",
        ),
        migrations.AddField(
            model_name="issue",
            name="type",
            field=models.ManyToManyField(
                blank=True, related_name="issues", to="issue_tracker.type"
            ),
        ),
    ]
