# Generated by Django 3.0.2 on 2020-02-08 11:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('olaniyiolabode99scrumy', '0002_auto_20200114_1837'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goalstatus',
            name='status_name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='scrumygoals',
            name='created_by',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='scrumygoals',
            name='goal_id',
            field=models.IntegerField(default=30),
        ),
        migrations.AlterField(
            model_name='scrumygoals',
            name='goal_name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='scrumygoals',
            name='goal_status',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='olaniyiolabode99scrumy.GoalStatus'),
        ),
        migrations.AlterField(
            model_name='scrumygoals',
            name='moved_by',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='scrumygoals',
            name='owner',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='scrumygoals',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='scrumyhistory',
            name='created_by',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='scrumyhistory',
            name='goal',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='olaniyiolabode99scrumy.ScrumyGoals'),
        ),
        migrations.AlterField(
            model_name='scrumyhistory',
            name='moved_by',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='scrumyhistory',
            name='moved_from',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='scrumyhistory',
            name='moved_to',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='scrumyhistory',
            name='time_of_action',
            field=models.DateTimeField(),
        ),
    ]
