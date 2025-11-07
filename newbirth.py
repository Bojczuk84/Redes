from datetime import datetime, date, timedelta

hoje = input("Digite sua data de hoje (dd/mm/aaaa): ")

agora = datetime.strptime(hoje, "%d/%m/%Y").date()

dia = date.today()


proximo_aniversario = date(dia.year )

if proximo_aniversario < dia:
    proximo_aniversario = date(dia.year)

diferenca = proximo_aniversario - dia 

print(f"Faltam {diferenca.days} dias para o seu próximo aniversário!")