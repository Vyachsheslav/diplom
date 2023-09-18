"""
URL configuration for orders project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django_rest_passwordreset.views import reset_password_request_token, reset_password_confirm

from main.views import RegisterAccount, LoginAccount, AccountDetails, ProductView, ProductsInfoView, \
    ProductPageView, BasketView, PartnerUpdateView, PartnerStateView, PartnerOrdersView, PartnerOrderView, \
    ContactView, OrderView, ConfirmAccount, CategoryView, ShopView, PartnerUpdateFromFileView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('basket/', BasketView.as_view(), name='basket'),
    path('categories/', CategoryView.as_view(), name='categories'),
    path('order/', OrderView.as_view(), name='order'),
    path('partner/orders/', PartnerOrdersView.as_view(), name='partner-orders'),
    path('partner/order/<pk>/', PartnerOrderView.as_view(), name='partner-order'),
    path('partner/state/', PartnerStateView.as_view(), name='partner-state'),
    path('partner/update/', PartnerUpdateView.as_view(), name='partner-update'),
    path('partner/update/from_file/', PartnerUpdateFromFileView.as_view(), name='partner-update'),
    path('products/', ProductView.as_view(), name='products'),
    path('products/info/', ProductsInfoView.as_view(), name='products-info'),
    path('products/info/<pk>/', ProductPageView.as_view(), name='products-info'),
    path('shops/', ShopView.as_view(), name='shops'),
    path('user/contact/', ContactView.as_view(), name='user-contact'),
    path('user/details/', AccountDetails.as_view(), name='user-details'),
    path('user/login/', LoginAccount.as_view(), name='user-login'),
    path('user/password_reset/', reset_password_request_token, name='password-reset'),
    path('user/password_reset/confirm/', reset_password_confirm, name='password-reset-confirm'),
    path('user/register/', RegisterAccount.as_view(), name='user-register'),
    path('user/register/confirm/', ConfirmAccount.as_view(), name='user-register'),
]
