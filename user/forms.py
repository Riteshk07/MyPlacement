from django import forms
import re 

class Registration(forms.Form):
    error_css_class = 'error'
    required_css_class ='required'
    cl = {'class' : "form-control"}
    fname = forms.CharField(widget=forms.TextInput(attrs=cl), label='First Name', label_suffix=' ')
    lname = forms.CharField(widget=forms.TextInput(attrs=cl), label='Last Name', label_suffix=' ')
    email = forms.EmailField(
        widget=forms.TextInput(attrs={'class' : "form-control", 'onkeyup':"checkuser()"}), 
        error_messages={'required':'Enter valid Email Address'},label="Email Address", 
        label_suffix=' ',
        )
    password1 = forms.CharField(widget=forms.PasswordInput(attrs=cl), label="Password", label_suffix=" ")
    password2 = forms.CharField(widget=forms.PasswordInput(attrs=cl), label="Conform Password", label_suffix=" ")


    def clean_password1(self):
        regpass = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[$@$!%*?&+~|{}:;<>/])[A-Za-z\d$@$!%*?&+~|{}:;<>/]{8,24}"
        valpass = self.cleaned_data['password1']
        pat = re.compile(regpass)
        print(valpass)
        mat = re.fullmatch(pat, valpass)
        print(mat)
        if(len(valpass)<8):
            raise forms.ValidationError('Your Password is to short. It should be more than 8 charecter')
        if(len(valpass)>24):
            raise forms.ValidationError('Your Password is to long. It should be less than 24 charecter')
        if(mat == None):
            raise forms.ValidationError('Minimum eight characters, at least one letter, one number and one special character:')
        return valpass

    def clean(self): 
        cleaned_data = super(Registration,self).clean()
        valpass = cleaned_data.get("password1")
        valpass2 = cleaned_data.get("password2")
        if(valpass != valpass2):
            raise forms.ValidationError("Password and Confirm Password does not match")
        