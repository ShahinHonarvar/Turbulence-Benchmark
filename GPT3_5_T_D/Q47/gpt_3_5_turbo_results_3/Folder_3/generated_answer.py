
def palindromes_of_specific_lengths(string):
    string = string.lower()
    substring = string[27:96]
    palindromes = set()
    for i in range(len(substring) - 51):
        if substring[i:i+49] == substring[i:i+49][::-1]:
            palindromes.add(substring[i:i+49])
        if substring[i:i+50] == substring[i:i+50][::-1]:
            palindromes.add(substring[i:i+50])
        if substring[i:i+51] == substring[i:i+51][::-1]:
            palindromes.add(substring[i:i+51])
    return palindromes.intersection(set(string.ascii_lowercase))
