from random import randint
#Banco de palavras


listaPalavras = []


with open("palavras.txt") as file:
    for line in file:
        listaPalavras.append(line.rstrip())
    file.close()



class Forca_Internal:
    """Classe utilizada para buscar letras nas palavras,
    determinar a posição e modificar as chances."""

    def __init__(self) -> None:
        """inicializa uma palavra aleatório do banco de palavras e
        secreta ela."""

        self.palavra = listaPalavras[randint(0,len(listaPalavras))]
        self.posicao = []
        self.adivinhar = ["_"] * len(self.palavra)
        self.adivinhando = "".join(self.adivinhar)



    def findletra(self, letra: str) -> None:
        """parametro letra: letra a ser encontrada
        na palavra inicializada pelo self.palavra.

                busca pela letra na palavra, determina a posição e
        mostra as letras encontradas"""

        for pos in range(0, len(self.palavra)):
            if letra == self.palavra[pos]:
                self.posicao.append(pos)
        if self.posicao == []:
             self.chances -= 1
        for indice in self.posicao:
                del self.adivinhar[indice]
                self.adivinhar.insert(indice, letra)
        self.posicao = []
        self.adivinhando = "".join(self.adivinhar)

