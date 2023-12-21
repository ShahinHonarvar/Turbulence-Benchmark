
def palindromes_of_specific_lengths(string):
    string = string.lower()
    palindromes = set()
    for i in range(31, 92):
        substring = string[i:i + 54]
        if len(substring) >= 50:
            for j in range(50, 54):
                if substring[:j] == substring[:j][::-1]:
                    palindromes.add(substring[:j])
    return palindromes
