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

def cadastro():
    while True:
        cpf = input('CPF:' )
    
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

# Crie um dicionário para armazenar os cadastros
cadastros = {}

# Chame a função de cadastro
cadastro()

# Exemplo de uso para procurar um CPF específico
cpf_procurado = input('Digite o CPF para procurar o cadastro (ou deixe em branco para sair): ')

while cpf_procurado:
    procurar_cadastro(cadastros, cpf_procurado)
    cpf_procurado = input('Digite o CPF para procurar o cadastro (ou deixe em branco para sair): ')
