import os.path
import re
from datetime import timedelta
import sys
from sys import exit

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


def get_note_raw_content():
    raw = ''
    with open(file_import_path) as file:
        raw = file.read()
    return raw


def get_note_content_iterator():
    pattern = r"^^## Horários\n(\d{2}\/\d{2}\/\d{4}\s(\d{2}h\d{2}\s-\s\d{2}h\d{2}\t?)+(.*)\n)+(\n{2})?"

    raw_content = get_note_raw_content()

    return re.search(pattern, raw_content, re.MULTILINE | re.IGNORECASE)


def get_raw_lines_notes(matches):
    hours_list = []
    for line in matches.group().split('\n')[1:]:
        if not line:
            continue
        hours_list.append(line)
    return hours_list


def sum_hour_notes(notes):
    """Somar horas encontradas"""

    sum = timedelta()

    for note in notes:
        pattern = r"(\d{2}h\d{2}\s-\s\d{2}h\d{2}\t?)+"

        search = re.search(pattern, note)

        raw_hours = search.group()

        pair_start_end_hour = raw_hours.split('\t')

        for pair in pair_start_end_hour:
            if not pair:
                continue

            start, end = pair.split(' - ')

            h, m = start.split('h')

            start_hour = timedelta(hours=int(h), minutes=int(m))

            h, m = end.split('h')

            end_hour = timedelta(hours=int(h), minutes=int(m))

            sum += end_hour - start_hour

    return sum


def get_custom_file_if_exists(file_import_path):
    try:
        file_import_path = sys.argv[1]
    except IndexError as e:
        pass
    return file_import_path


def check_if_file_exists(file_import_path):
    exists = os.path.exists(file_import_path)

    if not exists:
        with open(file_import_path, 'w') as file:
            file.write(file_sample)
        print(f"Arquivo de exemplo criado: {file_import_path}")
        exit()


"""
Começa aqui o 'main'
"""

file_import_path = get_custom_file_if_exists(file_import_path)

check_if_file_exists(file_import_path)

matches = get_note_content_iterator()

notes = get_raw_lines_notes(matches)

sum_hour = sum_hour_notes(notes)

totsec = sum_hour.total_seconds()
h = totsec//3600
m = (totsec%3600) // 60
sec = (totsec%3600)%60

print(f"Você trabalhou um total de {int(h)} horas e {int(m)} minutos")
