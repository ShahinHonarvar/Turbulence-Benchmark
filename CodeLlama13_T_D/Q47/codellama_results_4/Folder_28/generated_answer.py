
def palindromes_of_specific_lengths(string):
    palindromes = set()
    for i in range(32, 72):
        for j in range(i+1, min(len(string), i+22)):
            substr = string[i:j]
            if substr == substr[::-1]:
                palindromes.add(substr)
    return palindromes
