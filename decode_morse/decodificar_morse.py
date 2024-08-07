import os
import datetime
import pandas as pd
from credentials import dict_morse, file_path

def decodificar_morse(mensagem, dict_morse):
    lista_mensagem = mensagem.split(" ") # separa a mensagem em uma lista
    mensagem_decodificada = []
    for letra in lista_mensagem:
        if letra in dict_morse:
            valor_morse = dict_morse[letra]
            if isinstance(valor_morse, int):
                valor_morse = str(valor_morse)  # converte variavel letra para string se for inteiro
            mensagem_decodificada.append(valor_morse)
    return "".join(mensagem_decodificada)

def salva_mensagem_csv(caminho_arquivo, mensagem, dict_morse):
    data_atual = datetime.datetime.now()
    mensagem_decodificada = decodificar_morse(mensagem, dict_morse)
    df = pd.DataFrame([[mensagem_decodificada, data_atual]], columns=['Mensagem','Data'])
    if not os.path.exists(caminho_arquivo):
        hdr = True
    else:
        hdr = False
    df.to_csv(caminho_arquivo, mode='a', index=False, header=hdr)

def main():
    print('Executando Programa...')
    mensagem = input('Informe a mensagem para ser decodificada: ')
    print('Decodificando sua mensagem...')
    salva_mensagem_csv(file_path, mensagem, dict_morse)
    print(f"""Mensagem decodificada: {decodificar_morse(mensagem, dict_morse)}
    Texto adicionado no arquivo: {file_path}
    Caminho: {os.path.abspath(file_path)}""")

if __name__ == "__main__":
    main()