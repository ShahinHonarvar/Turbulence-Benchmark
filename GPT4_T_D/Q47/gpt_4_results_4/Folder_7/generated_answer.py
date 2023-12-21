
def palindromes_of_specific_lengths(input_string):
    import re
    input_string = input_string[119:257]
    palindromes_set = set()

    for i in range(len(input_string)):
        for j in range(i+104, min(i+124, len(input_string)+1)):
            substring = input_string[i:j]
            substring_only_letters = re.sub("[^a-zA-Z]+", "", substring)
            if substring_only_letters.lower() == substring_only_letters[::-1].lower():
                palindromes_set.add(substring_only_letters)
                
    return palindromes_set
