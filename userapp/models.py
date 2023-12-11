from django.db import models
from enum import Enum, auto

# Crescimento Crianca

class CrescimentoCrianca(models.Model):
    IDADE_CHOICES = [
        ('primeira semana', 'Primeira semana'),
        ('1 mês', '1 mês'),
        ('2 meses', '2 meses'),
        ('3 meses', '3 meses'),
        ('4 meses', '4 meses'),
        ('5 meses', '5 meses'),
        ('6 meses', '6 meses'),
        ('9 meses', '9 meses'),
        ('12 meses', '12 meses'),
        ('18 meses', '18 meses'),
        ('24 meses', '24 meses'),
        ('36 meses', '36 meses'),
    ]

    idadeCrianca = models.CharField(max_length=15, choices=IDADE_CHOICES, default='Escolha')
    altura = models.FloatField()  # Altura em centímetros
    peso = models.FloatField()  # Peso em quilogramas
    perimetro = models.FloatField()
    imc = models.FloatField(null=True, blank=True)  # Campo para armazenar o IMC

    def calcular_imc(self):
        altura_metros = self.altura / 100  # Converte altura de centímetros para metros
        imc = self.peso / (altura_metros ** 2)
        return round(imc, 2)  # Arredonda o IMC para 2 casas decimais

    def avaliar_medida(self):
        percentis = {
            'primeira semana': (30.7, 34.5, 38.3),
            '1 mês': (33.8, 37.3, 40.8),
            '2 meses': (35.6, 39.1, 42.6),
            '3 meses': (37.0, 40.5, 44.1),
            '4 meses': (38.0, 41.6, 45.2),
            '5 meses': (38.9, 42.6, 46.2),
            '6 meses': (39.7, 43.3, 47.0),
            '9 meses': (40.8, 44.5, 48.3),
            '12 meses': (41.2, 45.0, 48.8),
            '18 meses': (41.9, 45.8, 49.6),
            '24 meses': (42.2, 46.1, 49.9),
            '36 meses': (43.4, 47.4, 51.7),
        }

        percentil_10, mediana, percentil_90 = percentis.get(self.idadeCrianca, (None, None, None))

        if percentil_10 is not None:
            if self.perimetro < percentil_10:
                return 'Abaixo do percentil 10 - Abaixo da média'
            elif percentil_10 <= self.perimetro <= percentil_90:
                return 'Entre os percentis 10 e 90 - Na média'
            else:
                return 'Acima do percentil 90 - Acima da média'
        else:
            return 'Faixa etária não encontrada'

    def save(self, *args, **kwargs):
        self.full_clean()  # Chama a função clean antes de salvar
        self.imc = self.calcular_imc()  # Calcula o IMC antes de salvar
        super(CrescimentoCrianca, self).save(*args, **kwargs)

# Aleitamento

class Aleitamento(models.Model):
    ALEITAMENTO_CHOICES = [
        ('leite materno exclusivo', 'Leite materno exclusivo'),
        ('leite artificials', 'Leite artificial'),
        ('leite materno complementado', 'Leite materno complementado'),
        ]

    aleitamento = models.CharField(max_length=30, choices=ALEITAMENTO_CHOICES, default='Escolha')

# Leite artificial

class LeiteArtificial(models.Model):
    SIMNAO_CHOICES = [
        ('sim', 'Sim'),
        ('não', 'Não')
    ]

    parouAmamentar = models.CharField(max_length=10, choices=SIMNAO_CHOICES, default='nao visualizado')
    idadeParou = models.CharField(max_length=150)
    alimentoCrianca = models.CharField(max_length=150)
    porcoesFrutasDia = models.CharField(max_length=150)
    alimentosIndustrializado = models.CharField(max_length=10, choices=SIMNAO_CHOICES, default='nao visualizado')
    qualAlimentoIndust = models.CharField(max_length=150)

# Desenvolvimento

