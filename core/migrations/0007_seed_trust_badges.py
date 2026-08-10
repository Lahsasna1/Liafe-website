from django.db import migrations

BADGES = ['AAOIFI Aligned', 'IFSB Standards', 'CIBAFI Capacity Building', 'IsDB Affiliation']
TRUST_STRIP_LABEL = 'Trusted across UK · MENA · Asia'


def seed(apps, schema_editor):
    TrustBadge = apps.get_model('core', 'TrustBadge')
    HomepageSection = apps.get_model('core', 'HomepageSection')
    for i, title in enumerate(BADGES):
        TrustBadge.objects.get_or_create(title=title, defaults={'order': i, 'is_active': True})
    HomepageSection.objects.get_or_create(
        section_name='trust_strip',
        defaults={'title': TRUST_STRIP_LABEL, 'is_active': True, 'order': 99},
    )


def unseed(apps, schema_editor):
    TrustBadge = apps.get_model('core', 'TrustBadge')
    HomepageSection = apps.get_model('core', 'HomepageSection')
    TrustBadge.objects.filter(title__in=BADGES).delete()
    HomepageSection.objects.filter(section_name='trust_strip').delete()


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_trustbadge'),
    ]

    operations = [
        migrations.RunPython(seed, unseed),
    ]
