from django.http import HttpResponse
from django.shortcuts import render

from django.shortcuts import render_to_response,redirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

from django.shortcuts import get_object_or_404

from .models import Flipper, InventoryItem, SaleLot, PurchaseLot, Theme, Category

from .forms import RegisterForm, LoginForm, ItemForm, PurchaseLotForm, SaleLotForm, ManageForm, CategoryForm

import crypt
import random

def index(request):
	# Handle user account
	if 'flipper_id' not in request.session:
		logged_in = False
		email = False
		all_items = False
	else:
		logged_in = True
		s = Flipper.objects.get(id=request.session['flipper_id'])
		name = s.first_name

	# GET ALL THE DATAS!!!!
		all_items = InventoryItem.objects.all()

		for item in all_items:
			item.net_change = item.sale_price - item.purchase_price - item.additional_expense
			if item.sale_lot:
				date_s = item.sale_lot.date
			else:
				date_s = item.sale_date

			if item.purchase_lot:
				date_p = item.purchase_lot.date
			else:
				date_p = item.purchase_date

			item.time_to_sale = (date_s - date_p).days

	return render(request, 'lanternapp/index.html', { 'logged_in': logged_in, 'name': name, 'all_items': all_items })

def add(request):
	s = Flipper.objects.get(id=request.session['flipper_id'])
	email = s.email

	if request.method == "POST":
		form = ItemForm(request.POST)
		if form.is_valid():
			frm = form.save(commit=False)
			frm.flipper = Flipper.objects.get(id=request.session['flipper_id'])
			frm.save()
			return redirect('lanternapp.views.index')
	else:
		form = ItemForm()

	return render(request, 'lanternapp/item.html', { 'form': form, 'email': email, 'editing': False })

def edit(request, pk):
	s = Flipper.objects.get(id=request.session['flipper_id'])
	email = s.email
	item = get_object_or_404(InventoryItem, pk=pk)
	if request.method == "POST":
		form = ItemForm(request.POST, instance=item)
		if form.is_valid():
			item = form.save(commit=False)
			item.save()
			return redirect('lanternapp.views.index')
	else:
		form = ItemForm(instance=item)
	return render(request, 'lanternapp/item.html', { 'form': form, 'email': email, 'item': item, 'editing': True })

def delete(request, pk):
    item_to_delete = InventoryItem.objects.get(pk=pk).delete()

    return redirect('lanternapp.views.index')

def add_lot(request, p):

	if p == 'purchase':
		is_purchase = True
	else:
		is_purchase = False

	s = Flipper.objects.get(id=request.session['flipper_id'])
	email = s.email

	if request.method == "POST":
		if is_purchase == 1:
			form = PurchaseLotForm(request.POST)
		else:
			form = SaleLotForm(request.POST)

		if form.is_valid():
			frm = form.save(commit=False)
			frm.flipper = Flipper.objects.get(id=request.session['flipper_id'])
			frm.save()
			return redirect('lanternapp.views.index')
	# else:
	if is_purchase > 0:
		form = PurchaseLotForm()
	else:
		form = SaleLotForm()
	
	return render(request, 'lanternapp/addlot.html', { 'form': form, 'email': email, 'is_purchase': is_purchase })

def view_lot(request, p, pk):

	if p == 'purchase':
		is_purchase = True
	else:
		is_purchase = False

	s = Flipper.objects.get(id=request.session['flipper_id'])
	email = s.email

	show_delete = False
	value_for_total = 0
	lots_in_total = list()

	if is_purchase == True:
		lot = get_object_or_404(PurchaseLot, pk=pk)
		all_items_in_lot = InventoryItem.objects.filter(purchase_lot=lot)
		if all_items_in_lot is None:
			show_delete = True
		else:
			for item in all_items_in_lot:
				if item.sale_lot == None:
					value_for_total += item.sale_price
				elif item.sale_lot.pk in lots_in_total:
					value_for_total += 0
				else:
					value_for_total += item.sale_lot.price
					lots_in_total.append(item.sale_lot.pk)
			lot.profit = value_for_total - lot.price

	else:
		lot = get_object_or_404(SaleLot, pk=pk)
		all_items_in_lot = InventoryItem.objects.filter(sale_lot=lot)
		if all_items_in_lot is None:
			show_delete = True
		else:
			for item in all_items_in_lot:
				if item.purchase_lot == None:
					value_for_total += item.purchase_price
				elif item.purchase_lot.pk in lots_in_total:
					value_for_total += 0
				else:
					value_for_total += item.purchase_lot.price
					lots_in_total.append(item.purchase_lot.pk)
			lot.profit = lot.price - value_for_total
	
	if request.method == "POST":
		if is_purchase == True:
			form = PurchaseLotForm(request.POST, instance=lot)
		else:
			form = SaleLotForm(request.POST, instance=lot)

		if form.is_valid():
			lot = form.save(commit=False)
			lot.flipper = Flipper.objects.get(id=request.session['flipper_id'])
			lot.save()
			return redirect('lanternapp.views.index')
	else:
		if is_purchase == True:
			form = PurchaseLotForm(instance=lot)
		else:
			form = SaleLotForm(instance=lot)

	return render(request, 'lanternapp/lot.html', { 'form': form, 'email': email, 'lot': lot, 'all_items_in_lot':all_items_in_lot,
		'show_delete':show_delete,'is_purchase': is_purchase, 'value_for_total':value_for_total })

