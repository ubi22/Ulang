from pocketbase import PocketBase
from password import password

client = PocketBase('http://127.0.0.1:8090')
admin_data = client.collection("_superusers").auth_with_password("zoom.main21@gmail.com", password)


def authorization_admin():
    return client


def authorization_user(login, password_user):
    pass