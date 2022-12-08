from django.urls import path
from . import views
from rest_framework.routers import SimpleRouter

# Code using Routers
router = SimpleRouter()
router.register("users",views.UserViewSet, basename="users")
router.register("", views.PostViewSet, basename="posts")

urlpatterns = router.urls

# Code without Routers. Uncomment to test out
# urlpatterns = [
#     path("<int:pk>/", views.PostDetail.as_view(), name="post_detail"),
#     path("", views.PostList.as_view(), name="post_list"),
#     path("users/", views.UserList.as_view(), name="user_list"),
#     path("users/<int:pk>", views.UserDetail.as_view(), name="user_detail"),
# ]