class Desenvolvimento(models.Model):
    OPCOES_CHOICES = [
        ('presente', 'Presente'),
        ('ausente', 'Ausente'),
        ('nao visualizado', 'Não visualizado')
    ]
    idCrescimentoCrianca = models.ForeignKey(CrescimentoCrianca, on_delete=models.CASCADE)
    brincaEsconde = models.CharField(max_length=15, choices=OPCOES_CHOICES, default='nao visualizado')
    objetosMao = models.CharField(max_length=15, choices=OPCOES_CHOICES, default='nao visualizado')
    duplicaSilaba = models.CharField(max_length=15, choices=OPCOES_CHOICES, default='nao visualizado')
    senta = models.CharField(max_length=15, choices=OPCOES_CHOICES, default='nao visualizado')

# Sinais de alerta

class SinaisAlerta(models.Model):
    SIMNAO_CHOICES = [
        ('sim', 'Sim'),
        ('não', 'Não')
    ]
    diarreia =  models.CharField(max_length=10, choices=SIMNAO_CHOICES, default='nao visualizado')
    vomitos =  models.CharField(max_length=10, choices=SIMNAO_CHOICES, default='nao visualizado')
    dificuldadeRespirar =  models.CharField(max_length=10, choices=SIMNAO_CHOICES, default='nao visualizado')
    febre =  models.CharField(max_length=10, choices=SIMNAO_CHOICES, default='nao visualizado')
    hipotermia =  models.CharField(max_length=10, choices=SIMNAO_CHOICES, default='nao visualizado')
    sibilancias =  models.CharField(max_length=10, choices=SIMNAO_CHOICES, default='nao visualizado')
    convulcoes =  models.CharField(max_length=10, choices=SIMNAO_CHOICES, default='nao visualizado')

# Cuidados especiais

class CuidadosEspeciais(models.Model):
    SIMNAO_CHOICES = [
        ('sim', 'Sim'),
        ('não', 'Não')
    ]
    ferro =  models.CharField(max_length=10, choices=SIMNAO_CHOICES, default='nao visualizado')
    micronutrientes =  models.CharField(max_length=10, choices=SIMNAO_CHOICES, default='nao visualizado')
    vitaminaA =  models.CharField(max_length=10, choices=SIMNAO_CHOICES, default='nao visualizado')
    odonto =  models.CharField(max_length=10, choices=SIMNAO_CHOICES, default='nao visualizado')
    acidentesDomesticos =  models.CharField(max_length=10, choices=SIMNAO_CHOICES, default='nao visualizado')
    negligencias =  models.CharField(max_length=10, choices=SIMNAO_CHOICES, default='nao visualizado')

# Criança

class Crianca(models.Model):
    nomeDaCrianca = models.CharField(max_length=150)
    cpf = models.CharField(max_length=14)
    dataDeNascimento = models.DateField()
    nomeDaMae = models.CharField(max_length=150)
    cpfDaMae = models.CharField(max_length=14)
    dataNascimentoMae = models.DateField()
    unidadeSaudeFamiliar = models.CharField(max_length=150)
    maternidade = models.CharField(max_length=150)
    tipoDoParto = models.CharField(max_length=150)
    idadeGestacional = models.CharField(max_length=150)

# Cuidador

class Cuidador(models.Model):
    nome = models.CharField(max_length=150)
    grauDeParentesco = models.CharField(max_length=150)
    email = models.CharField(max_length=150)
    telefone = models.CharField(max_length=11, unique=True)

# Cuidador Criança

class CuidadorCrianca(models.Model):
    idCuidador = models.ForeignKey(Cuidador, on_delete=models.CASCADE)
    idCrianca = models.ForeignKey(Crianca, on_delete=models.CASCADE)
    criadoEmDiaMesAno = models.DateField()
    
# Endereço

class Endereco(models.Model):
    logradouro = models.CharField(max_length=100)
    cep = models.CharField(max_length=9)
    numero = models.CharField(max_length=100)
    estado = models.CharField(max_length=50)
    municipio = models.CharField(max_length=20)
    complemento = models.CharField(max_length=100)
    

