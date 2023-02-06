from django.http import HttpResponse
from django.shortcuts import render
from listings.models import Band, Listing

def hello(request):
    bands = Band.objects.all()
    return HttpResponse(f"""
                        <h1>Hello Django!</h1>
                        <p>Mes groupes préférés sont : </p>
                        <ul>
                            <li>{bands[0].name}</li>
                            <li>{bands[1].name}</li>
                            <li>{bands[2].name}</li>
                        </ul>
                        """)

def about(request):
    return HttpResponse('<h1>À propos</h> <p>Nous adorons merch !</p>')

def listings(request):
    titles = Listing.objects.all()
    return HttpResponse(f"""
                        <h1>Nos produits en ligne</h1>
                        <ul>
                            <li>{titles[0].title}</li>
                            <li>{titles[1].title}</li>
                            <li>{titles[2].title}</li>
                        </ul>
                        """)

def contact(request):
    return HttpResponse('<h1>Voulez-vous rester en contact</h1>')

# Create your views here.
