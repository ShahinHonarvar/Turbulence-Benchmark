
def palindromes_of_specific_lengths(string):
    palindromes = set()
    for i in range(40, 95):
        for j in range(i+1, min(len(string), i+52)):
            substr = string[i:j]
            if len(substr) >= 45 and len(substr) <= 51 and substr == substr[::-1]:
                palindromes.add(substr)
    return palindromes
