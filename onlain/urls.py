
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import ProductView, UserRegistrationView, CommentAPIView, RatingAPIView

urlpatterns = [
    path('api/v1/product/', ProductView.as_view()),
    path('api/reg', UserRegistrationView.as_view()),
    path('api/comment/', CommentAPIView.as_view()),
    path('api/Rating', RatingAPIView.as_view()),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]