from django.conf.urls.defaults import url, patterns
from django.contrib import admin
from django.contrib.admin.sites import AdminSite
from django.contrib.admin.views.main import ChangeList
from django.contrib.auth.models import User
from ewidencja.forms import PersonForm
from models import *



class LarchSite(AdminSite):
    def index(self, request, extra_context={}):
        self.index_template = 'larch_index.html'
            
        return super(LarchSite, self).index(request, extra_context)


class PersonChangeList(ChangeList):
    def url_for_result(self, result):
        return "/admin/ewidencja/person/%s" % str(result.id)

class PersonAdmin(admin.ModelAdmin):
    list_display = ['name', 'city']
    form = PersonForm

    def changelist_view(self, request, city_id=None, extra_context={}, **kwargs):
        if city_id:
            city = City.objects.get(pk=city_id)
            def _queryset(request):
                qs = super(PersonAdmin, self).queryset(request)
                qs = qs.filter(city=city)
                return qs
            self.queryset=_queryset
        return super(PersonAdmin, self).changelist_view(request, extra_context=extra_context, **kwargs)

    def get_changelist(self, request, **kwargs):
        return PersonChangeList


class CityAdmin(admin.ModelAdmin):
    def get_urls(self):
        return patterns('',
            url(r'^(?P<city_id>\d+)/persons/', self.admin_site.admin_view(PersonAdmin(Person, self.admin_site).
                changelist_view), name='city_persons'),
        ) + super(CityAdmin, self).get_urls()


larch = LarchSite(name='larch', app_name='larch')

larch.register(Person, PersonAdmin)
larch.register(City, CityAdmin)
larch.register(User)