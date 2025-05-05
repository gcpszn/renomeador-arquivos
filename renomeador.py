import os  # Módulo para interagir com o sistema operacional

# Solicita o caminho da pasta onde estão os arquivos
caminho_pasta = input('Digite o caminho da pasta: ').strip()

# Verifica se o caminho informado existe
if os.path.exists(caminho_pasta):
    lista_arquivos = os.listdir(caminho_pasta)  # Lista todos os arquivos da pasta
    print(f'\nForam encontrados {len(lista_arquivos)} arquivos.\n')

    # Solicita o nome base que será usado nos novos arquivos
    nome_base = input('Digite o nome base para os arquivos: ').strip()

    contador = 1  # Inicia contador para numerar os arquivos
    for nome_arquivo in lista_arquivos:
        caminho_antigo = os.path.join(caminho_pasta, nome_arquivo)  # Caminho do arquivo

        if os.path.isfile(caminho_antigo):  # Verifica se é um arquivo (ignora pastas)
            extensao = os.path.splitext(nome_arquivo)[1]  # Separa a extensão do arquivo

            # Monta o novo nome com base no contador
            nome_novo = f'{nome_base}_{contador}{extensao}'
            caminho_novo = os.path.join(caminho_pasta, nome_novo)  # Novo caminho com o nome alterado

            os.rename(caminho_antigo, caminho_novo)  # Renomeia o arquivo
            print(f'Renomeado: {nome_arquivo} → {nome_novo}')
            contador += 1  # Incrementa o contador para o próximo arquivo

    print('\n\033[92m✅ Processo concluído com sucesso!\033[0m')
else:
    print('\033[91m❌ Caminho inválido.\033[0m')
