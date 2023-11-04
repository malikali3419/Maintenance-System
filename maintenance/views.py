from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
from django.views import View
from .models import Land,Stadt,Andrede,Records,Company

User = get_user_model()

class DashboardView(LoginRequiredMixin, View):
    template_name = 'maintenance/dashboard.html'
    def get(self, request):
        context = {}
        context['land'] = Land.objects.all()
        context['andrede'] = Andrede.objects.all()
        context['stadt'] = Stadt.objects.all()
        context['company'] = Company.objects.first()
        context['records'] = Records.objects.all()
        return render(request, self.template_name,context)
    def post(self,request):
        andrede = request.POST.get('anrede')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        company_name = request.POST.get('company_name')
        email = request.POST.get('email')
        news_accept = request.POST.get('news_accept')
        telefone = request.POST.get('telefone')
        starBe = request.POST.get('StarBe')
        nr = request.POST.get('nr')
        postal_code = request.POST.get('postal_code')
        stadt = request.POST.get('Stadt')
        land = request.POST.get('land')
        birthdate = request.POST.get('birthdate')
        uid_number = request.POST.get('uid_number')
        ammerkung = request.POST.get('ammerkung')
        record = Records(
            andrede_name=Andrede.objects.filter(id=andrede).first(),
            first_name=first_name,
            last_name=last_name,
            company_name=company_name,
            email=email,
            news_accept=True if news_accept == "on" else False,
            telefone=telefone,
            starBe=starBe,
            nr=nr,
            postal_code=postal_code,
            stadt_name=Stadt.objects.filter(id=stadt).first(),
            land_name=Land.objects.filter(id=land).first(),
            birthdate=birthdate,
            uid_number=uid_number,
            ammerkung=ammerkung
        )
        record.save()
        return redirect('/')
