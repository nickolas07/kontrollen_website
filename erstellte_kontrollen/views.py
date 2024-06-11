import glob
import os
import time

from django.db.models import QuerySet
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

from .forms import Kontrolle
from kontrollen.models import ErstellteKontrollen, Kontrollen

path = '/'.join(os.path.abspath(__file__).split('\\')[:-2])


# Create your views here.
def home(request):
    if request.method == 'POST':
        form = Kontrolle(request.POST)
        if form.is_valid():
            uuid = ''
            for value in form.cleaned_data.values():
                uuid += str(value).upper()
                uuid += '-' if len(uuid) == 4 else ''

            kontrolle_db: QuerySet = ErstellteKontrollen.objects.filter(uuid=uuid).values()
            if kontrolle_db:
                kontrolle__db_str = f'{kontrolle_db[0]['identifier']} {kontrolle_db[0]['uuid']}'
            else:
                kontrolle__db_str = None

            kontrolle_file = glob.glob(f'{path}/matheKontrollen/pdf/*{uuid}.pdf')
            kontrolle_file_str = kontrolle_file[0].split('\\')[1][:-4] if kontrolle_file else None

            if kontrolle__db_str == kontrolle_file_str and (
                    kontrolle__db_str is not None and kontrolle__db_str is not None):
                return redirect(to=f'{kontrolle__db_str}/')
            else:
                return redirect(to=f'notFound/')
    else:
        form = Kontrolle()
    return render(request, 'kontrolleSuchen.html', {'form': form})


def view_kontrolle(request, identifier: str):
    identifier = identifier.replace('.pdf', '')
    beispiel = True if identifier.split(' ')[0] == 'Beispiel' else False
    if beispiel:
        name = Kontrollen.objects.filter(identifier=' '.join(identifier.split(' ')[1:])).get().name
        return render(request, 'viewKontrolle.html', {'beispiel': beispiel,
                                                       'name': f'Beispiel: {name}',
                                                       'identifier': identifier,
                                                       'path': f'{path}/matheKontrollen/pdf/{name}'})
    else:
        try:
            name = Kontrollen.objects.filter(identifier=' '.join(identifier.split(' ')[:-1])).get().name
            return render(request, 'viewKontrolle.html', {'beispiel': beispiel, 'name': name,
                                                          'identifier': identifier,
                                                          'path': f'{path}/matheKontrollen/pdf/{name}'})
        except:
            name = identifier
            return render(request, 'viewKontrolle.html', {'beispiel': beispiel, 'name': name,
                                                          'identifier': identifier,
                                                          'path': f'{path}/matheKontrollen/pdf/{name}'})


def not_found(request):
    return render(request, 'nichtGefunden.html')


def delete(request, name):
    ErstellteKontrollen.objects.filter(uuid=name.split(' ')[-1]).delete()
    os.remove(f'{path}/matheKontrollen/pdf/{name}.pdf')
    os.remove(f'{path}/matheKontrollen/pdf/{name} - Lsg.pdf')
    time.sleep(1)
    return redirect(to=f'/')
