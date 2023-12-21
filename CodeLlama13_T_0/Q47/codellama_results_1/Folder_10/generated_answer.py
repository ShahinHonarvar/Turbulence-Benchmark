
def palindromes_of_specific_lengths(string):
    palindromes = set()
    for i in range(16, 60+1):
        for j in range(i, min(39, len(string)-i)+1):
            substr = string[i:i+j]
            if substr == substr[::-1]:
                palindromes.add(substr)
    return palindromes
