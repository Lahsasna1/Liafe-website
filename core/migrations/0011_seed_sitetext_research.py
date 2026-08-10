from django.db import migrations

ITEMS = [
    ('research_eyebrow',              'Hero eyebrow / breadcrumb current segment', 'Research House'),
    ('research_values_empty_title',   'Research values empty state',               'Research values coming soon'),
    ('research_areas_eyebrow',        'Research Areas eyebrow',                    'Research Areas'),
    ('research_disciplines_heading',  'Research Areas heading',                    'Three disciplines. One integrated approach.'),
    ('research_featured_eyebrow',     'Featured Research eyebrow',                 'Featured Research'),
    ('research_insight_heading',      'Featured Research heading',                 'Insight that shapes practice.'),
    ('research_partner_label',        'Project card "Partner:" label',             'Partner:'),
    ('research_read_more_button',     'Project card button',                       'Read More'),
    ('research_enquiry_eyebrow',      'Enquiry form eyebrow',                      'Research Enquiry'),
    ('research_commission_heading',   'Enquiry form heading',                      'Commission research or explore collaboration.'),
    ('research_commission_body',      'Enquiry form intro text',                   "Whether you need a bespoke research report, a policy brief, or a long-term partnership, our team is ready to scope your requirements."),
    ('research_email_label',          'Contact info "Email" label',                'Email'),
    ('research_phone_label',          'Contact info "Phone" label',                'Phone'),
    ('research_success_message',      'Form success banner text',                  "Request sent — we'll be in touch shortly."),
    ('research_form_name_label',      'Form: Name field label',                    'Full Name *'),
    ('research_form_name_placeholder','Form: Name field placeholder',              'Your full name'),
    ('research_form_email_label',     'Form: Email field label',                   'Email *'),
    ('research_form_email_placeholder','Form: Email field placeholder',            'your@email.com'),
    ('research_form_phone_label',     'Form: Phone field label',                   'Phone'),
    ('research_form_phone_placeholder','Form: Phone field placeholder',            '+44 ...'),
    ('research_form_org_label',       'Form: Organisation field label',            'Organisation'),
    ('research_form_org_placeholder', 'Form: Organisation field placeholder',      'Company / Institution'),
    ('research_form_subject_label',   'Form: Topic field label',                   'Research Topic'),
    ('research_form_subject_placeholder','Form: Topic field placeholder',          'Research area or question'),
    ('research_form_message_label',   'Form: Message field label',                 'Description *'),
    ('research_form_message_placeholder','Form: Message field placeholder',        'Describe your research needs...'),
    ('research_form_submit_button',   'Form: Submit button',                       'Send Request'),
]


def seed(apps, schema_editor):
    SiteText = apps.get_model('core', 'SiteText')
    for i, (key, label, default_value) in enumerate(ITEMS):
        SiteText.objects.get_or_create(key=key, defaults={
            'group': 'research', 'label': label, 'value': default_value, 'order': i,
        })


def unseed(apps, schema_editor):
    SiteText = apps.get_model('core', 'SiteText')
    SiteText.objects.filter(key__in=[k for k, _, _ in ITEMS]).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_seed_sitetext_academy'),
    ]

    operations = [
        migrations.RunPython(seed, unseed),
    ]
