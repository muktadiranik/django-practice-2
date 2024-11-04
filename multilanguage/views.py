from django.shortcuts import render
from .forms import BilingualForm


def bilingual_form_view(request):
    language = request.POST.get(
        'language') or request.GET.get('language', 'en')

    if request.method == 'POST':
        form = BilingualForm(request.POST, initial={'language': language})
        if form.is_valid():
            print(f"Language: {form.cleaned_data['language']}")
            print(f"Name: {form.cleaned_data[f'name_{language}']}")
            print(f"Email: {form.cleaned_data[f'email_{language}']}")
            print(f"Message: {form.cleaned_data[f'message_{language}']}")
            return render(request, 'success.html', {'language': language})
    else:
        form = BilingualForm(initial={'language': language})

    return render(request, 'bilingual_form.html', {'form': form, 'current_language': language})
