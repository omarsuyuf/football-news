from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2406421200',
        'name': 'Omar Suyuf Wicaksono',
        'class': 'PBP E'
    }

    return render(request, "main.html", context)