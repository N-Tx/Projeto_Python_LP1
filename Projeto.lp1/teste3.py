def validar_cpf(cpf):
    cpf = str(cpf)
    if not cpf.isdigit() or len(cpf) != 11:
        return False
    # Verifica o primeiro dígito verificador
    soma = 0
    for i in range(9):
        soma += int(cpf[i]) * (10 - i)
    digito1 = (soma * 10) % 11
    if digito1 == 10:
        digito1 = 0
    if digito1 != int(cpf[9]):
        return False
    # Verifica o segundo dígito verificador
    soma = 0
    for i in range(10):
        soma += int(cpf[i]) * (11 - i)
    digito2 = (soma * 10) % 11
    if digito2 == 10:
        digito2 = 0
    return digito2 == int(cpf[10])
def cadastro(cadastros):
    print('='*27)
    print('  Cadastro RuralSportClub')
    print('='*27)
    print()
    while True:
        cpf = input('CPF: ')
    
        if validar_cpf(cpf):
            nome = input('Nome completo: ')
            while True:
                matricula = input('Matrícula: ')
                if len(matricula) == 11 and matricula.isdigit():
                    break
                else:
                    print('Matrícula inválida. A matrícula deve conter exatamente 11 dígitos numéricos.')
            curso = input('Curso: ')
            nasc = input('Data de nascimento: ')
            
            # Crie um dicionário para armazenar os detalhes do cadastro
            cadastro_dict = {
                'Nome': nome,
                'Matrícula': matricula,
                'Curso': curso,
                'Data de Nascimento': nasc
            }
            
            # Armazene o dicionário de detalhes do cadastro usando o CPF como chave
            cadastros[cpf] = cadastro_dict
            print('Cadastro realizado com sucesso!')
            break
        else:
            print('CPF inválido. Por favor, insira um CPF válido.')
def procurar_cadastro(cadastros, cpf_procurado):
    if cpf_procurado in cadastros:
        detalhes_cadastro = cadastros[cpf_procurado]
        print('Detalhes do cadastro:')
        for chave, valor in detalhes_cadastro.items():
            print(f'{chave}: {valor}')
    else:
        print('CPF não encontrado no banco de dados.')
def reservar_quadra(quadra, nome):
    horario = input('Digite o horário desejado para a quadra (somente números): ')
    horario = int(horario)  # Converte o horário para um número inteiro
    #tentativa de nao deixar a pessoa reservar o mesmo horario
    #escopo (nao vamos adicionar dia pra reservar apenas a hora do dia, com a ideia que abrirá o app so no dia pra reservar de manha ate a noite prentendemos colocar hora como das8 as 21 q pode ser feita a reserva
    # )
    if horario in quadra:
        print(f'O horário das {horario} já está reservado por {quadra[horario]}.')
        
    else:
        quadra[horario] = nome
        print(f'Horário das {horario} reservado para {nome}')


   
def mostrar_cadastros(cadastros):
    if not cadastros:
        print('Nenhum cadastro disponível.')
    else:
        print('\nCadastros:')
        for cpf, detalhes in cadastros.items():
            print(f'CPF: {cpf}')
            print(f'Nome: {detalhes["Nome"]}')
            print(f'Matrícula: {detalhes["Matrícula"]}')
            print(f'Curso: {detalhes["Curso"]}')
            print(f'Data de Nascimento: {detalhes["Data de Nascimento"]}')
            print()
            
def visualizar_quadra(quadra):
    # Função para visualizar as reservas na quadra
    print('\nQuadra Reservada:')
    for horario, nome in quadra.items():
        if nome is not None:
            print(f'Horário das {horario} reservado por {nome}')
cadastros = {}  # Dicionário para armazenar os cadastros
quadra_disponivel = {}  # Dicionário para armazenar a disponibilidade da quadra

cadastro(cadastros)

print('#'*30)
while True:
    
    print("\nMenu:")
    print('#'*30)
    print("1. Reservar Horário na Quadra")
    print("2. Visualizar Reservas na Quadra")
    print("3. Sair")
    print('#'*30)
    opcao = input("Escolha uma opção: ")
    
    if opcao == '1':
        cpf_procurado = input('Digite o CPF da pessoa que deseja reservar um horário na quadra: ')
        if cpf_procurado in cadastros:
            nome = cadastros[cpf_procurado]["Nome"]
            reservar_quadra(quadra_disponivel, nome)
        else:
            print('CPF não encontrado no banco de dados.')
    elif opcao == '2':
        visualizar_quadra(quadra_disponivel)
    elif opcao == '3':
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")
print("Encerrando o programa.")