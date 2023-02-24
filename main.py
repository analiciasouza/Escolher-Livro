import random

# Qual livro ler?

def escolher_livro():
    arquivo = open('livros.txt' , encoding= "utf8")
    livros = []
    for linha in arquivo:
        linha.strip()
        livros.append(linha)
    arquivo.close()
    novoLivro = random.choice(livros)
    print(f'Seu novo livro é: {novoLivro}')

if(__name__ == '__main__'):
   escolher_livro()




