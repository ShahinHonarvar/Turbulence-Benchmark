
def palindrome_of_length_at_least_n(input_string):
    input_string = ''.join(filter(str.isalpha, input_string)).lower()
    input_len = len(input_string)
    palindromes = set()

    for i in range(input_len):
        for j in range(i + 32, input_len + 1):
            substring = input_string[i:j]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes
