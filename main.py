from SRC.funcoes import metadado, registra
from time import sleep


def mescla_dados():
    """
    Mescla 2 metadados em formatato f_string e transforma em um metadado maior contendo as informações cenralisadas num
    único metadado registrando e retornando-o.

    :return: meta02
    """

    # Indica se o uso de memória esta num nível seguro ou não e a porcentagem:
    meta01 = '[Indicador + X%]'

    # Mescla 2 metadados em um:
    meta02 = metadado(f'Uso de memória {meta01}', 'INFO')

    # Registra o metadado:
    registra(meta02)

    return meta02


def painel_log():
    """
    Exibe um cabecalho inicial seguido de uma string que se atualiza em looping contendo os dados [data e hora] situação,
    Uso de memória + porcentagem.
    :return:
    """

    # Cabecalho:
    cabecalho = metadado('Sistema de monitoramento iniciado', 'INFO')
    print(cabecalho)

    # Looping:
    while True:
        print(mescla_dados())
        sleep(1)


if __name__ == "__main__":
    painel_log()