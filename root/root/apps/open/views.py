from django.shortcuts import render
from .models import SpZakup, SpRyad, PunbbUsers


def Zakup_list(request):
    status = 3                                              # Статус закупок
    orgId = 3 #615
    limit = 15                                              # Лимит закупок на странице

    """Все закупки с органичением по количеству"""
    # ZakupList = SpZakup.objects.all()[0:limit]

    """Закупки конкретных оргов с ограничением по количеству и сортировкой"""
    ZakupList = SpZakup.objects.filter(status=status).order_by('-id')[0:limit]
    RealName = PunbbUsers.objects.get(id=orgId)
    # RealName = PunbbUsers.objects.all().select_related(ZakupList.user)

    return render(request, 'open/index.html', context={'Zakup_names': ZakupList, 'RealName': RealName})


def zakup_detail(request, id):
    all_ryads = SpRyad.objects.filter(id_zp=id)

    return render(request, 'open/zakup_detail.html', context={'all_ryad_list': all_ryads})


def row_detail(request, id):
    row = SpRyad.objects.get(id=id)
    return render(request, 'open/row_detail.html', context={'current_row': row})


