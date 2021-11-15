from django.urls import path

from .views import index, other_page, BBLogonView, profile, BBlogoutView, ChangeUserInfoView, BBPasswordChangeview, \
    RegisterUserView, RegisterDoneView, user_activate, DeleteUserView

app_name = 'main'
urlpatterns = [
    path('accounts/register/delete/', DeleteUserView.as_view(), name='profile_delete'),
    path('accounts/register/<str:sign>/', user_activate, name='register_activate'),
    path('accounts/register/done', RegisterDoneView.as_view(), name='register_done'),
    path('accounts/register/', RegisterUserView.as_view(), name='register'),
    path('accounts/logout/', BBlogoutView.as_view(), name='logout'),
    path('accounts/password/change', BBPasswordChangeview.as_view(), name='password_change'),
    path('accounts/profile/change/', ChangeUserInfoView.as_view(), name='profile_change'),
    path('accounts/profile/', profile, name='profile'),
    path('accounts/login/', BBLogonView.as_view(), name='login'),
    path('<str:page>/', other_page, name='other'),
    path('', index, name='index'),
]
