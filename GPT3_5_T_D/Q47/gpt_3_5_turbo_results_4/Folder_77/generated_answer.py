
def palindromes_of_specific_lengths(string):
    substring = string[103:277].lower()
    palindromes = set()
    for length in range(100, 170):
        for i in range(len(substring) - length + 1):
            if substring[i:i+length] == substring[i:i+length][::-1] and substring[i:i+length].isalpha():
                palindromes.add(substring[i:i+length])
    return palindromes
