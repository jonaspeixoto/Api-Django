from rest_framework import serializers
from ..models import Vaga


class VagaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vaga
        field = ('titulo', 'descricao', 'salario', 'local', 'quantidade', 'contato',
                 'tipo_contratacao', 'tecnologias')


