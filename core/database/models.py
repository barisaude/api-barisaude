from django.db import models
from django.db.models import DecimalField

# Create your models here.

class Medico(models.Model):
    medico_id = models.AutoField(primary_key=True)
    medico_nome = models.CharField(max_length=20, blank=True, null=True)
    medico_crm = models.CharField(max_length=20, blank=True, null=True)
    medico_telefone: DecimalField = models.DecimalField(max_digits=11, decimal_places=0, blank=True, null=True)
    medico_endereco = models.CharField(max_length=100, blank=True, null=True)
    medico_cidade = models.CharField(max_length=100, blank=True, null=True)
    medico_estado = models.CharField(max_length=2, blank=True, null=True)
    medico_especialidade = models.CharField(max_length=100, blank=True, null=True)


class Paciente(models.Model):
    paciente_id = models.AutoField(primary_key=True)
    paciente_nome = models.CharField(max_length=100, blank=True, null=True)
    paciente_cpf = models.CharField(max_length=11, blank=True, null=True)
    paciente_rg = models.CharField(max_length=11, blank=True, null=True)
    paciente_telefone = models.DecimalField(max_digits=11, decimal_places=0, blank=True, null=True)
    paciente_endereco = models.CharField(max_length=100, blank=True, null=True)
    paciente_bairro = models.CharField(max_length=100, blank=True, null=True)
    paciente_cidade = models.CharField(max_length=100, blank=True, null=True)
    paciente_peso = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    paciente_altura = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)



class Medicacao(models.Model):
    paciente = models.OneToOneField('Paciente', on_delete=models.CASCADE, primary_key=True)
    medicacao_tipo = models.CharField(max_length=100, blank=True, null=True)
    medicacao_descricao = models.TextField(blank=True, null=True)
    medicacao_data_inicio = models.DateField()
    medicacao_data_fim = models.DateField(blank=True, null=True)



class HistoricoPaciente(models.Model):
    historico_paciente_id = models.AutoField(primary_key=True)
    historico_paciente_dados = models.JSONField()
    historico_paciente_paciente = models.ForeignKey('Paciente', on_delete=models.CASCADE)



class Especialidade(models.Model):
    especialidade_medico = models.OneToOneField('Medico', on_delete=models.CASCADE, primary_key=True)
    especialidade_medico_crm = models.CharField(max_length=20, blank=True, null=True)
    especialidade_tipo = models.CharField(max_length=20, blank=True, null=True)
    especialidade_descricao = models.TextField(blank=True, null=True)


class Dieta(models.Model):
        dieta_paciente = models.OneToOneField('Paciente', on_delete=models.CASCADE, primary_key=True)
        dieta_tipo = models.CharField(max_length=100, blank=True, null=True)
        dieta_descricao = models.TextField(blank=True, null=True)
        dieta_data_inicio = models.DateField()
        dieta_data_fim = models.DateField(blank=True, null=True)



class Agenda(models.Model):
    agenda_medico = models.ForeignKey('Medico', on_delete=models.CASCADE)
    agenda_data_agendamento = models.DateField()
    agenda_hora_agendamento = models.TimeField()
    agenda_paciente = models.ForeignKey('Paciente', on_delete=models.CASCADE)
    agenda_especialidade = models.CharField(max_length=20)
    agenda_observacoes = models.TextField(blank=True, null=True)



class Academia(models.Model):
    academia_id = models.AutoField(primary_key=True)
    academia_endereco = models.CharField(max_length=100, blank=True, null=True)
    academia_telefone = models.DecimalField(max_digits=11, decimal_places=0, blank=True, null=True)
    academia_horario = models.DateField(blank=True, null=True)


class Pagamento(models.Model):
    pagamento_id = models.AutoField(primary_key=True)
    pagamento_pix = models.CharField(max_length=50, blank=True, null=True)
    pagamento_cartao_credito = models.CharField(max_length=50, blank=True, null=True)
    pagamento_cartao_debito = models.CharField(max_length=50, blank=True, null=True)
    pagamento_transferencia = models.CharField(max_length=50, blank=True, null=True)
    pagamento_boleto = models.CharField(max_length=50, blank=True, null=True)
    pagamento_comprovante = models.CharField(max_length=50, blank=True, null=True)
    pagamento_status = models.CharField(max_length=50, blank=True, null=True)


class Receita(models.Model):
    receita_paciente = models.OneToOneField('Paciente', on_delete=models.CASCADE, primary_key=True)
    receita_medicacao = models.CharField(max_length=200, blank=True, null=True)
    receita_descricao = models.TextField(blank=True, null=True)


class Usuario(models.Model):
    usuario_id = models.AutoField(primary_key=True)
    usuario_login = models.CharField(max_length=20, blank=True, null=True)
    usuario_senha = models.CharField(max_length=20, blank=True, null=True)


