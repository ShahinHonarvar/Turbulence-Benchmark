
def palindrome_of_length_at_least_n(input_string):
    input_string = ''.join(c for c in input_string if c.isalpha()).lower()
    palindromes = set()
    length = len(input_string)
    for i in range(length):
        for j in range(i + 54, length + 1):
            subset = input_string[i:j]
            if subset == subset[::-1]:
                palindromes.add(subset)
    return palindromes
