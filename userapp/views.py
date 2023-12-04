from rest_framework import viewsets


from .models import ProfissionalDeSaude, Vacina, ProfissionalSaudeEUSF, UnidadeSaudeFamiliar, HistoricoDeVacinas, Cuidador, CuidadorCrianca, Crianca, CrescimentoCrianca, Agendamento, Endereco, Consulta, Medico, CriancaVacina, Desenvolvimento, SinaisAlerta, CuidadosEspeciais, Aleitamento, LeiteArtificial, Aplicacao, ExameOcular, CuidadosEspeciais,DesenvolvimentoInfantil

from .serializers import ProfissionalDeSaudeSerializer, VacinaSerializer, ProfissionalSaudeEUSFSerializer, UnidadeSaudeFamiliarSerializer, HistoricoDeVacinasSerializer, CuidadorSerializer, CuidadorCriancaSerializer, CriancaSerializer, CrescimentoCriancaSerializer, AgendamentoSerializer, EnderecoSerializer, ConsultaSerializer, MedicoSerializer, CriancaVacinaSerializer, DesenvolvimentoSerializer, SinaisAlertaSerializer, CuidadosEspeciaisSerializer, AleitamentoSerializer, LeiteArtificialSerializer, AplicacaoSerializer, ExameOcularSerializer, CuidadosEspeciaisSerializer, DesenvolvimentoInfantilSerializer




class CrescimentoCriancaViewset(viewsets.ModelViewSet):
    queryset = CrescimentoCrianca.objects.all()
    serializer_class = CrescimentoCriancaSerializer

class AleitamentoViewset(viewsets.ModelViewSet):
    queryset = Aleitamento.objects.all()
    serializer_class = AleitamentoSerializer

class LeiteArtificialViewset(viewsets.ModelViewSet):
    queryset = LeiteArtificial.objects.all()
    serializer_class = LeiteArtificialSerializer

class DesenvolvimentoViewset(viewsets.ModelViewSet):
    queryset = Desenvolvimento.objects.all()
    serializer_class = DesenvolvimentoSerializer

class SinaisAlertaViewset(viewsets.ModelViewSet):
    queryset = SinaisAlerta.objects.all()
    serializer_class = SinaisAlertaSerializer

class CuidadosEspeciaisViewset(viewsets.ModelViewSet):
    queryset = CuidadosEspeciais.objects.all()
    serializer_class = CuidadosEspeciaisSerializer

class CriancaViewset(viewsets.ModelViewSet):
    queryset = Crianca.objects.all()
    serializer_class = CriancaSerializer

class CuidadorViewset(viewsets.ModelViewSet):
    queryset = Cuidador.objects.all()
    serializer_class = CuidadorSerializer

class CuidadorCriancaViewset(viewsets.ModelViewSet):
    queryset = CuidadorCrianca.objects.all()
    serializer_class = CuidadorCriancaSerializer

class EnderecoViewSet(viewsets.ModelViewSet):
    queryset = Endereco.objects.all()
    serializer_class = EnderecoSerializer

class ProfissionalDeSaudeViewSet(viewsets.ModelViewSet):
    queryset = ProfissionalDeSaude.objects.all()
    serializer_class = ProfissionalDeSaudeSerializer

class UnidadeSaudeFamiliarViewset(viewsets.ModelViewSet):
    queryset = UnidadeSaudeFamiliar.objects.all()
    serializer_class = UnidadeSaudeFamiliarSerializer

class ProfissionalSaudeEUSFViewset(viewsets.ModelViewSet):
    queryset = ProfissionalSaudeEUSF.objects.all()
    serializer_class = ProfissionalSaudeEUSFSerializer

class MedicoViewSet(viewsets.ModelViewSet):
    queryset = Medico.objects.all()
    serializer_class = MedicoSerializer

class ConsultaViewSet(viewsets.ModelViewSet):
    queryset = Consulta.objects.all()
    serializer_class = ConsultaSerializer

class AgendamentoViewSet(viewsets.ModelViewSet):
    queryset = Agendamento.objects.all()
    serializer_class = AgendamentoSerializer

class VacinaViewSet(viewsets.ModelViewSet):
    queryset = Vacina.objects.all()
    serializer_class = VacinaSerializer

class HistoricoDeVacinasViewset(viewsets.ModelViewSet):
    queryset = HistoricoDeVacinas.objects.all()
    serializer_class = HistoricoDeVacinasSerializer

class CriancaVacinaViewSet(viewsets.ModelViewSet):
    queryset = CriancaVacina.objects.all()
    serializer_class = CriancaVacinaSerializer

class AplicacaoViewSet(viewsets.ModelViewSet):
    queryset = Aplicacao.objects.all()
    serializer_class = AplicacaoSerializer

class ExameOcularViewSet(viewsets.ModelViewSet):
    queryset = ExameOcular.objects.all()
    serializer_class = ExameOcularSerializer

class CuidadosEspeciaisViewSet(viewsets.ModelViewSet):
    queryset = CuidadosEspeciais.objects.all()
    serializer_class = CuidadosEspeciaisSerializer

class CriancaViewSet(viewsets.ModelViewSet):
    queryset = Crianca.objects.all()
    serializer_class = CriancaSerializer

class DesenvolvimentoInfantilViewSet(viewsets.ModelViewSet):
    queryset = DesenvolvimentoInfantil.objects.all()
    serializer_class = DesenvolvimentoInfantilSerializer