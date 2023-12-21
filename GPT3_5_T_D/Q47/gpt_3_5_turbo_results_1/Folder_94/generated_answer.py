
def palindromes_of_specific_lengths(string):
    palindromes = set()
    substring = string[40:95].lower()
    for length in range(45, 52):
        for i in range(len(substring) - length + 1):
            if substring[i:i+length] == substring[i:i+length][::-1] and substring[i:i+length].isalpha():
                palindromes.add(substring[i:i+length])
    return palindromes
