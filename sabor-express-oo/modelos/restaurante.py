##colocar nome de classe com letra maiuscula

##Classe restaurante

from modelos.avaliacao import Avaliacao
from modelos.cardapio.item_cardapio import ItemCardapio

class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._Ativo = False
        self._avaliacao = []
        self._cardapio = []  # Inicialize o atributo _cardapio aqui
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'{self._nome} | {self._categoria}'

    @classmethod
    def listar_restaurantes(cls):
        print(f"{'Nome do Restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Avaliação'.ljust(25)} | {'Status'.ljust(25)}")
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {str(restaurante.media_avaliacoes).ljust(25)} | {restaurante.Ativo}')

    ## Muda como um ATRIBUTO vai ser lido
    @property
    def Ativo(self):
        return 'alguma coisa' if self._Ativo else 'false' 

    def alternar_estado(self):
        self._Ativo = not self._Ativo

    def receber_avaliacao(self, cliente, nota):
        avaliacao = Avaliacao(cliente, nota)
        self._avaliacao.append(avaliacao)

    @property
    def media_avaliacoes(self):
        if not self._avaliacao:
            return 0
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_de_notas = len(self._avaliacao)
        media = round(soma_das_notas / quantidade_de_notas, 1)
        media_real = media / 2
        return media_real

    def adicionar_no_cardapio(self, item):
        if isinstance(item, ItemCardapio):
            self._cardapio.append(item)        

    @property
    def exibir_cardapio(self):
        print(f'Cardápio do restaurante: {self._nome}\n')
        for i, item in enumerate(self._cardapio, start=1):
            if hasattr(item,'descricao'):
                mensagem_prato = f'{i}. Nome: {item.nome} | Preço: R${item.preco} | Descrição: {item.descricao}'
                print(mensagem_prato)
            else:
                mensagem_bebida = f'{i}. Nome: {item.nome} | Preço: R${item.preco} | Descrição: {item.tamanho}'
                print(mensagem_bebida)



