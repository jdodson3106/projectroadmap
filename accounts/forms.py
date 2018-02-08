from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from accounts.models import User, Employee

class RegistrationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('company_name', 'email', 'first_name',
                  'last_name', 'employee_phone', 'birth_date',
                  'admin', 'password1', 'password2')

        error_messages = {
            'first_name': {
                'max_length': ("The first name has too many characters. (200 max)"),
                'required': ("First name must be provided"),
            },
            'last_name': {
                'max_length': ("The last name has too many characters. (200 max)"),
                'required': ("Last name must be provided"),
            },
            'company_name': {
                'max_length': ("The company name has too many characters. (200 max)"),
            },
            'email':{
                'unique': ("The email address provided is already taken"),
                'required': ("Please enter an email address"),
            },
            'password1': {
                'required': ("A password must be provided"),
            },
            'password2': {
                'required': ("A password confirmation must be provided")
            }

        }

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        user.company_name = self.cleaned_data['company_name']
        user.employee_phone = self.cleaned_data['employee_phone']
        user.birth_date = self.cleaned_data['birth_date']
        user.admin = True


        user.save()
        return user

class NewEmployeeForm(UserCreationForm):

    class Meta:
        model = Employee
        fields = ('email', 'first_name',
                  'last_name', 'employee_phone', 'birth_date',
                  'admin')

    def save(self, commit=True):
        employee = super(NewEmployeeForm, self).save(commit=False)
        employee.first_name = self.cleaned_data['first_name']
        employee.last_name = self.cleaned_data['last_name']
        employee.email = self.cleaned_data['email']
        employee.employee_phone = self.cleaned_data['employee_phone']
        employee.birth_date = self.cleaned_data['birth_date']
        employee.admin = self.cleaned_data['admin']


        employee.save()
        return employee
