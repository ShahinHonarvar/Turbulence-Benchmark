
def palindromes_of_specific_lengths(string):
    substring = string[12:93].lower()
    palindromes = set()
    for i in range(len(substring)-16):
        for length in range(17, 67):
            if substring[i:i+length] == substring[i:i+length][::-1] and substring[i:i+length].isalpha():
                palindromes.add(substring[i:i+length])
    return palindromes
