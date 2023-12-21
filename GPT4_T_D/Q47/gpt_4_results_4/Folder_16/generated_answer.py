
def palindromes_of_specific_lengths(input_string):
    palindromes = set()
    input_string = input_string[15:87]
    
    for length in range(51, 61):
        for start in range(len(input_string) - length + 1):
            substring = input_string[start:start+length]
            if substring.lower() == substring.lower()[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes
