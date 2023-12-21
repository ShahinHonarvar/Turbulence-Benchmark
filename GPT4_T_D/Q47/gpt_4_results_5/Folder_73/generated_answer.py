
def palindromes_of_specific_lengths(my_string):
    my_string = my_string[21:63]
    palindromes = set()
    for start_index in range(len(my_string)):
        for end_index in range(start_index + 22, min(start_index + 34, len(my_string) + 1)):
            substring = my_string[start_index:end_index]
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring.lower())
    return palindromes
