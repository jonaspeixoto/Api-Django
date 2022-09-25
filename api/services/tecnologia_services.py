from ..models import Tecnologia


def lista_tecnologia():
    tecnologias = Tecnologia.objects.all()
    return tecnologias


def cadatrar_tecnologia(teclonogia):
    Tecnologia.objects.create(nome=teclonogia.nome)
