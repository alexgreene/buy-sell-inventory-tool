import datetime
from django.db import models
from django.utils import timezone

class Theme(models.Model):
	DEFAULT = 1
	name = models.CharField(max_length = 50)
	primary_color = models.CharField(max_length = 10)
	secondary_color = models.CharField(max_length = 10)

	def __str__(self):         
		return self.name

class Category(models.Model):
	DEFAULT = 1
	name = models.CharField(max_length=75)
	color = models.CharField(max_length=50)

	def __str__(self):         
		return self.name

class Flipper(models.Model):
	first_name = models.CharField(max_length = 50)
	email = models.CharField(max_length = 75)
	password = models.CharField(max_length = 75)
	app_title = models.CharField(max_length = 75, default="Flipper App")
	app_theme = models.ForeignKey(Theme, default = Theme.DEFAULT)

class TransactionLot(models.Model):
	flipper = models.ForeignKey(Flipper)
	title = models.CharField(max_length = 100)
	description = models.TextField()

	def __str__(self):         
		return self.title

	class Meta:
		abstract = True

class PurchaseLot(TransactionLot):
	price = models.IntegerField()
	date = models.DateField(blank = True, null = True)
	medium = models.CharField(max_length = 75)

class SaleLot(TransactionLot):
	price = models.IntegerField()
	date = models.DateField(blank = True, null = True)
	medium = models.CharField(max_length = 75)

class InventoryItem(models.Model):
	flipper = models.ForeignKey(Flipper)
	title = models.CharField(max_length = 100)
	description = models.TextField()

	purchase_lot = models.ForeignKey(PurchaseLot, blank=True, null=True)
	purchase_price = models.IntegerField(default=0)
	purchase_date = models.DateField(blank = True, null = True)
	purchase_medium = models.CharField(max_length = 75, blank = True, null = True)

	additional_expense = models.IntegerField(default=0)

	sale_lot = models.ForeignKey(SaleLot, blank=True, null=True)
	sale_price = models.IntegerField(default=0)
	sale_date = models.DateField(blank = True, null = True)
	sale_medium = models.CharField(max_length = 75, blank = True, null = True)

	category = models.ForeignKey(Category, default=Category.DEFAULT)


