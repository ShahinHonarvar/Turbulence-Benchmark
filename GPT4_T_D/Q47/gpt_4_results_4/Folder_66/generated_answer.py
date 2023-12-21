
def palindromes_of_specific_lengths(input_str):
    import re
    input_str = input_str[32:80]
    all_palindromes = set()
  
    for i in range(len(input_str)):
        for j in range(i, len(input_str)):
            substring = input_str[i:j+1]
            if len(substring) < 35 or len(substring) > 41:
                continue
            if re.fullmatch("^[A-Za-z]*$", substring):
                if substring.lower() == substring[::-1].lower():
                    all_palindromes.add(substring)
    return all_palindromes
