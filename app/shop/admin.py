from django.contrib import admin

from shop.models import Visit, Employee, Market


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone',)
    search_fields = ("name",)


class MarketAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', "employee")
    search_fields = ("name",)


class VisitAdmin(admin.ModelAdmin):
    list_display = ('id', 'market', 'latitude', 'longitude', 'visit_date', "employee")
    list_filter = ('market',)
    search_fields = ("market__name", "market__employee__name")

    def employee(self, obj: Visit):
        """вытаскиваем имя работника в посещение"""
        return obj.market.employee.name


admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Market, MarketAdmin)
admin.site.register(Visit, VisitAdmin)
