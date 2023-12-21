
def palindromes_of_specific_lengths(string):
    palindromes = set()
    for i in range(124, 284):
        for j in range(115, 135):
            substring = string[i:i+j]
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring.lower())
    return palindromes
