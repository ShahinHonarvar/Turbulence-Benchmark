
def palindromes_of_specific_lengths(string):
    lower = 18
    upper = 47
    start = 43
    end = 95
    palindromes = set()
    for length in range(lower, upper + 1):
        for i in range(start, end - length + 1):
            substr = string[i:i+length]
            if substr == substr[::-1]:
                palindromes.add(substr)
    return palindromes
