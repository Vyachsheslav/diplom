from django.contrib import admin

from main.models import Category, Product, Shop, ProductInfo, Parameter, ProductParameter, Contact, \
    Order, OrderItem, ConfirmEmailToken

admin.site.register(Category)
admin.site.register(Parameter)


@admin.register(ConfirmEmailToken)
class UserAdmin(admin.ModelAdmin):
    list_display = ('user', 'created_at', 'key')


@admin.register(Contact)
class UserAdmin(admin.ModelAdmin):
    list_display = ('user', 'city', 'street', 'house', 'phone')


@admin.register(Order)
class UserAdmin(admin.ModelAdmin):
    list_display = ('user', 'dt', 'state', 'contact')


@admin.register(OrderItem)
class UserAdmin(admin.ModelAdmin):
    list_display = ('order', 'product_info', 'quantity')


@admin.register(Product)
class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'category')


@admin.register(ProductInfo)
class UserAdmin(admin.ModelAdmin):
    list_display = ('model', 'product', 'shop', 'quantity', 'price', 'price_rrc', 'description')


@admin.register(ProductParameter)
class UserAdmin(admin.ModelAdmin):
    list_display = ('product_info', 'parameter', 'value')


@admin.register(Shop)
class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'user', 'state')
