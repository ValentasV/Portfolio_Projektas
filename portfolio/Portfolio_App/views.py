from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, CreateView
from .models import Profilis, Projektas

#  render -

# request -

# FormMixin -

# formView -

# LoginRequiredMixin - informacija bus matoma tik prisijungusiems vartotojams

# isowner -


class ProfilisIrProjektasView(View):
    def get(self, request):
        profilis = Profilis.objects.all()
        projektas = Projektas.objects.all()
        return render(request, 'Portfolio_App/index.html', {'profilis': profilis, 'projektas': projektas})

# ALTERNATYVA

# def ProfilisIrProjektai(request):
#     profilis = Profilis.objects.all().values()
#     projektas = Projektas.objects.all().values()
#     template = loader.get_template('Portfolio_App/index.html')
#     context = {
#         'profilis': profilis,
#         'projektas': projektas,
#   }
#     return HttpResponse(template.render(context, request))



class ProjektasListView(ListView):
    model = Projektas
    context_object_name = "projektas"
    paginate_by = 1
    template_name = 'projektas_list.html'


class CreateProjektasView(LoginRequiredMixin, CreateView):
    model = Projektas
    fields = [ "iliustracija", "pavadinimas", "aprasymas", "technologiju_sarasas", "projekto_svetaine", "githubo_nuoroda" ]
    success_url = '/Portfolio_App/profiliai/'


# Naudotojo sukūrimas tik prisijunges naudotojas gali pildyti formą.
    def form_valid(self, form):
        naudotojo_profilis = Profilis.objects.get(naudotojas=self.request.user)
        form.instance.naudotojas = naudotojo_profilis
        return super().form_valid(form)


# class ProjektasListView(ListView):
#     def get(self, request):
#         projektas = Projektas.objects.all()
#         return render(request, 'Portfolio_App/projektas_list.html', {'projektas': projektas})

