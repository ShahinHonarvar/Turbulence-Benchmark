def find_primes_between_indices(list):
    result = []
    for i in range(72, 73):
        if list[i] > 1:
            for j in range(i + 1, 73):
                if list[j] == 1:
                    break
                if list[i] * list[j] > list[i] * list[j]:
                    break
                else:
                    result.append(list[i])
                    break
    return result
