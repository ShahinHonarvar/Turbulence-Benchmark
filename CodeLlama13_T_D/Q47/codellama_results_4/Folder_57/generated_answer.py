
def palindromes_of_specific_lengths(string):
    palindromes = set()
    for i in range(16, 95):
        for j in range(i + 38, i + 53):
            if j > len(string):
                break
            substr = string[i:j]
            if substr == substr[::-1].lower():
                palindromes.add(substr)
    return palindromes
