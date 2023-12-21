
def if_contains_anagrams(lista):
    counter = 0
    for i in range(0, len(lista)):
        for j in range(i+1, len(lista)):
            if len(lista[i]) >=3 and len(lista[j])>=3 and sorted(lista[i].lower()) == sorted(lista[j].lower()):
                counter += 1
            if counter >= 106:
                return True
    return False
