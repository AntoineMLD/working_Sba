from django import forms
from django.contrib.auth.forms import UserCreationForm

from utils.environment import get_env
from .models import ModelApi, User

DEBUG = get_env('DEBUG') == '1'

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
    # Personnalisation des champs du formulaire avec des widgets et des valeurs initiales conditionnelles au mode DEBUG
    
    ApprovalDate = forms.DateField(label='Approval Date', widget=forms.DateInput(attrs={'class': 'date-input', 'type': 'date'}), initial=lambda: '2024-04-01' if DEBUG else '')
    Term = forms.IntegerField(label='Loan term in months', initial=lambda: '12' if DEBUG else '')
    NoEmp = forms.IntegerField(label='Number of business employees', initial=lambda: '5' if DEBUG else '')
    FranchiseCode = forms.ChoiceField(choices=FRANCHISECODE_CHOICES, label='Are you a franchisee ?', initial=lambda: 'No franchise' if DEBUG else '')
    Naics = forms.ChoiceField(choices=NAICS_CHOICES, label="Choose your industry", initial=lambda: NAICS_CHOICES[2] if DEBUG else '')
    ApprovalFY = forms.IntegerField(label='Fiscal year of commitment', initial=lambda: '2020' if DEBUG else '')
    NewExist = forms.ChoiceField(choices=NEWEXIST_CHOICES, label='New if it has existed for less than two years', initial=lambda: NEWEXIST_CHOICES[1] if DEBUG else '')
    LowDoc = forms.ChoiceField(choices=LOWDOC_CHOICES, label= 'Do you have a Loan Program ?', initial=lambda: LOWDOC_CHOICES[1] if DEBUG else '')
    GrAppv = forms.IntegerField(label='What is the gross amount of the loan approved by the bank ?', initial=lambda: '40000' if DEBUG else '')
    CreateJob = forms.IntegerField(label='Have you generated job creation ?', initial=lambda: '3' if DEBUG else '')
    RetainedJob = forms.IntegerField(label='Have any jobs been retained ?', initial=lambda: '0' if DEBUG else '')
    UrbanRural = forms.ChoiceField(choices=URBANRURAL_CHOICES, label='Are you located in a rural or urban area ?', initial=lambda: URBANRURAL_CHOICES[1] if DEBUG else '')
    RevLineCr = forms.ChoiceField(choices=REVLINECR_CHOICES, label='Is a revolving line of credit available ?', initial=lambda: URBANRURAL_CHOICES[0] if DEBUG else '')

    class Meta:
        model = ModelApi
        fields = '__all__'

    


# Définition d'un formulaire de connexion pour les utilisateurs   
class LoginForm(forms.Form):
    username = forms.CharField(max_length=65)
    password = forms.CharField(max_length=65, widget=forms.PasswordInput)



# Définition d'un formulaire d'inscription pour les nouveaux utilisateurs, étendant UserCreationForm pour inclure des fonctionnalités supplémentaires
class RegisterForm(UserCreationForm):
    class Meta:
        model=User
        fields = ['username', 'email', 'password1', 'password2']



# Définition d'un formulaire de contact simple pour la collecte de noms, emails et messages des utilisateurs

class ContactForm(forms.Form):
    name = forms.CharField(label='Your Name', max_length=100)
    email = forms.EmailField(label='Your Email')
    message = forms.CharField(label='Your message', widget=forms.Textarea)