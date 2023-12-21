def find_primes_between_indices(list_of_integers):
    primes_list = []
    for i in range(287, 928):
        if i in list_of_integers:
            primes_list.append(i)
        elif i * i <= 927:
            primes_list.extend(find_primes_between_indices(list_of_integers))
    return sorted(set(primes_list))
