from django import forms


class Customer_Form(forms.Form):
    first_name = forms.CharField(
        max_length=20, label="First Name:", required=True
    )
    middle_initial = forms.CharField(
        max_length=1, label="M.I.:"
    )
    last_name = forms.CharField(
        max_length=20, label="Last Name:", required=True
    )
    suffix = forms.CharField(
        max_length=5, label="Suffix:", required=False
    )
    address = forms.CharField(
        max_length=50, label="Street Address:", required=True
    )
    zip_code = forms.IntegerField(label="Zip:")
    # dashes between the number
    telephone_number = forms.IntegerField(
        required=True, label="Telephone:"
    )
    email = forms.EmailField(
        max_length=50, required=False, label="Email:"
    )
    date_of_birth = forms.DateField(required=True, label="Date of Birth")
    home_ownership = forms.CharField(label="Do you Rent or Own Your Home?")


class Vehicle_Form(forms.Form):
    Vehicle_Identification_Number = forms.IntegerField(
        required=True,
        label="What is the vehicle identification number for your vehicle?",
    )
    Annual_Mileage = forms.IntegerField(
        required=True, label="How many miles do you drive each year?"
    )


class Driver_Form(forms.Form):

    Usage_Type = forms.CharField(
        required=True,
        label="Will this vehicle be used for work, school, pleasure, or business?",
    )
    Driver_First_Name = forms.CharField(
        required=True, label="What is your drivers first name?"
    )
    Driver_Last_Name = forms.CharField(
        required=True, label="What is your drivers last name?"
    )
    Driver_Relation = forms.CharField(
        required=True, label="What is the relationship does this driver have to you?"
    )
    US_State = forms.CharField(
        required=True, label="In what US state do you have your license?"
    )
    Drivers_License_Number = forms.IntegerField(
        required=True, label="What is your drivers license number?"
    )
    Drivers_License_Status = forms.CharField(
        required=True, label="What is your current status of your drivers license?"
    )
