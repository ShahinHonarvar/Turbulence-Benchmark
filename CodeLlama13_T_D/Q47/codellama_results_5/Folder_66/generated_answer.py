
def palindromes_of_specific_lengths(string):
    palindromes = set()
    for i in range(32, 79+1):
        for j in range(i+35-1, i+41):
            if j < len(string) and string[j] == string[i]:
                palindromes.add(string[i:j])
    return palindromes
