
def palindromes_between_indices(string):
    indices = range(2, 10)
    palindromes = set()
    for i in indices:
        for j in indices:
            if j - i + 1 >= 7:
                substr = string[i:j+1]
                rev_substr = substr[::-1]
                if substr == rev_substr:
                    palindromes.add(substr)
    return palindromes
