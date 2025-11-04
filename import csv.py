import csv
from collections import Counter, defaultdict

def ler_logs(firewall_log):
    logs = []
    with open(firewall_log, 'r') as f:
        reader = csv.reader(f)
        for linha in reader:
            if len(linha) == 6:
                log = {
                    'timestamp': linha[0],
                    'ip_origem': linha[1],
                    'ip_destino': linha[2],
                    'porta': linha[3],
                    'protocolo': linha[4],
                    'acao': linha[5]
                }
                logs.append(log)
    return logs

def gerar_relatorio(logs):
    conexoes_por_ip = Counter(log['ip_origem'] for log in logs)
    acoes = Counter(log['acao'] for log in logs)
    portas = Counter(log['porta'] for log in logs)
    protocolos = Counter(log['protocolo'] for log in logs)
    
    tentativas_negadas = defaultdict(int)
    for log in logs:
        if log['acao'].upper() == 'DENY':
            tentativas_negadas[log['ip_origem']] += 1
    ips_suspeitos = [ip for ip, qtd in tentativas_negadas.items() if qtd > 5]
    
    print("\n===== RELATÓRIO DE SEGURANÇA =====")
    print(f"Total de registros: {len(logs)}")
    print("\nAções:")
    for acao, qtd in acoes.items():
        print(f"  {acao}: {qtd}")
    print("\nTop 5 IPs de origem:")
    for ip, qtd in conexoes_por_ip.most_common(5):
        print(f"  {ip}: {qtd} conexões")
    print("\nPortas mais acessadas:")
    for porta, qtd in portas.most_common(5):
        print(f"  Porta {porta}: {qtd} vezes")
    print("\nProtocolos mais usados:")
    for proto, qtd in protocolos.most_common():
        print(f"  {proto}: {qtd}")
    print("\nIPs suspeitos (múltiplas negações):")
    if ips_suspeitos:
        for ip in ips_suspeitos:
            print(f"  {ip}")
    else:
        print("  Nenhum IP suspeito detectado.")


if __name__ == "__main__":
    arquivo = "firewall_log.txt"
    logs = ler_logs(arquivo)
    gerar_relatorio(logs)