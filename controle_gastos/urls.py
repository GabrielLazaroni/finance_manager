from django.contrib import admin
from django.urls import path
from contas.views import home, listagem, nova_transacao, update, login, register, delete

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login, name='url_login'),
    path('home/', home),
    path('register/', register, name='url_register'),
    path('listagem/', listagem, name='url_listagem'),
    path('nova/', nova_transacao, name='url_nova'),
    path('update/<int:pk>/', update, name='url_update'),
    path('delete/<int:pk>/', delete, name='url_delete')
]
