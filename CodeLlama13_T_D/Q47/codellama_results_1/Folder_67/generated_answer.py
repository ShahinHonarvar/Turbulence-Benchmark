
def palindromes_of_specific_lengths(string):
    lengths = range(26, 34)
    sub_string = string[65:100]
    palindromes = set()
    for length in lengths:
        for i in range(len(sub_string) - length + 1):
            substring = sub_string[i:i+length]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes
