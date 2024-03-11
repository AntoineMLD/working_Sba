from django.contrib.auth import get_user_model

def create_test_user():
    username ='testuser'
    email = 'test@example.com'
    password = 'password123'
    User = get_user_model()
    User.objects.create_user(username=username, email=email, password=password)

create_test_user()