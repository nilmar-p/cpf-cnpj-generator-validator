import random

#menus
def menu():
    print("\n=-=-= >>> CPF/CNPJ VALIDATOR <<< =-=-= \n")
    print("1. Gerar")
    print("2. Checar\n")
    print("0. Fechar\n")

    try:
        option = int(input(">>> "))
        if option not in [0, 1, 2]:
            print("Erro! Opção inexistente! <<<<<<<<<<")
            return None
        return option
    
    except ValueError:
        print("Erro! Digite um número inteiro! <<<<<<<<<<")
        return None


def check_menu():
    print("=-=-= >>> Checagem <<< =-=-= \n")
    print("1. CPF")
    print("2. CNPJ\n")
    print("0. Voltar\n")    

    option = None

    try:
        option = int(input(">>> "))

        if option not in [0, 1, 2]:
            print("Erro! Opção inexistente! <<<<<<<<<<")
            return None    
        return option
    
    except ValueError:
        print(f"Erro! Digite um número inteiro! <<<<<<<<<<")
        return None

def generate_menu():
    print("=-=-= >>> Gerar Registros <<< =-=-= \n")
    print("1. Gerar 10 CPF's válidos")
    print("2. Gerar 10 CNPJ's válidos\n")
    print("0. Voltar\n")    

    option = None

    try:
        option = int(input(">>> "))

        if option not in [0, 1, 2]:
            print("Erro! Opção inexistente! <<<<<<<<<<")
            return None    
        return option
    
    except ValueError:
        print(f"Erro! Digite um número inteiro! <<<<<<<<<<")
        return None

#utils
def is_valid_cpf(cpf):
    if len(cpf) != 11:
        print("!!!!!ERRO!!!!! CPF deve conter 11 dígitos numéricos \n")
        return False
    
    print(f"\n=-=-= >>> CPF: {cpf[0:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:11]}")

    sub_cpf = cpf[0:9][::-1]

    sum = 0
    for i in range(9):
        digit = int(sub_cpf[i])
        sum += digit * (i + 2)

    remainder = sum % 11

    first_check_digit = 0 if remainder < 2 else 11 - remainder

    if(first_check_digit != int(cpf[9])):
        return False
    
    sub_cpf = cpf[0:10][::-1]
    
    sum = 0
    for i in range (10):
        digit = int(sub_cpf[i])
        sum += digit * (i + 2)

    remainder = sum % 11

    second_check_digit = 0 if remainder < 2 else 11 - remainder

    if (second_check_digit != int(cpf[10])):
        return False
    
    return True

def is_valid_cnpj(cnpj):
    print(f"\n=-=-= >>> CNPJ: {cnpj[0:2]}.{cnpj[2:5]}.{cnpj[5:8]}/{cnpj[8:12]}.{cnpj[12:14]}")

    if len(cnpj) != 14:
        print("=-=-= >>> ERRO! CNPJ deve conter 14 dígitos numéricos")
        return False

    sub_cnpj = cnpj[0:12][::-1]
    
    sum = 0
    for i in range(12):
        digit = int(sub_cnpj[i])
        if (i >= 0 and i <= 7):
            sum += digit * (i+2)
        else:
            sum += digit * (i-6)
        
    remainder = sum % 11

    first_check_digit = 0 if remainder < 2 else 11 - remainder

    if (first_check_digit != int(cnpj[12])):
        return False
    
    sub_cnpj = cnpj[0:13][::-1]

    sum = 0
    for i in range(13):
        digit = int(sub_cnpj[i])
        if (i >= 0 and i <= 7):
            sum += digit * (i+2)
        else:
            sum += digit * (i-6)

    remainder = sum % 11

    second_check_digit = 0 if remainder < 2 else 11 - remainder

    if (second_check_digit != int(cnpj[13])):
        return False
    
    return True

def generate_cpfs():
    for i in range(10):
        num = None

        while True:
            num = random.randint(100000000, 999999999)
            num_str = str(num)

            if len(set(num_str)) == 1:
                continue

            break

        print(f"{generate_check_cpf_digits(num_str)}")

def generate_check_cpf_digits(base_cpf):
    total = 0
    for i in range(9):
        digit = int(base_cpf[i])
        total += digit * (10 - i)
    
    remainder = total % 11
    first_check_digit = 0 if remainder < 2 else 11 - remainder

    total = 0
    for i in range(9):
        digit = int(base_cpf[i])
        total += digit * (11 - i)
    
    total += first_check_digit * 2
    remainder = total % 11
    second_check_digit = 0 if remainder < 2 else 11 - remainder

    return f"{base_cpf[:3]}.{base_cpf[3:6]}.{base_cpf[6:9]}-{first_check_digit}{second_check_digit}"

def generate_check_cnpj_digits(base_cnpj):
    print("aaabbbcccdddeeefffggg")  
# main
while True:
    option = menu()

    if (option is None):
        continue

    match option:
        case 0:
            print(">>> Encerrando app...")
            break

        case 1:
            opt = generate_menu()

            if (opt is None):
                continue

            match opt:
                case 1:
                    generate_cpfs()

        case 2:
            opt = check_menu()
            if (opt is None):
                continue

            match opt:
                case 0:
                    continue

                case 1:
                    print("\n=-= >> Digite o CPF: ")

                    if is_valid_cpf(input(">>> ")):
                        print("=-=-= >>> CPF INFORMADO É VÁLIDO <<< =-=-=")
                    else:
                        print("!!!!!INVÁLIDO!!!!! CPF INFORMÁDO É INVÁLIDO!")
                    
                case 2:
                    print("\n =-= >> Digite o CNPJ: ")

                    if is_valid_cnpj(input(">>> ")):
                        print("=-=-= >>> CNPJ INFORMADO É VÁLIDO <<< =-=-=")
                    else:
                        print("!!!!!INVÁLIDO!!!!! CNPJ INFORMÁDO É INVÁLIDO!")
        