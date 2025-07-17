from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from news.views import news_list_view, news_detail_view, add_news_view, delete_news_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', news_list_view, name='home'),
    path('news/<int:pk>/', news_detail_view, name='news_detail'),
    path('news/add/', add_news_view, name='add_news'),
    path('news/delete/<int:pk>/', delete_news_view, name='delete_news'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
