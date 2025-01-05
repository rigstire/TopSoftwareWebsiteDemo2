from django.contrib.auth.forms import UserCreationForm  
from Users.models import Users


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Users
        fields = UserCreationForm.Meta.fields + (
            "email_field", 
            "company_name", 
            "first_name", 
            "last_name"
        )
        