def delete_lot(request, p, pk):

	if p == 'purchase':
		lot_to_delete = PurchaseLot.objects.get(pk=pk).delete()
	else:
		lot_to_delete = SaleLot.objects.get(pk=pk).delete()

	return redirect('lanternapp.views.index')

def settings(request):
	
	person = Flipper.objects.get(id=request.session['flipper_id'])
	email = person.email

	if request.method == "POST":
		form = ManageForm(request.POST, instance=person)
		if form.is_valid():
			settings = form.save(commit=False)
			settings.save()
			return redirect('lanternapp.views.settings')
	else:
		form = ManageForm(instance=person)

	return render(request, 'lanternapp/settings.html', { 'form': form, 'flipper': person, 'email': email })

def categories(request):
	
	person = Flipper.objects.get(id=request.session['flipper_id'])
	email = person.email

	if request.method == "POST":
		form = CategoryForm(request.POST)
		if form.is_valid():
			frm = form.save(commit=False)
			frm.flipper = Flipper.objects.get(id=request.session['flipper_id'])
			frm.save()
			return redirect('lanternapp.views.categories')
	else:
		form = CategoryForm()
		categories = Category.objects.all()

	return render(request, 'lanternapp/categories.html', { 'form': form, 'flipper': person, 'categories': categories, 'email': email})

def edit_category(request, pk):

	person = Flipper.objects.get(id=request.session['flipper_id'])
	email = person.email

	category = get_object_or_404(Category, pk=pk)
	if request.method == "POST":
		form = CategoryForm(request.POST, instance=category)
		if form.is_valid():
			cat = form.save(commit=False)
			cat.save()
			return redirect('lanternapp.views.categories')
	else:
		form = CategoryForm(instance=category)
	return render(request, 'lanternapp/category.html', { 'form': form, 'email': email, 'category': category, 'email': email })

def delete_category(request, pk):

	lot_to_delete = get_object_or_404(Category, pk=pk).delete()
	items_to_update = InventoryItem.objects.filter(flipper=request.session['flipper_id'], category=pk)
	for item in items_to_update:
		item.category = 1
		item.save()

	return redirect('lanternapp.views.categories')

def payments(request):
	
	person = Flipper.objects.get(id=request.session['flipper_id'])
	email = person.email

	return render(request, 'lanternapp/payments.html', { 'flipper': person, 'email': email })

def login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
			data = form.cleaned_data
			try:
				flpr = Flipper.objects.get(email=request.POST['email'])
				if flpr.password == crypt.crypt(request.POST['password'], flpr.password):
					request.session['flipper_id'] = flpr.id
					return redirect('lanternapp.views.index')
				else:
					return HttpResponse("Your username and password didn't match.")
			except Flipper.DoesNotExist:
				return HttpResponse("User does not exist.")
    else:
        form = LoginForm()
    return render(request, 'lanternapp/login.html', {'form': form})    

def logout(request):
	try:
		del request.session['flipper_id']
	except KeyError:
		pass
	return redirect('lanternapp.views.index')

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            frm = form.save(commit=False)
            try: # Make sure this email is not already in the system
            	flpr = Flipper.objects.get(email=request.POST['email'])
            	return HttpResponse('This email is already assocciated with another account.')
            except Flipper.DoesNotExist: 
            	rndsalt  = ''.join(random.choice('0123456789ABCDEF') for i in range(16))
            	frm.password = crypt.crypt(frm.password, rndsalt)
            	frm.save()
            	return redirect('lanternapp.views.index')
    else:
        form = RegisterForm()
    return render(request, 'lanternapp/register.html', { 'form': form })

