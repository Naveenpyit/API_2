from .serializer import prodserializer
from .views import main_view
from django.urls import path
from rest_framework_simplejwt.views import ( # type: ignore
TokenObtainPairView, TokenRefreshView
)


urlpatterns=[
    path('api/products/',main_view,name='get&post'),
    path('api/products/<int:id>/',main_view,name='put&del'),
    # path('api/token/',TokenObtainPairView.as_view(),name='token_obtain'),
    # path('api/token/refresh/',TokenRefreshView.as_view(),name='token_refresh'),
]

