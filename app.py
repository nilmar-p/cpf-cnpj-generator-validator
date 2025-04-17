#utils
def is_valid_cpf(cpf):   
    if len(cpf) != 11:
        print("!!!!!ERRO!!!!! CPF deve conter 11 dígitos numéricos \n")
        return False
    
    print(f"=-=-= >>> CNPJ: {cpf[0:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:11]}\n")

    sub_cpf = cpf[0:9][::-1]

    sum = 0
    for i in range(9):
        digit = int(sub_cpf[i])
        sum += digit * (i + 2)

    remainder = sum % 11

    first_check_digit = 0 if remainder < 2 else 11 - remainder

    if(first_check_digit != int(cpf[9])):
        print(f"!!!!!ERRO!!!!! Primeiro dígito verificador ({cpf[9]}) é INVÁLIDO")
        return False
    
    print(f"=-=-= >>> Primeiro dígito verificador ({cpf[9]}) é valido")

    sub_cpf = cpf[0:10][::-1]
    
    sum = 0
    for i in range (10):
        digit = int(sub_cpf[i])
        sum += digit * (i + 2)

    remainder = sum % 11

    second_check_digit = 0 if remainder < 2 else 11 - remainder

    if (second_check_digit != int(cpf[10])):
        print(f"!!!!!ERRO!!!!! Segundo dígito verificador ({cpf[10]}) é INVÁLIDO")
        return False

    print(f"=-=-= >>> Segundo dígito verificador ({cpf[10]}) é VÁLIDO \n")
    print(f"=-=-= >>> CPF INFORMADO É VÁLIDO <<< =-=-=")
    return True

def is_valid_cnpj(cnpj):
    print(f"=-=-= >>> CNPJ: {cnpj[0:2]}.{cnpj[2:5]}.{cnpj[5:8]}/{cnpj[8:12]}.{cnpj[12:14]} \n")

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
        print(f"!!!!!ERRO!!!!! Primeiro dígito verificador {cnpj[12]} é INVÁLIDO")
        return False
    
    print(f"=-=-= >>> Primero dígito verificador {cnpj[12]} é VÁLIDO")

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
        print(f"!!!!!ERRO!!!!! Segundo dígito verificador {cnpj[13]} é INVÁLIDO")
        return False
    
    print(f"=-=-= >>> Segundo dígito verificador {cnpj[13]} é VÁLIDO \n")
    print(f"=-=-= >>> CNPJ INFORMADO É VÁLIDO <<< =-=-=")
    return True

# main