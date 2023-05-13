from django.db import models
from django.utils.text import slugify


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=150)
    slug = models.SlugField(unique=True, blank=True)
    image = models.ImageField()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Sneakers(models.Model):
    name = models.CharField(max_length=155)
    slug = models.SlugField(unique=True, blank=True)
    type = models.ForeignKey(Category, on_delete=models.CASCADE)
    Character = models.TextField()
    UZ = "so'm"
    RU = "rubl"
    ENG = "$"
    the_price = (
        (UZ, "so'm"),
        (RU, "rubl"),
        (ENG, "$"),
    )
    price_type = models.CharField(max_length=10,
                                  choices=the_price,
                                  default="so'm")
    price = models.IntegerField()
    image = models.ImageField()


class Buy(models.Model):
    name = models.CharField(max_length=155)
    phone = models.CharField(max_length=17)
    product = models.ForeignKey(Sneakers, on_delete=models.CASCADE, null=True)
    All_Sizes = (
        ('36', '36'),
        ('37', '37'),
        ('38', '38'),
        ('39', '39'),
        ('40', '40'),
        ('41', '41'),
        ('42', '42'),
        ('43', '43'),
        ('44', '44'),
    )
    size = models.CharField(max_length=100, choices=All_Sizes)
    All_Values = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
    )
    how = models.CharField(max_length=100, choices=All_Values)
    map = models.TextField()
    email = models.EmailField(blank=True)


