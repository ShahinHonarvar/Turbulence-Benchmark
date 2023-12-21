
def palindromes_of_specific_lengths(string):
    palindromes = set()
    substring = string[18:89].lower()
    for i in range(len(substring)-11):
        if substring[i:i+12] == substring[i:i+12][::-1]:
            palindromes.add(substring[i:i+12])
        elif substring[i:i+13] == substring[i:i+13][::-1]:
            palindromes.add(substring[i:i+13])
        elif substring[i:i+14] == substring[i:i+14][::-1]:
            palindromes.add(substring[i:i+14])
    return palindromes
