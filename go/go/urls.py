from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from go import settings
from flatty.views import *

admin.autodiscover()

handler404 = 'flatty.views.page_not_found'
handler500 = 'flatty.views.page_error'

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'gogo.views.home', name='home'),
    # url(r'^gogo/', include('gogo.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^index/$', index),
    url(r'^index/index.html$', index),
    url(r'^index/form_styles.html$', form_styles),
    url(r'^index/sign_in.html$', sign_in),
    url(r'^index/sign_up.html$', sign_up),
    url(r'^index/forgot_password.html$', forgot_password),
    url(r'^index/user_profile.html$', user_profile),
    url(r'^index/wysiwyg.html$', wysiwyg),
    url(r'^index/wizard.html$', wizard),
    url(r'^index/address_book.html$', address_book),
    url(r'^index/blank.html$', blank),
    url(r'^index/buttons_and_icons.html$', buttons_and_icons),
    url(r'^index/calendar.html$', calendar),
    url(r'^index/charts.html$', charts),
    url(r'^index/chats.html$', chats),
    url(r'^index/closed_navigation.html$', closed_navigation),
    url(r'^index/email_templates.html$', email_templates),
    url(r'^index/faq.html$', faq),
    url(r'^index/filetrees.html$', filetrees),
    url(r'^index/fileupload.html$', fileupload),
    url(r'^index/fixed_header.html$', fixed_header),
    url(r'^index/fixed_navigation.html$', fixed_navigation),
    url(r'^index/fixed_navigation_and_header.html$', fixed_navigation_and_header),
    url(r'^index/form_components.html$', form_components),
    url(r'^index/form_styles.html$', form_styles),
    url(r'^index/gallery.html$', gallery),
    url(r'^index/grid.html$', grid),
    url(r'^index/inplace_editing.html$', inplace_editing),
    url(r'^index/invoice.html$', invoice),
    url(r'^index/orders.html$', orders),
    url(r'^index/pricing_tables.html$', pricing_tables),
    url(r'^index/search_results.html$', search_results),
    url(r'^index/tables.html$', tables),
    url(r'^index/timeline.html$', timeline),
    url(r'^index/todo.html$', todo),
    url(r'^index/type.html$', type),
    url(r'^index/ui_elements.html$', ui_elements),
    url(r'^index/validations.html$', validations),
    url(r'^index/widgets.html$', widgets),
    url(r'^index/err500.html$', page_error),
    url(r'^index/auto.html$', auto),
    (r'^site_media/(?P<path>.*)$', 'django.views.static.serve', {'document_root':settings.STATIC_ROOT}),
)
