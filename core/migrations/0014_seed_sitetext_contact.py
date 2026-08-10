from django.db import migrations

ITEMS = [
    ('contact_breadcrumb_current',    'Breadcrumb current segment',     'Contact'),
    ('contact_eyebrow',               'Hero eyebrow label',             'Contact Us'),
    ('contact_get_in_touch_eyebrow',  'Contact info column eyebrow',    'Get in touch'),
    ('contact_love_to_hear_heading',  'Contact info column heading',    "We'd love to hear from you."),
    ('contact_phone_label',           'Contact info "Phone" label',     'Phone'),
    ('contact_email_label',           'Contact info "Email" label',     'Email'),
    ('contact_location_label',        'Contact info "Location" label',  'Location'),
    ('contact_hours_label',           'Contact info "Working Hours" label', 'Working Hours'),
    ('contact_success_title',         'Form success banner title',      'Message sent — thank you.'),
    ('contact_form_name_label',       'Form: Name field label',         'Full Name *'),
    ('contact_form_name_placeholder', 'Form: Name field placeholder',   'Your full name'),
    ('contact_form_email_label',      'Form: Email field label',        'Email *'),
    ('contact_form_email_placeholder','Form: Email field placeholder',  'your@email.com'),
    ('contact_form_phone_label',      'Form: Phone field label',        'Phone'),
    ('contact_form_phone_placeholder','Form: Phone field placeholder',  '+44 ...'),
    ('contact_form_subject_label',    'Form: Subject field label',      'Subject'),
    ('contact_form_subject_placeholder','Form: Subject field placeholder', 'How can we help?'),
    ('contact_form_message_label',    'Form: Message field label',      'Message *'),
    ('contact_form_message_placeholder','Form: Message field placeholder', 'Your message...'),
    ('contact_form_submit_button',    'Form: Submit button',            'Send Message'),
]


def seed(apps, schema_editor):
    SiteText = apps.get_model('core', 'SiteText')
    for i, (key, label, default_value) in enumerate(ITEMS):
        SiteText.objects.get_or_create(key=key, defaults={
            'group': 'contact', 'label': label, 'value': default_value, 'order': i,
        })


def unseed(apps, schema_editor):
    SiteText = apps.get_model('core', 'SiteText')
    SiteText.objects.filter(key__in=[k for k, _, _ in ITEMS]).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_seed_sitetext_publication'),
    ]

    operations = [
        migrations.RunPython(seed, unseed),
    ]
