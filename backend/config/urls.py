from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from posts.views import PostViewSet, CommentViewSet
from likes.views import LikeViewSet
from users.views import RegisterView, UserProfileView, LogoutView
from django.http import HttpResponse


router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)
router.register(r'likes', LikeViewSet)

def home(request):
    return HttpResponse("Welcome to DjaR API!")


urlpatterns = [
    path('', home, name='home'),  # Главная страница
    path('admin/', admin.site.urls),
    path('api/auth/register/', RegisterView.as_view(), name='register'),
    path('api/auth/profile/', UserProfileView.as_view(), name='user-profile'),
    path('api/auth/logout/', LogoutView.as_view(), name='logout'),
    path('api/', include(router.urls)),
]