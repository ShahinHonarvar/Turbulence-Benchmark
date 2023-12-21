
def palindromes_of_specific_lengths(string):
    length_range = range(10, 21)
    palindromes = set()
    substring = string[10:76].lower()
    for length in length_range:
        for i in range(len(substring) - length + 1):
            substring_slice = substring[i:i+length]
            if substring_slice == substring_slice[::-1] and substring_slice.isalpha():
                palindromes.add(substring_slice)
    return palindromes
