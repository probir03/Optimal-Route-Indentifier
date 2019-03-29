from django.urls import path
from django.urls import include
from django.conf.urls import url
from grids.views import grid_views

grids = [
    path('', grid_views.GridViewSet.as_view(), name='grids'),
    path('<grid_id>', grid_views.EachGridViewSet.as_view(), name='each_grid'),
]

app_name = 'grids'
urlpatterns = [
    url(r'grids/?', include(grids))
]