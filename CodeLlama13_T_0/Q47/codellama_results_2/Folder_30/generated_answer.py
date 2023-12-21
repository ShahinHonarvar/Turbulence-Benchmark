
def palindromes_of_specific_lengths(string):
    palindromes = set()
    for i in range(14, 90+1):
        for j in range(i+55-1, i+71):
            if string[i:j] == string[i:j][::-1]:
                palindromes.add(string[i:j])
    return palindromes
