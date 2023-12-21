
def palindromes_of_specific_lengths(string):
    palindromes = set()
    for i in range(12, 221):
        for j in range(i+1):
            if string[j:i-j].lower() == string[j:i-j][::-1]:
                palindromes.add(string[j:i-j])
    return palindromes
