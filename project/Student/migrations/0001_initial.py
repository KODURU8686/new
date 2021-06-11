# Generated by Django 3.0 on 2021-06-10 14:46

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceBox',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=50)),
                ('change_role', models.CharField(max_length=1000)),
                ('impf', models.ImageField(default='ngo1.jpg', upload_to='Medicines/')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('img', models.ImageField(default='profile.png', upload_to='Profiles/')),
                ('dob', models.DateField(blank=True, null=True)),
                ('organization_name', models.CharField(blank=True, max_length=120, null=True)),
                ('hospital_name', models.CharField(blank=True, max_length=120, null=True)),
                ('gender', models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female')], max_length=10, null=True)),
                ('ph_no', models.CharField(max_length=10)),
                ('pan_no', models.CharField(blank=True, max_length=10, null=True)),
                ('address', models.CharField(max_length=100)),
                ('postal_code', models.CharField(max_length=7)),
                ('city', models.CharField(max_length=20)),
                ('state', models.CharField(default='Andra Pradesh', max_length=20)),
                ('country', models.CharField(default='India', max_length=20)),
                ('role', models.IntegerField(choices=[(1, 'Medicinist'), (2, 'Organisation'), (3, 'Guest')], default=3)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Rolrq',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uname', models.CharField(max_length=50)),
                ('roltype', models.IntegerField(choices=[(1, 'Medicinist'), (2, 'Organisation')], default=0)),
                ('prf', models.ImageField(upload_to='RolesRequested/')),
                ('is_checked', models.BooleanField(default=0)),
                ('ud', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Orgdetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('org_name', models.CharField(default='Organisation Name', max_length=50)),
                ('found_name', models.CharField(default='Founder Name', max_length=50)),
                ('est_date', models.DateField(null=True)),
                ('us', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('org_name', models.CharField(max_length=200)),
                ('orglicense_no', models.CharField(max_length=20)),
                ('required_tablets', models.CharField(max_length=20, null=True)),
                ('oid', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='MedicineInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pharmacy_name', models.CharField(max_length=200, null=True)),
                ('phrlicense_no', models.CharField(max_length=20, null=True)),
                ('medicine_name', models.CharField(max_length=120)),
                ('category', models.CharField(choices=[('Tablet', 'Tablet'), ('Syrup', 'Syrup'), ('Injection', 'Injection')], default='Tablet', max_length=20)),
                ('dosage', models.CharField(max_length=20)),
                ('days_count', models.CharField(blank=True, max_length=20)),
                ('production_date', models.DateField(null=True)),
                ('email', models.TextField(default='xyz', max_length=122)),
                ('entry_date', models.DateField(null=True)),
                ('expiry_date', models.DateField(null=True)),
                ('created_date', models.DateField(auto_now=True)),
                ('quantity', models.CharField(max_length=20, null=True)),
                ('remaining_tablets', models.CharField(max_length=20, null=True)),
                ('accepted_by', models.TextField(max_length=12)),
                ('uid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Export',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_medicinist', models.BooleanField(default=False)),
                ('u', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Donate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('donated_quantity', models.CharField(max_length=20)),
                ('pomid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Student.MedicineInfo')),
            ],
        ),
    ]
