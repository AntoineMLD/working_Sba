from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import ModelApi, User


# Ce sont des tuples !
FRANCHISECODE_CHOICES = (
    ("Franchise" , "Franchise"),
    ("No franchise" , "No franchise")
)

NEWEXIST_CHOICES = (
    ("Existing business" , "Existing business"),
    ("New business" , "New business")
)

LOWDOC_CHOICES = (
    ("Yes Loan Program" , "Yes Loan Program"),
    ("No Loan Program" , "No Loan Program")
)

URBANRURAL_CHOICES = (
    ("Urban Zone" , "Urban Zone"),
    ("Rural Zone" , "Rural Zone")
)

REVLINECR_CHOICES = (
    ("No" , "No"),
    ("Yes" , "Yes")
)

NAICS_CHOICES = (
    ( 'Agriculture, forestry, fishing and hunting', 'Agriculture, forestry, fishing and hunting'),
    ('Mining, quarrying, and oil and gas extraction', 'Mining, quarrying, and oil and gas extraction'),
    ('Utilities', 'Utilities'),
    ( 'Construction','Construction'),
    ( 'Manufacturing', 'Manufacturing'),
    ( 'Wholesale trade', 'Wholesale trade'),
    ( 'Retail trade', 'Retail trade'),
    ( 'Transportation and warehousing', 'Transportation and warehousing'),
    ( 'Information', 'Information'),
    ( 'Finance and insurance', 'Finance and insurance'),
    ( 'Real estate and rental and leasing', 'Real estate and rental and leasing'),
    ( 'Professional, scientific, and technical services', 'Professional, scientific, and technical services'),
    ( 'Management of companies and enterprises', 'Management of companies and enterprises'),
    ( 'Administrative and support and waste management and remediation services', 'Administrative and support and waste management and remediation services'),
    ( 'Educational services', 'Educational services'),
    ( 'Health care and social assistance', 'Health care and social assistance'),
    ( 'Arts, entertainment, and recreation', 'Arts, entertainment, and recreation'),
    ( 'Accommodation and food services', 'Accommodation and food services'),
    ( 'Other services (except public administration)', 'Other services (except public administration)'),
    ( 'Public administration', 'Public administration'),
)


class ModelApiForm(forms.ModelForm):
    ApprovalDate = forms.DateField(label='Approval Date', widget=forms.DateInput(attrs={'class': 'date-input', 'type': 'date'}))
    Term = forms.IntegerField(label='Loan term in months')
    NoEmp = forms.IntegerField(label='Number of business employees')
    FranchiseCode = forms.ChoiceField(choices=FRANCHISECODE_CHOICES, label='Are you a franchisee ?')
    Naics = forms.ChoiceField(choices=NAICS_CHOICES, label="Choose your industry")
    ApprovalFY = forms.IntegerField(label='Fiscal year of commitment')
    NewExist = forms.ChoiceField(choices=NEWEXIST_CHOICES, label='New if it has existed for less than two years')
    LowDoc = forms.ChoiceField(choices=LOWDOC_CHOICES, label= 'Do you have a Loan Program ?')
    GrAppv = forms.IntegerField(label='What is the gross amount of the loan approved by the bank ?')
    CreateJob = forms.IntegerField(label='Have you generated job creation ?')
    RetainedJob = forms.IntegerField(label='Have any jobs been retained ?')
    UrbanRural = forms.ChoiceField(choices=URBANRURAL_CHOICES, label='Are you located in a rural or urban area ?')
    RevLineCr = forms.ChoiceField(choices=REVLINECR_CHOICES, label='Is a revolving line of credit available ?')

    class Meta:
        model = ModelApi
        fields = '__all__'

    
    
class LoginForm(forms.Form):
    username = forms.CharField(max_length=65)
    password = forms.CharField(max_length=65, widget=forms.PasswordInput)


class RegisterForm(UserCreationForm):
    class Meta:
        model=User
        fields = ['username', 'email', 'password1', 'password2']


class ContactForm(forms.Form):
    name = forms.CharField(label='Your Name', max_length=100)
    email = forms.EmailField(label='Your Email')
    message = forms.CharField(label='Your message', widget=forms.Textarea)