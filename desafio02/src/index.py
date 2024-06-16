def contar_frutas(frutas):
    # Lista de Tuplas
    lista_tuplas = [(fruta, frutas.count(fruta)) for fruta in set(frutas)]
    
    # Dicionário
    dicionario = {}
    for fruta in frutas:
        if fruta in dicionario:
            dicionario[fruta] += 1
        else:
            dicionario[fruta] = 1
    
    # Lista de Dicionários
    lista_dicionarios = [{"nome": fruta, "quantidade": frutas.count(fruta)} for fruta in set(frutas)]
    
    return lista_tuplas, dicionario, lista_dicionarios

# Exemplo de uso
frutas = ["maçã", "banana", "maçã", "laranja", "maçã", "uva", "banana", "uva"]

tuplas, dic, lista_dic = contar_frutas(frutas)

print("Lista de Tuplas:", tuplas)
print("Dicionário:", dic)
print("Lista de Dicionários:", lista_dic)