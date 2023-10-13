from django.core.mail import send_mail
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from .filters import ResponseFilter
from .forms import AddAdForm, AddAdResponse
from .models import AdResponses, Ads

from django.views.generic import ListView,  DetailView, DeleteView

class AdsList(ListView):
    model = Ads
    template_name = 'index.html'
    context_object_name = 'ads'
    queryset = model.objects.order_by('-create_date')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['response'] = AdResponses.objects.all().count()
        context['title'] = 'Главная страница'
        return context

    def get_queryset(self):
        return Ads.objects.order_by('-create_date').select_related('user_id')

class AdResponseSearch(LoginRequiredMixin, ListView):
    model = AdResponses
    template_name = 'cabinet/ads.html'
    context_object_name = 'response'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = ResponseFilter(self.request.GET, queryset=self.get_queryset())
        return context
    
def add_ad(request):
    if request.method == 'POST':
            form = AddAdForm(request.POST, request.FILES)
            if form.is_valid():
                user = request.user
                Ads.objects.create(**form.cleaned_data, user_id_id=user.id)
                return redirect('general')
    else:
        form = AddAdForm()
    return render(request, 'cabinet/add_ad.html', {'form': form, 'title': 'Добавление объявления'})


class Ad(DetailView):
    model = Ads
    template_name = 'ad/index.html'
    context_object_name = 'ad'


def add_response(request):
    id = request.GET.get("id")
    ad = Ads.objects.get(ad_id=id)
    if request.method == 'POST':
        id = request.GET.get("id")
        ad = Ads.objects.get(ad_id=id)
        form = AddAdResponse(request.POST)
        if form.is_valid():
            user = request.user
            AdResponses.objects.create(**form.cleaned_data, user_id_id=user.pk, ad_id_id=id)
            return redirect('general')
    else:
        form = AddAdResponse()
    return render(request, 'response/add.html', {'form': form, 'title': "Комментарий", 'ad': ad})


class ResponseDeleteView(DeleteView):
    template_name = 'response/delete.html'
    queryset = AdResponses.objects.all()
    success_url = '/ads/cabinet/'

def submit_response(request):
    response_id = request.GET.get("resp")
    mail_to = AdResponses.objects.get(pk=response_id).user_id.email
    send_mail(
        'Увеомление сайта объявлений',
        'Спасибо, что откликнулись! Ваш отклик принят.',
        'testpochta@mail.ru',
        [f'{mail_to}']
    )
    return redirect('cabinet')