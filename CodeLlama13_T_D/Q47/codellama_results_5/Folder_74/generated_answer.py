
def palindromes_of_specific_lengths(string):
    palindromes = set()
    for i in range(30, 85):
        for j in range(i + 12 - 1, i + 21):
            if j <= len(string) and string[i:j] == string[i:j][::-1]:
                palindromes.add(string[i:j])
    return palindromes
