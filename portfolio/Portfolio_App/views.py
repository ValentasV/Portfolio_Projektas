from django.shortcuts import render
from django.views import View
from django.views.generic import ListView
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



# class ProjektasListView(ListView):
#     def get(self, request):
#         projektas = Projektas.objects.all()
#         return render(request, 'Portfolio_App/projektas_list.html', {'projektas': projektas})











# class ProjektasDetailView(DetailView):
#     model = Projektas
#     context_object_name = "projektas"
#
#     def post(self, request, pk):
#         iliustracija = request.POST.get('paveikslėlis')
#         pavadinimas = request.POST.get('projekto pavadinimas')
#         aprašymas = request.POST.get('informacija apie projektą')
#         technologiju_sarasas = request.POST.get('naudojamos technologijos')
#         projekto_svetaine = request.POST.get('svetaines adresas')
#         githubo_nuoroda = request.POST.get('githubo nuoroda')
#
#         if pavadinimas.isnumeric():
#             messages.error(request, "Skaičių vesti negalima")
#             return redirect(f"/Portfolio_App/{pk}")
#         if len(technologiju_sarasas) == 0:
#             messages.error(request, "Technologijų sąrašas turi būti užpildytas")
#             return redirect(f"/events/{pk}")
#         projektas = get_object_or_404(Projektas, pk=pk)
#
#
#
