from datetime import datetime, timedelta

def imprimir_datas_dia_semana(ano, mes, dia_semana_nome):
    dias_semana = {
        'segunda': 0,
        'terca': 1,
        'terça': 1,
        'quarta': 2,
        'quinta': 3,
        'sexta': 4,
        'sabado': 5,
        'sábado': 5,
        'domingo': 6
    }
    
    dia_semana = dias_semana.get(dia_semana_nome.lower())
    if dia_semana is None:
        print("Dia da semana inválido.")
        return
    
    data = datetime(ano, mes, 1)
    datas = []

    while data.month == mes:
        if data.weekday() == dia_semana:
            datas.append(data.strftime('%d/%m/%Y'))
        data += timedelta(days=1)
    
    print(f"Datas dos {dia_semana_nome}s em {mes:02d}/{ano}:")
    for d in datas:
        print(d)

imprimir_datas_dia_semana(1952, 8, 'domingo')