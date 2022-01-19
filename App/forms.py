from socket import fromshare
from tkinter.tix import Form
from django import forms

class Formulario_auto(forms.Form):

    marca=forms.CharField()
    modelo=forms.CharField()
    color=forms.CharField()
    km=forms.IntegerField()


class Formulario_moto(forms.Form):
    marca=forms.CharField()
    modelo=forms.CharField()
    color=forms.CharField()
    km=forms.IntegerField()


class Formulario_propietario(forms.Form):
    nombre=forms.CharField()
    apellido=forms.CharField()
    dni=forms.IntegerField()
    email=forms.EmailField()
    fechaDeAdquisicion=forms.DateField()

    
