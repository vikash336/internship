from advnetwork import views
from django.conf.urls import url
urlpatterns=[

    url('main',views.main),
    url('inuser',views.inuser),
    url('login',views.tstlogin),
    url('sign',views.tstsign),
    url('siggn',views.siggn),
    url('combine',views.combine),
    url('view',views.view),
    url('vik',views.vik),
    url('con',views.con),
    url('gusain',views.gusain),
    url('newadv',views.newadv),
    url('addd',views.add),

]
