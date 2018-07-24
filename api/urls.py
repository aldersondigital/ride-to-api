from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .managers import CategoryViewManager, ProductViewManager
from .views import CategoriesView, ProductsView

urlpatterns = {
    url(r'^categories/(?P<pk>\d+)$', CategoryViewManager.as_view()),
    url(r'^categories/$', CategoriesView.as_view()),
    url(r'^products/(?P<pk>\d+)$', ProductViewManager.as_view()),
    url(r'^products/$', ProductsView.as_view())
}

urlpatterns = format_suffix_patterns(urlpatterns)
