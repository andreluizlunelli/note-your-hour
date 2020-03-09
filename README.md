# note-your-hour

Repositório para quantificar horas trabalhadas baseado em um arquivo txt

Para rodar basta chamar:
```
python sum.py
```

Parâmetros opcionais: Arquivo de leitura e Dia
```
python sum.py /your/path/here/notas.txt 0
``` 
`/your/path/here/notas.txt` Direciona qual será o arquivo de entrada de dados

`0` Busca a quantidade de horas do último dia informado. Se for `1` será um dia anterior, `2` um da anterior ao anterior e assim vai :)


Criar executável linux:
```
pyinstaller --onefile sum.py -n sum.sh
```

Criar executável widows apartir do linux
```
docker run -v "$(pwd):/src/" cdrx/pyinstaller-windows
```