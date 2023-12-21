def palindromes_of_specific_lengths(str):
    str = str[11:97+1].lower()
    return set(re.findall(r'[a-z]{29,62}([a-z]{29,62})', str))
