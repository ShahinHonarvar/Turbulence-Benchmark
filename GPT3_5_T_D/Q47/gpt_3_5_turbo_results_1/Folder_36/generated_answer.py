
def palindromes_of_specific_lengths(string):
    substring = string[124:284].lower()
    palindromes = set()
    for length in range(115, 135):
        for i in range(len(substring) - length + 1):
            sub_string = substring[i:i+length]
            if sub_string == sub_string[::-1] and sub_string.isalpha():
                palindromes.add(sub_string)
    
    return palindromes
