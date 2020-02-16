import os.path

file_import_path = "./notas.txt"

file_sample = """Arquivo de exemplo.

Fui criado pois não foi encontrado um arquivo "notas.txt" :(

Após encontrar "## Horários" será lido linha por linha buscando o padrão

Exemplos de marcação válida:
04/02/2020 08h20 - 12h20	// introdução
04/02/2020 08h20 - 12h20	13h50 - 18h10// introdução
04/02/2020 08h20 - 12h20	13h50 - 18h10	19h00 - 20h00 // introdução

Exemplos de marcação ignorada:
04/02/2020 08h20 - 	// introdução
04/02/2020 08h20 - 12h20	13h50 - 18h // introdução

O programa para de buscar horários para somar quando chegar no fim do arquivo ou, encontrar duas linhas em brando.
Divirta-se!

## Horários
04/02/2020 08h20 - 12h20	13h50 - 18h10	// introdução, projeto importação


"""

exists = os.path.exists(file_import_path)

if not exists:
    with open(file_import_path, 'w') as file:
        file.write(file_sample)
    print(f"Arquivo de exemplo criado: {file_import_path}")
    exit()

