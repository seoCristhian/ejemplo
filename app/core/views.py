from django.shortcuts import render
from .forms import UsuarioForm

def registro(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'gracias.html')
    else:
        form = UsuarioForm()
    return render(request, 'registro.html', {'form': form})