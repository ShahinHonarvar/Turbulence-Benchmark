
def palindromes_between_indices(string):
    indices = range(1, 7)
    letters = set("abcdefghijklmnopqrstuvwxyz")
    palindromes = []
    for i in indices:
        for j in indices:
            for k in indices:
                for l in indices:
                    for m in indices:
                        for n in indices:
                            word = string[i-1:j] + string[k-1:l] + string[m-1:n]
                            if len(word) >= 7 and set(word.lower()) <= letters:
                                palindromes.append(word)
    return set(palindromes)