# Profissional de Saude

class ProfissionalDeSaude(models.Model):
    nome = models.CharField(max_length=150)
    cpf = models.CharField(max_length=14, unique=True)
    email = models.CharField(max_length=150)
    senha = models.CharField(max_length=150)
    telefone = models.CharField(max_length=11, unique=True)
    tipoProfissional = models.CharField(max_length=150)
    conselho = models.CharField(max_length=150)

    # def __str__(self):
    #     return self.nome

    
# Unidade Saude Familiar

class UnidadeSaudeFamiliar(models.Model):
    idCuidador = models.ForeignKey(Cuidador, on_delete=models.CASCADE)
    idCrianca = models.ForeignKey(Crianca, on_delete=models.CASCADE)
    idProfissionalDeSaude = models.ForeignKey(ProfissionalDeSaude, on_delete=models.CASCADE)
    idEndereco = models.ForeignKey(Endereco, on_delete=models.CASCADE)
    criadoEmDiaMesAno = models.DateField()

# ProfissionalSaudeEUSF

class ProfissionalSaudeEUSF(models.Model):
    idUSF = models.ForeignKey(UnidadeSaudeFamiliar, on_delete=models.CASCADE)
    idProfissionalDeSaude = models.ForeignKey(ProfissionalDeSaude, on_delete=models.CASCADE)
    criadoEmDiaMesAno = models.DateField()
    
# Médico

class Medico(models.Model):
    NomeDoMedico = models.CharField(max_length=100)
    Conselho = models.CharField(max_length=100)
    Escilidade = models.CharField(max_length=100)
    NumeroDeInscricao = models.CharField(max_length=100)
    Email = models.CharField(max_length=100)
    Telefone =  models.CharField(max_length=11)

# Consulta

class Consulta (models.Model):
    TIPO_CHOICES = [
        ('particular', 'Particular'),
        ('sus', 'SUS'),
    ]

    idMedico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    dataConsulta = models.DateField()
    idEndereco = models.ForeignKey(Endereco, on_delete=models.CASCADE)
    tipoDaConsulta = models.CharField(max_length=10, choices=TIPO_CHOICES, default='sus')
    
# Agendamento

class Agendamento(models.Model):
    horaDaVacinacao = models.TimeField()
    dataDaVacinacao = models.DateField()

# Vacina

class Vacina(models.Model):
    tipoVacina = models.CharField(max_length=150)
    lote = models.CharField(max_length=150)
    fabricante = models.CharField(max_length=150)
    dataFabricacao = models.DateField()

# Historico de Vacinas

class HistoricoDeVacinas(models.Model):
    idVacina = models.ForeignKey(Vacina, on_delete=models.CASCADE)
    idAgendamento = models.ForeignKey(Agendamento, on_delete=models.CASCADE)
    criadoEmDiaMesAno = models.DateField()

# Criança Vacina

class CriancaVacina(models.Model):
    idVacina = models.ForeignKey(Vacina, on_delete=models.CASCADE)
    idCrianca = models.ForeignKey(Crianca, on_delete=models.CASCADE)
    criadoEmDiaMesAno = models.DateField()


class Aplicacao(models.Model):
    STATUS_CHOICES = [
        ('atrasado', 'Atrasado'),
        ('agendado', 'Agendado'),
    ]
    idVacina = models.ForeignKey(Vacina, on_delete=models.CASCADE)
    idAgendamento = models.ForeignKey(Agendamento, on_delete=models.CASCADE)
    profissional = models.ForeignKey(ProfissionalDeSaude, related_name='vacinas', on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='agendado')

#Exame ocular

