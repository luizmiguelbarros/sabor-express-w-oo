from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato

restaurante_choes = Restaurante('Choes', 'Japonesa')
bebida_suco = Bebida('Suco de Laranja', 8.00, 'Suco de laranja do grande macho peludo')
prato_pao = Prato('Pão', 3.00, 'Erick quer pão?')
prato_pao.aplicar_desconto()
bebida_suco.aplicar_desconto()

restaurante_choes.adicionar_no_cardapio(bebida_suco)
restaurante_choes.adicionar_no_cardapio(prato_pao)


def main():
    restaurante_choes.exibir_cardapio

if __name__ == '__main__':
    main()

