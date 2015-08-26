from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /lanternapp/
    url(r'^$', views.index, name='index'),

    # ex: /lanternapp/add
    url(r'^add/$', views.add, name='add'),

    # ex: /lanternapp/edit/3456345
    url(r'^edit/(?P<pk>[0-9]+)/$', views.edit, name='edit'),

    # ex: /lanternapp/delete/3456345
    url(r'^delete/(?P<pk>[0-9]+)/$', views.delete, name='delete'),

    # ex: /lanternapp/add-lot/
    url(r'^add-lot/(?P<p>[\w-]+)/$', views.add_lot, name='add_lot'),

    # ex: /lanternapp/lot/3456345
    url(r'^lot/(?P<p>[\w-]+)/0(?P<pk>[0-9]+)/$', views.view_lot, name='view_lot'),

    # ex: /lanternapp/delete-lot/3456345
    url(r'^delete-lot/(?P<p>[\w-]+)/(?P<pk>[0-9]+)/$', views.delete_lot, name='delete_lot'),

    # ex: /lanternapp/manage/settings
    url(r'^manage/settings/$', views.settings, name='settings'),

    # ex: /lanternapp/manage/categories
    url(r'^manage/categories/$', views.categories, name='categories'),

    # ex: /lanternapp/manage/categories/3456345
    url(r'^manage/categories/(?P<pk>[0-9]+)/$', views.edit_category, name='edit_category'),

    # ex: /lanternapp/delete-category/3456345
    url(r'^manage/categories/(?P<pk>[0-9]+)/delete/$', views.delete_category, name='delete_category'),

    # ex: /lanternapp/manage/
    url(r'^manage/payments/$', views.payments, name='payments'),

    # ex: /lanternapp/login
    url(r'^login/$', views.login, name='login'),

    # ex: /lanternapp/logout
    url(r'^logout/$', views.logout, name='logout'),

    # ex: /lanternapp/register
    url(r'^register/$', views.register, name='register'),

]