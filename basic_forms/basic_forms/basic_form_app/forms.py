from django.core import validators

from django import forms


# for individual field
def check_for_z(value: str):

    if boo := value.lower().startswith("z"):
        return

    if not boo:
        raise forms.ValidationError("NEed to start with Z")


class FormName(forms.Form):
    name = forms.CharField(validators=[check_for_z])  # for individual
    # name = forms.CharField()
    email = forms.EmailField()
    verify_email = forms.EmailField(label="Enter your email agin")
    text = forms.CharField(widget=forms.Textarea)
    # bot_catcher = forms.CharField(
    #     required=False,
    #     widget=forms.HiddenInput,
    #     validators=[validators.MaxLengthValidator(0)],
    # )  # to catch automation bots

    # use django.core import validators
    # def clean_bot_catcher(self):
    #     """
    #     use clean to validate each method
    #     for ex: clean_text method will be used to validate the text field
    #     """
    #     bot_catcher = self.cleaned_data["bot_catcher"]
    #     if len(bot_catcher) > 0:
    #         raise forms.ValidationError("Gotcha Bot")
    #     return bot_catcher
    # clean method for entire form
    def clean(self):
        all_clean_data = super().clean()

        email = all_clean_data["email"]
        verify_mail = all_clean_data["verify_email"]

        if email != verify_mail:
            raise forms.ValidationError("Emails don't match")
