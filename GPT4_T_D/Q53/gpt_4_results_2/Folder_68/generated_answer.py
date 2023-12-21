
def palindrome_of_length_at_least_n(my_string):
    my_string = my_string.lower()
    palindromes = set()
    for i in range(len(my_string)):
        for j in range(i + 21, len(my_string) + 1):
            chunk = my_string[i:j]
            if chunk == chunk[::-1] and chunk.isalpha():
                palindromes.add(chunk)
    return palindromes
