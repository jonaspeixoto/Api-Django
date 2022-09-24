from ..models import Tecnologia


def lista_tecnologia():
    tecnologias = Tecnologia.objects.all()
    return tecnologias
