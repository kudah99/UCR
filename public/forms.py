
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Div
from django import forms
from .models import Customer , Bookings, CustomersMessage
from django.core.validators import RegexValidator
from phonenumber_field.formfields import PhoneNumberField
from bootstrap_datepicker_plus.widgets import DateTimePickerInput


# class NameWidget(forms.MultiWidget):

#     def __init__(self, attrs=None):
#         super().__init__([
#             forms.TextInput(),
#             forms.TextInput()
#         ], attrs)

#     def decompress(self, value):
#         if value:
#             return value.split(' ')
#         return ['', '']

# class NameField(forms.MultiValueField):

#     widget = NameWidget

#     def __init__(self, *args, **kwargs):

#         fields = (
#             forms.CharField(validators=[
#                 RegexValidator(r'[a-zA-Z]+', 'Enter a valid first name (only letters)')
#             ]),
#             forms.CharField(validators=[
#                 RegexValidator(r'[a-zA-Z]+', 'Enter a valid second name (only letters)')
#             ])
#         )

#         super().__init__(fields, *args, **kwargs)

#     def compress(self, data_list):
#         return f'{data_list[0]} {data_list[1]}'

TITLE_CHOICES = [
    ('MR', 'Mr.'),
    ('MRS', 'Mrs.'),
    ('MS', 'Ms.'),
    ('DR', 'Dr'),
    ('PROF', 'Prof'),
    ('ENG', 'Eng'),
    ('HON', 'Hon'),
]
GENDER_CHOICES = [
    ('MALE' , 'Male'),
    ('FEMALE', 'Female'),
    ('OTHER', 'Other')
]
class BookingForm(forms.ModelForm):
    customer_title = forms.ChoiceField(choices=TITLE_CHOICES ,label='select title')
    customer_name = forms.CharField(
        label='Enter Full Name',
        widget=forms.TextInput(attrs={'placeholder': 'Enter Full Name'})
        )
    phone_number = PhoneNumberField()
    vehicle_type  =  forms.CharField(
        label='Vehicle type',
        widget=forms.TextInput(
            attrs={'placeholder': 'Enter vehicle type'})
        )
    pick_up_Location = forms.CharField(
        label='Pick up Location',
        widget=forms.TextInput(attrs={'placeholder': 'e.g R.G.M Airport ' ,'start_datetime': DateTimePickerInput()})
        )
    drop_off_Location = forms.CharField(
        label='Drop off Location',
        widget=forms.TextInput(attrs={'placeholder': 'e.g Harare'})
        )
    pick_up_time = forms.DateField()
    drop_off_time = forms.DateField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper
        self.helper.form_method = 'post'
        self.helper.form_class = 'request-form ftco-animate bg-primary'

        self.helper.layout = Layout(
            Div(
                Div('customer_title',  css_class='col-md-6'),
                Div('customer_name',  css_class='col-md-6'),
                css_class='row fluid'
            ),
            Div(
                Div('phone_number',  css_class='col-md-6'),
                Div('vehicle_type',  css_class='col-md-6'),
                css_class='row fluid'
            ),
            Div(
                Div('pick_up_Location',  css_class='col-md-6'),
                Div('drop_off_Location',  css_class='col-md-6'),
                css_class='row fluid'
            ),
            Div(
                Div('pick_up_time',  css_class='col-md-6',),
                Div('drop_off_time',  css_class='col-md-6',),
                css_class='row fluid'
            ),
            Submit('submit', 'Rent A Car Now', css_class='btn btn-secondary py-3 px-4')
        )
    class Meta:
        model = Bookings
        fields = ('customer_title','customer_name','phone_number','vehicle_type','pick_up_Location','drop_off_Location','pick_up_time','drop_off_time')


class CustomerForm(forms.ModelForm):

    first_name = forms.CharField(
        label='Enter First Name'
        )
    last_name = forms.CharField(label='Enter Last Name')
    title = forms.ChoiceField(choices=TITLE_CHOICES ,label='select title')
    gender = forms.ChoiceField(choices=GENDER_CHOICES, label='select gender')
    email = forms.EmailField(label='E-Mail')
    phone_number = PhoneNumberField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            'first_name',
            'last_name',
            'title',
            'gender',
            'email',
            'phone_number',
            Submit('submit', 'Submit', css_class='btn btn-secondary py-3 px-4')
        )
    class Meta:
        model = Customer
        fields = ('first_name','last_name','title','gender','email','phone_number')


class ContactForm(forms.ModelForm):
    name = forms.CharField(label='Enter Name')
    email = forms.EmailField(label='E-Mail')
    category = forms.ChoiceField(choices=[('question', 'Question'),('quotation' , 'Quotation'),('enquiries', 'Enquiries') ,('other', 'Other')])
    subject = forms.CharField(required=False)
    body = forms.CharField(widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper
        self.helper.form_method = 'post'
        self.helper.form_class = " "

        self.helper.layout = Layout(
            'name',
            'email',
            'category',
            'subject',
            'body',
            Submit('submit', 'Submit', css_class='btn-success')
        )

    class Meta:
        model = CustomersMessage
        fields = ('name','email','subject', 'body')
