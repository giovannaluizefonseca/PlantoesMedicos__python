from plantoes import Plantao

print("-" * 40)

def exibir_menu():
    print(f"Menu de Plantão Médico")
    print(f"1. Cadastrar Médico")
    print(f"2. Consultar Médicos")
    print(f"3. Consultar Médico Individual")
    print(f"4. Atualizar Médico")
    print(f"5. Deletar Médico")
    print(f"6. Sair")

f1 = Plantao() #Objeto criado

while True:
    exibir_menu()
    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        # Cadastrar médico
        id_medico = int(input("Informe o ID do médico: "))
        nome_medico = input("Informe o nome do médico: ")
        especialidade = input("Informe a especialidade do médico: ")
        data = input("Informe a data (YYYY-MM-DD): ")
        turno = input("Informe o turno do médico: ")
        f1.cadastrar(id_medico, nome_medico, especialidade, data, turno)

    elif opcao == '2':
        # Consultar todos os médicos
        f1.consultar()

    elif opcao == '3':
        # Consultar médico individual
        id_medico = int(input("Informe o ID do médico que deseja consultar: "))
        f1.consultar_individual(id_medico)

    elif opcao == '4':
        # Atualizar médico
        id_medico = int(input("Informe o ID do médico que deseja atualizar: "))
        novo_nome_medico = input("Informe o novo nome do médico: ")
        f1.atualizar(id_medico, novo_nome_medico)

    elif opcao == '5':
        # Deletar médico
        id_medico = int(input("Informe o ID do médico que deseja deletar: "))
        f1.deletar(id_medico)

    elif opcao == '6':
        # Sair
        print("Saindo do sistema.")
        break

    else:
        print("Opção inválida! Tente novamente.")
