import random
# Qual livro ler?
livros = ['Os Goonies - James Kahn', 'Senhor dos Aneis - J.R.R. Tolkien', 'Coraline - Neil Gaiman', '1984 - George Orwell', 
'O despertar do príncipe - Colleen Houck', 'Crimes e Castigo - Fiódor Dostoiévski',
'Orgulho e Preconceito - Jane Austen', 'Looking for Alasca - John Green','Álbum Duplo - Paulo Henrique Ferreira', 
'Todo Amor - Vinicius de Moraes', 'Para você que teve um dia ruim - Victor Fernandes']

novoLivro = random.choice(livros)
print(novoLivro)