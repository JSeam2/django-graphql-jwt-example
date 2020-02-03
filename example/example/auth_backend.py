from django.contrib.auth import get_user_model
from example.settings import custom_get_user_by_natural_key

UserModel = get_user_model()

class AuthBackend:
    def authenticate(self, request, username=None, password=None, **kwargs):
        if username is None or password is None:
            return None

        user = custom_get_user_by_natural_key(username)

        if user is not None and user.check_password(password) and user.is_active:
            return user

        return None

    def get_user(self, user_id):
        return None
