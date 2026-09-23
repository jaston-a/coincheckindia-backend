from django.db import models

class Category(models.Model):
    ITEM_TYPES = (
        ('coin', 'Coin'),
        ('note', 'BankNote'),
    )
    name = models.CharField(max_length=50) # e.g., "1 Rupee", "5 Paisa", "786 Notes"
    slug = models.SlugField(unique=True)
    item_type = models.CharField(max_length=10, choices=ITEM_TYPES, default='coin')

    def __str__(self):
        return f"{self.name} ({self.get_item_type_display()})"


class CoinOrNoteVariant(models.Model):
    RARITY_CHOICES = (
        ('Common', 'Common'),
        ('Scarce', 'Scarce'),
        ('Rare', 'Rare'),
        ('Extremely Rare', 'Extremely Rare'),
    )

    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='variants')
    title = models.CharField(max_length=100) # e.g., "1985 Noida Mint 1 Rupee" or "786 Series ₹10 Note"
    year = models.IntegerField(null=True, blank=True)
    mint_mark = models.CharField(max_length=100, help_text="e.g., Mumbai (Diamond), Noida (Dot), Calcutta (No Mark)")
    rarity = models.CharField(max_length=20, choices=RARITY_CHOICES, default='Rare')
    estimated_value = models.CharField(max_length=50, help_text="e.g., ₹500 - ₹2,000")
    
    front_image = models.ImageField(upload_to='coins/front/', null=True, blank=True)
    back_image = models.ImageField(upload_to='coins/back/', null=True, blank=True)
    
    description = models.TextField(help_text="Detailed info on where to check the mint mark / unique features.")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title