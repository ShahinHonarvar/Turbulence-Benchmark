
def palindromes_of_specific_lengths(string):
    palindromes = set()
    for i in range(6, 10):
        substring = string[:i].lower()
        if substring.isalpha():
            for j in range(3, 6):
                if len(substring) >= j:
                    for k in range(len(substring) - j + 1):
                        if substring[k:k+j] == substring[k:k+j][::-1]:
                            palindromes.add(substring[k:k+j])
    return palindromes
