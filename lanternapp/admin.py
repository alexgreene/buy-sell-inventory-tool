from django.contrib import admin

# Register your models here.

from .models import Flipper
from .models import InventoryItem
from .models import PurchaseLot
from .models import SaleLot
from .models import Theme
from .models import Category

admin.site.register(Flipper)
admin.site.register(InventoryItem)
admin.site.register(PurchaseLot)
admin.site.register(SaleLot)
admin.site.register(Theme)
admin.site.register(Category)