class ExameOcular(models.Model):
    class TamanhoOcular(models.TextChoices):
        NORMAL = 'normal', 'Normal'
        ANORMAL = 'anormal', 'Anormal'

    globo_ocular = models.CharField(
        max_length=10,
        choices=TamanhoOcular.choices,
        default=TamanhoOcular.NORMAL,
    )

    class Pupilas(models.TextChoices):
        NORMAL = 'normal', 'Normal'
        ANORMAL = 'anormal', 'Anormal'

    pupilas = models.CharField(
        max_length=10,
        choices=Pupilas.choices,
        default=Pupilas.NORMAL,
    )

    class Estrabismo(models.TextChoices):
        NAO = 'nao', 'Não'
        SIM = 'sim', 'Sim'

    estrabismo = models.CharField(
        max_length=5,
        choices=Estrabismo.choices,
        default=Estrabismo.NAO,
    )

    class SecrecaoOcular(models.TextChoices):
        NAO = 'nao', 'Não'
        SIM = 'sim', 'Sim'

    secrecao_ocular = models.CharField(
        max_length=5,
        choices=SecrecaoOcular.choices,
        default=SecrecaoOcular.NAO,
    )

class PosicaoSono(Enum):
    NAO = auto()
    SIM = auto()

class FuncionamentoIntestino(Enum):
    PRESERVADO = auto()
    NAO_PRESERVADO = auto()

class HigieneCuidadosGerais(Enum):
    PRESERVADO = auto()
    NAO_PRESERVADO = auto()

class SinaisViolencias(Enum):
    PRESENTE = auto()
    AUSENTE = auto()

class AcidentesDomiciliares(Enum):
    NAO = auto()
    SIM = auto()

class CuidadosEspeciais(models.Model):
    tempo_sono_24_horas = models.CharField(max_length=255, blank=True, null=True)
    posicao_sono_berco = models.CharField(max_length=50, choices=[(tag.name, tag.name.replace('_', ' ')) for tag in PosicaoSono], default=PosicaoSono.NAO.name)
    funcionamento_intestino_colicas = models.CharField(max_length=50, choices=[(tag.name, tag.name.replace('_', ' ')) for tag in FuncionamentoIntestino], default=FuncionamentoIntestino.PRESERVADO.name)
    higiene_cuidados_gerais = models.CharField(max_length=50, choices=[(tag.name, tag.name.replace('_', ' ')) for tag in HigieneCuidadosGerais], default=HigieneCuidadosGerais.PRESERVADO.name)
    sinais_violencias_negligencias = models.CharField(max_length=50, choices=[(tag.name, tag.name.replace('_', ' ')) for tag in SinaisViolencias], default=SinaisViolencias.AUSENTE.name)
    acidentes_domiciliares = models.CharField(max_length=50, choices=[(tag.name, tag.name.replace('_', ' ')) for tag in AcidentesDomiciliares], default=AcidentesDomiciliares.NAO.name)

    
class DesenvolvimentoInfantil(models.Model):
    MORO_REFLEX_CHOICES = [
        ('P', 'Presente'),
        ('A', 'Ausente'),
        ('NV', 'Não Verificado'),
    ]

    crianca = models.ForeignKey(Crianca, on_delete=models.CASCADE)
    reflexo_moro = models.CharField(max_length=2, choices=MORO_REFLEX_CHOICES, blank=True)
    reflexo_cocleo_palpebral = models.CharField(max_length=2, choices=MORO_REFLEX_CHOICES, blank=True)
    reflexo_succao = models.CharField(max_length=2, choices=MORO_REFLEX_CHOICES, blank=True)
    bracos_pernas_flexionados = models.CharField(max_length=2, choices=MORO_REFLEX_CHOICES, blank=True)
    postura_cabeca_lateralizada = models.CharField(max_length=2, choices=MORO_REFLEX_CHOICES, blank=True)
    observa_rosto = models.CharField(max_length=2, choices=MORO_REFLEX_CHOICES, blank=True)
    reage_som = models.CharField(max_length=2, choices=MORO_REFLEX_CHOICES, blank=True)
    eleva_cabeca = models.CharField(max_length=2, choices=MORO_REFLEX_CHOICES, blank=True)

    def __str__(self):
        return f"Desenvolvimento Infantil - {self.crianca} - {self.pk}"