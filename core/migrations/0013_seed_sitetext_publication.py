from django.db import migrations

ITEMS = [
    ('publication_eyebrow',             'Hero eyebrow label',              'Publications'),
    ('publication_breadcrumb_current',  'Breadcrumb current segment',      'Publication'),
    ('publication_all_filter',          '"All" filter chip',               'All'),
    ('publication_pdf_button',          'Publication card PDF button',     'PDF'),
    ('publication_read_more_button',    'Publication card link button',    'Read More'),
    ('publication_coming_soon_tag',     'No-file tag on a publication',    'Coming Soon'),
    ('publication_empty_title',         'No publications empty-state title','Publications coming soon'),
    ('publication_empty_body',          'No publications empty-state text', "Our editorial team is preparing the first publications. Register your interest to be notified on release."),
    ('publication_empty_button',        'No publications empty-state button','Stay informed'),
    ('publication_research_house_cta',  'CTA secondary button',            'Research House'),
]


def seed(apps, schema_editor):
    SiteText = apps.get_model('core', 'SiteText')
    for i, (key, label, default_value) in enumerate(ITEMS):
        SiteText.objects.get_or_create(key=key, defaults={
            'group': 'publication', 'label': label, 'value': default_value, 'order': i,
        })


def unseed(apps, schema_editor):
    SiteText = apps.get_model('core', 'SiteText')
    SiteText.objects.filter(key__in=[k for k, _, _ in ITEMS]).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_seed_sitetext_shariah'),
    ]

    operations = [
        migrations.RunPython(seed, unseed),
    ]
