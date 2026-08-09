from django.db import migrations, models

# The 4 core service pages have hardcoded routing (services/views.py, services/urls.py)
# that used to look services up by the user-editable `slug` field — so renaming a
# service in the dashboard could silently 404 its own page. `key` is a separate,
# non-editable field that routing uses instead, so `slug`/`title` become safe to edit.
KNOWN_KEYS = ['shariah-advisory', 'academy', 'research-house', 'publication']


def backfill_key(apps, schema_editor):
    Service = apps.get_model('services', 'Service')
    for slug in KNOWN_KEYS:
        Service.objects.filter(slug=slug).update(key=slug)


def clear_key(apps, schema_editor):
    Service = apps.get_model('services', 'Service')
    Service.objects.all().update(key=None)


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='key',
            field=models.SlugField(max_length=64, unique=True, null=True, blank=True, editable=False,
                                    help_text="Internal routing identifier, fixed at creation. Not shown in the dashboard."),
        ),
        migrations.RunPython(backfill_key, clear_key),
    ]
