import os
import datetime

from django.http import HttpResponse, FileResponse
from django.shortcuts import render, redirect
from .models import Kontrollen, ErstellteKontrollen
from .forms import Kontrolle, KontrolleErstellen
from funktionen import get_uuid

path = '/'.join(os.path.abspath(__file__).split('\\')[:-2])


# Create your views here.
def view_kontrollen(request):
    if request.method == 'POST':
        form = Kontrolle(request.POST)
        if form.is_valid():
            kontrolle = form.cleaned_data['identifier']
            uuid = erstellen(identifier=kontrolle)
            # return redirect(to=f'pdf/{kontrolle} {uuid}')
            return redirect(to=f'/finden/{kontrolle} {uuid}')
    else:
        form = Kontrolle()
    return render(request, 'kontrollen.html',
                  {'form': form, 'Kontrollen': Kontrollen.objects.all().filter(sichtbar=True).order_by('identifier')})


def erstellen(identifier, schule='', schulart='', kurs='', lehrer='', datum='', probe=True, aufgaben=None, schnell=False):
    uuid = get_uuid()
    cwd = os.getcwd()
    os.chdir(f'{path}/matheKontrollen')
    if schnell:
        os.system(f'python "{identifier}.py" "{uuid}" "{probe}"')
    elif aufgaben is None:
        os.system(f'python "{identifier}.py" "{uuid}" "0:{schule}" "1:{schulart}" "2:{kurs}" '
                  f'"5:{lehrer}" "8:{datum}" "{probe}"')
    else:
        os.system(f'python "{identifier}.py" "{uuid}" "0:{schule}" "1:{schulart}" "2:{kurs}" '
                  f'"5:{lehrer}" "8:{datum}" "{probe}" "{aufgaben}"')
    os.chdir(cwd)
    kontrolle = ErstellteKontrollen(identifier=identifier, uuid=uuid)
    kontrolle.save()
    return uuid


def view_pdf(response, identifier):
    beispiel = True if identifier.split(' ')[0] == 'Beispiel' else False
    if beispiel:
        file_path = f'{path}/matheKontrollen/pdf/beispiele/{identifier}.pdf'
    else:
        file_path = f'{path}/matheKontrollen/pdf/{identifier}.pdf'
    return FileResponse(open(file_path, 'rb'), content_type='application/pdf')


def download_pdf(response, identifier):
    file_path = f'{path}/matheKontrollen/pdf/{identifier}.pdf'
    with open(file_path, 'rb') as fh:
        response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
        response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
        return response


def kontrolle_erstellen_konfigo(request, identifier, aufgaben=None):
    try:
        name = Kontrollen.objects.get(identifier=identifier)
    except:
        name = identifier

    if request.method == 'POST':
        form = KontrolleErstellen(request.POST)
        if form.is_valid():
            identifier = form.cleaned_data['identifier']
            schule = form.cleaned_data['schule']
            schulart = form.cleaned_data['schulart']
            kurs = form.cleaned_data['kurs']
            lehrer = form.cleaned_data['lehrer']
            datum = form.cleaned_data['datum'].strftime('%d.%m.%Y') if form.cleaned_data['datum'] is not None else None
            kontrollen_art = form.cleaned_data['kontrollen_art']
            probe = True if kontrollen_art == 'Probe' else False
            uuid = erstellen(identifier, schule, schulart, kurs, lehrer,
                             datum, probe, aufgaben)

            return redirect(to=f'/suchen/{identifier} {uuid}')
    else:
        form = KontrolleErstellen()

    return render(request, 'erstellen.html', context={'form': form, 'identifier': identifier, 'name': name})


def kontrolle_erstellen(request, identifier):
    uuid = erstellen(identifier, schnell=True)

    return redirect(to=f'/suchen/{identifier} {uuid}')
