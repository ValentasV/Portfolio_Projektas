from django.db import models

# Create your models here.


class Profilis(models.Model):
    vardas = models.CharField(max_length=100)
    pavarde = models.CharField(max_length=100)
    trumpas_prisistatymas = models.TextField()
    logotipas = models.ImageField(upload_to='logotipai/', blank= True, null= True)
    socialinis_tinklas_linkedin = models.URLField(blank=True)
    socialinis_tinklas_github = models.URLField(blank=True)

    class Meta:
        # kad rodytų tvarkingus lietuviškus pavadinimus
        verbose_name = "Profilis"
        verbose_name_plural = "Profiliai"

    def __str__(self):
        return f"{self.vardas} {self.pavarde}"

class Projektas(models.Model):
    iliustracija = models.ImageField(upload_to="projektas", null=True, blank=True)
    pavadinimas = models.CharField(max_length=100)
    aprasymas = models.TextField()
    technologiju_sarasas = models.TextField(max_length=120)
    projekto_svetaine = models.URLField(blank=True)
    githubo_nuoroda = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)


    class Meta:
        # kad rodytų tvarkingus lietuviškus pavadinimus
        verbose_name = "Projektas"
        verbose_name_plural = "Projektai"

    def __str__(self):
        return f"{self.iliustracija} {self.pavadinimas}"