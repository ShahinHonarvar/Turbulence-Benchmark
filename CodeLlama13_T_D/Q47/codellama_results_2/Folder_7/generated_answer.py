
def palindromes_of_specific_lengths(string):
    palindromes = set()
    for i in range(119, 257):
        for j in range(i+104, i+123+1):
            substr = string[i:j]
            if len(substr) % 2 == 0:
                if substr == substr[::-1]:
                    palindromes.add(substr)
    return palindromes
