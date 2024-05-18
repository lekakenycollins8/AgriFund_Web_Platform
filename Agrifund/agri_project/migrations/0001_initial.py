# Generated by Django 5.0.6 on 2024-05-18 10:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('recipient', models.EmailField(help_text="Farmer's email", max_length=254)),
                ('message', models.TextField(help_text='notification message')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(help_text='The name of agribusiness project', max_length=50)),
                ('description', models.TextField(help_text='project description')),
                ('funding_goal', models.DecimalField(decimal_places=2, help_text='funding needed', max_digits=10)),
                ('current_status', models.CharField(default='Open', help_text='Open, Closed, Onhold', max_length=50)),
                ('farmer_name', models.CharField(help_text='Your names', max_length=100)),
                ('farmer_email', models.EmailField(help_text="Farmer's Email", max_length=254)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='LoanApplication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('amount_requested', models.DecimalField(decimal_places=2, help_text='Loan amount', max_digits=10)),
                ('supporting_docs', models.FileField(help_text='Legal documents needed', upload_to='documents/')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agri_project.project')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='InvestorInterest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('investor_fname', models.CharField(help_text="Investor's first name", max_length=50)),
                ('investor_lname', models.CharField(help_text="Investor's last name", max_length=50)),
                ('investor_email', models.EmailField(help_text='investor email', max_length=254)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agri_project.project')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
