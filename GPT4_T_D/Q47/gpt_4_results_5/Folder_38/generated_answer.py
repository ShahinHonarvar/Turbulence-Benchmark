
def palindromes_of_specific_lengths(string):
    string = string[18:88]
    palindromes = set()
    for length in range(38, 61):
        for i in range(len(string)):
            temp_str = string[i:i+length].lower()
            if not temp_str.isalpha():
                continue
            if temp_str == temp_str[::-1]:
                palindromes.add(temp_str)
    return palindromes
