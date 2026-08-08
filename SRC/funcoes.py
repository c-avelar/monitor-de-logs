from datetime import datetime


def metadado(mensagem='Mensagem de aviso', classificacao='INFO'):
    """
    Função "metadado()" recebe como argumento uma "mensagem" e "classificação de risco" e devolve uma f_string
    f"[data e hora] [classificação] mensagem".
    :param mensagem:
    :param classificacao:
    :return: f"[data e hora] [classificação] mensagem"
    """

    agora = datetime.now()

    data = agora.strftime("%d/%m/%Y")
    hora = agora.strftime("%H:%M:%S")
    periodo = f'{data} {hora}'

    return f'[{periodo}] [{classificacao}] - {mensagem}'


# recebe como argumento uma string e registra num documento .txt cada vêz que é executado.
def registra(string_metadado='___ERRO!__'):
    """
    Recebe uma string qualquer como argumento e a registra no documento "historico_log.txt" e retorna
    :param: string_metadado
    :return: None
    """
    with open("historico_log.txt", 'a', encoding="utf-8") as arquivo:
        arquivo.write(string_metadado + '\n')

    return None
