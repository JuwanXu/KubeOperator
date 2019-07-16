# Generated by Django 2.1.2 on 2019-06-21 07:45

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('kubeops_api', '0001_initial'),
    ]

    def forwards_func(apps, schema_editor):
        Setting = apps.get_model("kubeops_api", "Setting")
        db_alias = schema_editor.connection.alias
        Setting.objects.using(db_alias).bulk_create([
            Setting(name="主机名", key="local_hostname", order=0, value="", helper="eg:192.168.1.1"),
        ])
        Setting.objects.using(db_alias).bulk_create([
            Setting(name="域名后缀", key="domain_suffix", order=1, value="mydomain.com", helper="eg:mydomain.com"),
        ])

    def reverse_func(apps, schema_editor):
        Setting = apps.get_model("kubeops_api", "Setting")
        db_alias = schema_editor.connection.alias
        Setting.objects.using(db_alias).filter(key='local_hostname').delete()
        Setting.objects.using(db_alias).filter(key='domain_suffix').delete()

    operations = [
        migrations.RunPython(forwards_func, reverse_func),
    ]