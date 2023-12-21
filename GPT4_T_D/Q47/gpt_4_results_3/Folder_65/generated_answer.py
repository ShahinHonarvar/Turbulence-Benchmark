
def palindromes_of_specific_lengths(input_str):
    import re
    input_str = input_str[15:96]
    palindromes_set = set()
    for length in range(20, 67):
        for start in range(len(input_str) - length + 1):
            substring = input_str[start:start+length]
            if not re.search('[^a-zA-Z]', substring): 
                lower_substring = substring.lower()
                if lower_substring == lower_substring[::-1]: 
                    palindromes_set.add(substring)
    return palindromes_set
