from django import forms

class newadviser(forms.Form):
    adname=forms.CharField(label='Advisor Name',max_length=100)
    ad_id=forms.IntegerField(label="Advisor ID")
    bookingtime=forms.IntegerField(label='BookingTime')
    bookid=forms.IntegerField(label="Booking ID")
