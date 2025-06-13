from django.contrib import admin
from .models import ChaiVarity, ChaiReview, Store, ChaiCertificate
# Register your models here.

# 
class ChaiReviewInline(admin.TabularInline): 
    # TabularInline displays the form in a table format
    # # StackedInline displays the form in a stacked format
    model = ChaiReview
    extra = 2 # Number of empty forms to display
    # extra 2 means how many empty forms to display in the inline formset

class ChaiVarityAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'date_added')  # Fields to display in the list view
    # search_fields = ('name', 'type')  # Fields to search in the admin interface/
    # list_filter = ('type',)  # Fields to filter by in the admin interface
    inlines = [ChaiReviewInline]  # Inline model for reviews
    
class StoreAdmin(admin.ModelAdmin):
    list_display = ('name', 'location')  # Fields to display in the list view
    # search_fields = ('name', 'location')  # Fields to search in the admin interface
    filter_horizontal = ('chai_varities',)  # Many-to-many field for chai varities
    
class ChaiCertificateAdmin(admin.ModelAdmin):
    list_display = ('chai', 'certificate_number')  # Fields to display in the list view
    # search_fields = ('chai__name', 'certificate_number')  # Fields to search in the admin interface    
    
admin.site.register(ChaiVarity, ChaiVarityAdmin) # injecting the ChaiVarityAdmin class
admin.site.register(Store, StoreAdmin) # injecting the StoreAdmin class
admin.site.register(ChaiCertificate, ChaiCertificateAdmin) # injecting the ChaiCertificateAdmin class
