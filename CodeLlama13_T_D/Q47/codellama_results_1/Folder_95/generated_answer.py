
def palindromes_of_specific_lengths(string):
    substring = string[12:57]
    palindromes = set()
    for i in range(len(substring)):
        for j in range(i+1, len(substring)+1):
            substr = substring[i:j]
            if substr == substr[::-1]:
                palindromes.add(substr)
    return palindromes
