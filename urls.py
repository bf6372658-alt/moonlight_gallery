from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from gallery import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('create-board/', views.create_board, name='create_board'),
    path('category/<int:cat_id>/', views.category_detail, name='category_detail'),
    
    # This is the line that fixes your 404 error!
    path('upload/', views.upload_craft, name='upload_craft'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
