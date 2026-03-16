from django.shortcuts import render

def map_view(request):
    return render(request, 'kumbakonam.html')

def masjid_view(request):
    return render(request, 'Kumbakonam_big_Masjid.html')

def kulam_view(request):
    return render(request, 'Mahamaham_Kulam.html')

def cathedral_view(request):
    return render(request, 'St_Mary’s_Cathedral.html')