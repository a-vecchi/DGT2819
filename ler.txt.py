arquivoTxt = open("loremipsum.txt", "r", encoding="utf-8")

conteudo = arquivoTxt.read()
print("Conteúdo do arquivo TXT:")
print(conteudo)

arquivoTxt.seek(0)
print("Conteúdo da primeira linha:")
print(arquivoTxt.readline())

arquivoTxt.seek(0)
print("Primeiros 3 caracteres:")
print(arquivoTxt.read(3))

arquivoTxt.close()

print("Conteúdo do arquivo TXT usando with:")
with open("loremipsum.txt", "r", encoding="utf-8") as f:
    print(f.read())