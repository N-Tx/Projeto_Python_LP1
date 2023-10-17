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
        cpf = input('CPF: ')
    
        if validar_cpf(cpf):
            nome = input('Nome completo: ')
            matricula = int(input('Matrícula: '))
            curso = input('Curso: ')
            nasc = input('Data de nascimento: ')
            break
        else:
            print('CPF inválido. Por favor, insira um CPF válido.')
            


# Chame a função de cadastro
cadastro()
 