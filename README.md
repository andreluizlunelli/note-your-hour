# note-your-hour

Repositório para calcular horas trabalhadas baseado em um arquivo txt

Para rodar basta chamar:
```
python sum.py
```

Criar executável linux:
```
pyinstaller --onefile sum.py -n sum.sh
```

Criar executável widows apartir do linux
```
docker run -v "$(pwd):/src/" cdrx/pyinstaller-windows
```