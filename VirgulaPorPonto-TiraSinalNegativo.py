import os
import fileinput
import glob
import shutil

# Obter o caminho absoluto da pasta onde o arquivo Python está localizado
folder_path = os.path.abspath(".")

# Obter uma lista de todos os arquivos de texto na pasta
txt_files = glob.glob(os.path.join(folder_path, "*.txt"))

# Para cada arquivo de texto na lista
for txt_file in txt_files:
    # Obter o nome do arquivo sem o caminho completo
    filename = os.path.basename(txt_file)
    
    # Criar o nome do arquivo de cópia adicionando "_copy" antes da extensão
    copy_filename = os.path.splitext(filename)[0] + "_copiaDeletavel" + os.path.splitext(filename)[1]
    
    # Copiar o arquivo para o nome de cópia
    shutil.copy(txt_file, os.path.join(folder_path, copy_filename))
    
    # Abrir o arquivo original em modo de leitura e escrita
    with fileinput.FileInput(txt_file, inplace=True) as file:
        # Abrir o arquivo de cópia em modo de leitura
        with open(os.path.join(folder_path, copy_filename), "r") as copy_file:
            # Para cada linha no arquivo
            for line in file:
                # Substituir o sinal de negativo por nada (para removê-lo)
                line = line.replace("-", "")
                # Substituir todas as vírgulas por pontos
                line = line.replace(",", ".")
                # Imprimir a linha atualizada
                print(line, end="")
                
            # Fechar o arquivo de cópia
            copy_file.close()

# Imprimir mensagem de conclusão
print("Concluído!")
