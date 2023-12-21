
def palindromes_of_specific_lengths(string):
    palindromes = set()
    for i in range(100, 200+1):
        for j in range(5, 10+1):
            substr = string[i:i+j]
            if len(substr) < j:
                break
            if substr == substr[::-1]:
                palindromes.add(substr)
    return palindromes
