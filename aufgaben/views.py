from django.http import HttpResponse
from django.shortcuts import render, redirect
from funktionen import get_aufgaben
import re


def view_aufgaben(request, themenbereich):
    temp = get_aufgaben(themenbereich)
    aufgaben = []
    for aufgabe in temp:
        aufgaben.append(aufgabe[2:])

    if request.method == 'POST':
        form_data = request.POST.dict()
        del form_data['csrfmiddlewaretoken']
        selected = ['.'.join(select.split('_')[1:]) for select in form_data.keys()]
        for j, select in enumerate(selected):
            for i in range(1, len(temp) + 1):
                pattern = f'^{i}\\.\\d+$'
                if re.match(pattern, select) and str(i) not in selected:
                    selected.insert(j, str(i))
        print(selected)
        return redirect(to=f'/kontrollen/erstellen/{themenbereich}/{selected}')

    return render(request, 'aufgaben.html', {'aufgaben': aufgaben, 'themenbereich': themenbereich})
