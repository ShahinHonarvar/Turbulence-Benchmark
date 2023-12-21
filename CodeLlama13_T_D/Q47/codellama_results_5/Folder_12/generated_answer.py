
def palindromes_of_specific_lengths(string):
    sub = string[62:89]
    palindromes = set()
    for i in range(18, 22):
        for j in range(len(sub) - i + 1):
            if sub[j:j+i].lower() == sub[j:j+i][::-1]:
                palindromes.add(sub[j:j+i])
    return palindromes
