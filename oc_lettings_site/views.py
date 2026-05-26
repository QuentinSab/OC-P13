from django.shortcuts import render


# Lorem ipsum dolor sit amet, consectetur adipiscing elit.
def index(request):
    return render(request, 'index.html')


def error_404(request, exception):
    """
    Render custom 404 page.
    """
    return render(request, '404.html', status=404)


def error_500(request):
    """
    Render custom 500 page.
    """
    return render(request, '500.html', status=500)
