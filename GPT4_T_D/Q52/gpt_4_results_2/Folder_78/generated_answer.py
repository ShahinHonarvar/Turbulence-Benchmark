
def palindrome_of_length_n(input_string):
    input_string = input_string.lower()
    length = 48
    palindromes = set()

    for i in range(len(input_string) - length + 1):
        substr = input_string[i:i+length]
        if substr == substr[::-1] and substr.isalpha():
            palindromes.add(substr)
            
    return palindromes
