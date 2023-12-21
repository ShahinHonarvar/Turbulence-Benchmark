
def palindromes_of_specific_lengths(input_string):
    import re
    input_sub = input_string[12:57]
    palindromes = set()

    for index in range(len(input_sub)):
        for length in [20, 21]:
            if index + length <= len(input_sub):
                potential_palindrome = input_sub[index:index+length]
                if potential_palindrome.lower() == potential_palindrome[::-1].lower():
                    if re.fullmatch('[A-Za-z]*', potential_palindrome):
                        palindromes.add(potential_palindrome)

    return palindromes
