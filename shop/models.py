from django.db import models
from conf.models import BaseModel
from django.shortcuts import reverse

class Category(BaseModel):
    title = models.CharField(max_length=50, db_index=True)
    description = models.TextField(blank=True)
    slug = models.SlugField(max_length=50, unique=True, allow_unicode=True)

    class Meta:
        db_table = "categoris"
        ordering = ("title", )
        verbose_name = "카테고리"
        verbose_name_plural = "카테고리 목록"

    def __str__(self):
        return "[카테고리]"+self.title

    def get_absolute_url(self):
        pass

class Product(BaseModel):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name="products")
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True, allow_unicode=True)
    image = models.ImageField(upload_to = "products/%Y-%m-%d", blank=True)
    desription = models.TextField(blank=True)
    meta_desription = models.TextField(blank=True)
    price = models.IntegerField(default=0)
    stock = models.PositiveIntegerField(default=0)
    available_display = models.BooleanField("Display", default=True)
    available_order = models.BooleanField("Order", default=True)

    class Meta:
        db_table = "products"
        ordering = ("-created", )
        verbose_name = "상품"
        verbose_name_plural = "판매중인 상품들"
    
    def __str__(self):
        return "[상품]"+self.title

    def get_absolute_url(self):
        pass
        
