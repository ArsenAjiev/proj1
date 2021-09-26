from django.shortcuts import render
from django.http import HttpResponse
from notes.forms import AddNoteForm
from notes.models import Note

def index(request):
    if request.method == 'POST':
        form = AddNoteForm(request.POST)
        if form.is_valid():
            Note.objects.create(
                title=form.cleaned_data["title"], text=form.cleaned_data["text"]
            )
            pass
    else:
        form = AddNoteForm()
    notes = Note.objects.all()
    return render(request, 'note_list.html', {'notes': notes, 'form': form})




# def index(request):
#     return render(request, 'note_list.html')

# Create your views here.
