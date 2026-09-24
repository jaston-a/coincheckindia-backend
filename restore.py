import json
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from api.models import Category, CoinOrNoteVariant

with open('backup.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for cat in data:
    c, _ = Category.objects.get_or_create(
        id=cat['id'],
        defaults={
            'name': cat['name'],
            'slug': cat.get('slug', ''),
            'item_type': cat.get('item_type', 'coin')
        }
    )
    for v in cat.get('variants', []):
        CoinOrNoteVariant.objects.get_or_create(
            id=v['id'],
            defaults={
                'category': c,
                'title': v['title'],
                'year': v.get('year'),
                'mint_mark': v.get('mint_mark', ''),
                'rarity': v.get('rarity', ''),
                'estimated_value': v.get('estimated_value', ''),
                'front_image': v.get('front_image', ''),
                'back_image': v.get('back_image', ''),
                'description': v.get('description', '')
            }
        )

print("🎉 Data PostgreSQL-ku Success-ah Restored!")
