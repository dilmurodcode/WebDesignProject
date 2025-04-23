from django.contrib import admin
from app.models import *
from unfold.admin import ModelAdmin as UnfoldAdmin

# Register your models here.

@admin.register(BaseModel)
class BaseModelAdmin(UnfoldAdmin):
    list_display = ('id', 'created_at', 'updated_at')
    list_filter = ('id', 'created_at', 'updated_at')


@admin.register(Specialization)
class SpecializationAdmin(UnfoldAdmin):
    list_display = ('id', 'name')
    list_filter = ('id', 'name')


@admin.register(Award)
class AwardAdmin(UnfoldAdmin):
    list_display = ('id', 'image', 'url', 'name')
    list_filter = ('id', 'name')


@admin.register(AwardWinner)
class AwardWinnerAdmin(UnfoldAdmin):
    list_display = ('id', 'portfolio', 'url', 'competition_name', 'specialization', 'award')
    list_filter = ('id', 'competition_name')


@admin.register(Review)
class ReviewAdmin(UnfoldAdmin):
    list_display = ('id', 'full_name', 'position', 'photo', 'description')
    list_filter = ('id', 'full_name')


@admin.register(Service)
class ServiceAdmin(UnfoldAdmin):
    list_display = ('id', 'name', 'status')
    list_filter = ('id', 'name')


@admin.register(WebSiteService)
class WebSiteServiceAdmin(UnfoldAdmin):
    list_display = ('id', 'title', 'order')
    list_filter = ('id', 'order')


@admin.register(ApplicationType)
class ApplicationTypeAdmin(UnfoldAdmin):
    list_display = ('id', 'name')
    list_filter = ('id', 'name')


@admin.register(Application)
class ApplicationAdmin(UnfoldAdmin):
    list_display = ('id', 'full_name', 'phone')
    list_filter = ('id', 'full_name')


@admin.register(SEOAnalytic)
class SEOAnalyticAdmin(UnfoldAdmin):
    list_display = ('id', 'name', 'order')
    list_filter = ('id', 'name')


@admin.register(Feat)
class FeatAdmin(UnfoldAdmin):
    list_display = ('id', 'name')
    list_filter = ('id', 'name')


@admin.register(Portfolio)
class PortfolioAdmin(UnfoldAdmin):
    list_display = ('id', 'poster')
    list_filter = ('id',)


@admin.register(ProjectProgress)
class ProjectProgressAdmin(UnfoldAdmin):
    list_display = ('id', 'order', 'image', 'portfolio')
    list_filter = ('id',)


@admin.register(Article)
class ArticleAdmin(UnfoldAdmin):
    list_display = ('id', 'order')
    list_filter = ('id',)


