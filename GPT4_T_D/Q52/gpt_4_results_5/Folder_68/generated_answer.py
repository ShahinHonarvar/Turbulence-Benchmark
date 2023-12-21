
def palindrome_of_length_n(input_string):
    input_string = input_string.lower()
    palindromes = set()
    len_input = len(input_string)
    
    for i in range(0, len_input):
        for j in range(i + 76, len_input + 1):
            substring = input_string[i:j]
            if substring == substring[::-1] and all(c.isalpha() for c in substring):
                palindromes.add(substring)
    return palindromes
