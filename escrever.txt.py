arquivoTXT = open("texto.txt", "w", encoding="utf-8")

texto = list()

texto.append("Modelagem de sistemas em uml")
texto.append("Sistemas de Informacao e Sociedade")
texto.append("Persistência de dados com Python")
texto.append("Desenv. Back-end Corporativo Com Java e Cloud")
texto.append("Programacao Back-end Com Java")

for linha in texto:
    arquivoTXT.write(linha + "\n")

arquivoTXT.close()

print("Arquivo texto.txt criado com sucesso!")