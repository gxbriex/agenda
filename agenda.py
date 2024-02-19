agenda = {}


def adicionar_contato(nome, numero):
    agenda[nome] = numero
    print("Contato adicionado.")


def editar_contato(nome, novo_numero):
    agenda[nome] = novo_numero
    print("Contato editado.")


def apagar_contato(nome):
    if nome in agenda:
        del agenda[nome]
        print("Contato apagado.")
    else:
        print("Contato não encontrado.")


def ler_contatos():
    if len(agenda) > 0:
        print("Contatos na agenda: ")
        for nome, numero in agenda.items():
            print(f"Nome: {nome}, Número {numero}")
    else:
        print("Agenda vazia.")


while True:
    print("\nEscolha uma opção:")
    print("1. Adicionar contato.")
    print("2. Editar contato.")
    print("3. Excluir contato.")
    print("4. Ler contato")
    print("5. Sair.")

    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        nome = input("Nome do contato: ")
        numero = int(input("Numero do contato: "))
        adicionar_contato(nome, numero)
    elif opcao == '2':
        nome = input("Nome do contato que deseja editar: ")
        novo_numero = int(input("Digite o novo número: "))
        editar_contato(nome, novo_numero)
    elif opcao == '3':
        nome = input("Nome do contato que deseja apagar: ")
        apagar_contato(nome)
    elif opcao == '4':
        ler_contatos()
    elif opcao == '5':
        print("Saindo...")
        break
    else:
        print("Opção inválida.")