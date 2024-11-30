from django.db import migrations

def add_default_categories(apps, schema_editor):
    Categorys = apps.get_model('Thread', 'Categorys')
    categories = [
        ("General Discussion", "A place for general topics."),
        ("Astrophotography", "Discuss astrophotography techniques and share images."),
        ("Telescopes", "Talk about telescope models, usage, and advice."),
        ("Tavern", "Off-topic discussions and casual chats."),
    ]
    for name, description in categories:
        Categorys.objects.create(name=name, description=description)

class Migration(migrations.Migration):
    dependencies = [
        ('forum', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(add_default_categories),
    ]
