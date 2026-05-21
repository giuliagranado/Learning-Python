#024 - leia o nome de uma cidade e diga se ela começa ou não com "SANTO"
cidade = str(input("informe o nome da cidade: ")).strip()
print(cidade[:5].upper() == "SANTO")


""" usar o upper para evitar problemas com letras minusculas ou maiusculas, ou seja, o programa vai funcionar mesmo que o usuario digite "santo" ou "SANTO" ou "sAnTo" """


# 025 - leia o nome de uma pessoa e diga se ela tem "SILVA" no nome
nome = str(input("nome da pessoa: ")).strip()
print("SILVA" in nome.upper())
