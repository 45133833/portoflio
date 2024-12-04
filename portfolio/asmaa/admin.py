from django.contrib import admin
from .models import Home , Portfolio, About,Profile,skills,Category

# Register your models here.
admin.site.register(Home)

class profileInline(admin.TabularInline):
    model= Profile
    extra= 1 

@admin.register(About)
class aboutAdmin(admin.ModelAdmin):
    inlines=[
        profileInline,
        ]
    
class skillInline(admin.TabularInline):
    model=skills
    extra= 2

@admin.register(Category)
class categoryAdmin(admin.ModelAdmin):
    inlines=[
        skillInline,
    ]

admin.site.register(Portfolio)
    
    