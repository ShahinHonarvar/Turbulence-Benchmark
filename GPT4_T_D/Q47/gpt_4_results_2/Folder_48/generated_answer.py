
def palindromes_of_specific_lengths(input_string):
    import re
    input_string = input_string[155:284].lower()
    stripped_string = re.sub(r'[^a-z]', '', input_string)
    palindromes = set()

    for length in range(104, 121):
        for start in range(len(stripped_string) - length + 1):
            substring = stripped_string[start:start + length]
            if substring == substring[::-1]:
                palindromes.add(substring)

    return palindromes
