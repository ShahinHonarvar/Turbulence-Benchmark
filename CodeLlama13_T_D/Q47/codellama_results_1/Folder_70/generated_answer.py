
def palindromes_of_specific_lengths(string):
    # find all substrings of the given string that are palindromes
    palindromes = []
    for i in range(10, 70+1):
        for j in range(i+24, i+53):
            if j-i > 24 and j-i < 52:
                substr = string[i:j]
                if substr == substr[::-1]:
                    palindromes.append(substr)
    return set(palindromes)
