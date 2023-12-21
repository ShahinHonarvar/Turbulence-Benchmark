
def palindromes_of_specific_lengths(string):
    palindromes = set()
    for i in range(1, 299):
        for j in range(i+3, i+10):
            if j > len(string):
                break
            substring = string[i:j]
            reverse_substring = substring[::-1]
            if substring == reverse_substring and all(c.isalpha() for c in substring):
                palindromes.add(substring)
    return palindromes
