from .models import Empresa

def empresa_context(request):
    empresa = Empresa.objects.first()  # Supondo que há apenas uma empresa cadastrada
    return {'empresa': empresa}