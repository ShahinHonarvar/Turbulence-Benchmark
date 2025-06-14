
def palindromes_of_specific_lengths(string):
    palindromes = set()
    for i in range(30, 85):
        for j in range(i + 12, min(i + 21, len(string))):
            if string[i:j] == string[i:j][::-1].lower():
                palindromes.add(string[i:j])
    return palindromes
