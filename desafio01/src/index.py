def fruta_com_maior_quantidade_alfabetica(frutas):
    from collections import Counter
    
    # Usar Dicionário
    contagem_dict = {}
    for fruta in frutas:
        if fruta in contagem_dict:
            contagem_dict[fruta] += 1
        else:
            contagem_dict[fruta] = 1
    maior_quantidade_dict = max(contagem_dict.values())
    frutas_mais_comuns_dict = [fruta for fruta, qtd in contagem_dict.items() if qtd == maior_quantidade_dict]
    fruta_alfabetica_dict = min(frutas_mais_comuns_dict)
    
    # Usar Counter
    contagem_counter = Counter(frutas)
    maior_quantidade_counter = max(contagem_counter.values())
    frutas_mais_comuns_counter = [fruta for fruta, qtd in contagem_counter.items() if qtd == maior_quantidade_counter]
    fruta_alfabetica_counter = min(frutas_mais_comuns_counter)
    
    # Usar max com set
    maior_quantidade_set = max(frutas.count(fruta) for fruta in set(frutas))
    frutas_mais_comuns_set = [fruta for fruta in set(frutas) if frutas.count(fruta) == maior_quantidade_set]
    fruta_alfabetica_set = min(frutas_mais_comuns_set)
    
    # Resultado final
    return {
        "dicionario": (fruta_alfabetica_dict, maior_quantidade_dict),
        "counter": (fruta_alfabetica_counter, maior_quantidade_counter),
        "set_max": (fruta_alfabetica_set, maior_quantidade_set)
    }

# Exemplo de uso
frutas = ["maçã", "banana", "maçã", "laranja", "uva", "banana", "uva"]

resultado = fruta_com_maior_quantidade_alfabetica(frutas)
print(f"Usando Dicionário: A fruta com a maior quantidade e, em caso de empate, a primeira em ordem alfabética é '{resultado['dicionario'][0]}' com {resultado['dicionario'][1]} aparições.")
print(f"Usando Counter: A fruta com a maior quantidade e, em caso de empate, a primeira em ordem alfabética é '{resultado['counter'][0]}' com {resultado['counter'][1]} aparições.")
print(f"Usando Set e Max: A fruta com a maior quantidade e, em caso de empate, a primeira em ordem alfabética é '{resultado['set_max'][0]}' com {resultado['set_max'][1]} aparições.")
