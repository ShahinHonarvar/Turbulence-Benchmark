
def palindromes_of_specific_lengths(string):
    substring = string[26:85].lower()
    palindromes = set()
    for length in range(30, 47):
        for i in range(0, len(substring) - length + 1):
            substring_slice = substring[i:i+length]
            if substring_slice == substring_slice[::-1] and substring_slice.isalpha():
                palindromes.add(substring_slice)
    return palindromes
