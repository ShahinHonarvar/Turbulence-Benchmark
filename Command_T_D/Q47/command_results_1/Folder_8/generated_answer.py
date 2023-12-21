def palindromes_of_specific_lengths(s):
    return set(re.findall(r'(?i)(?=([a-z]){50}(?:[a-z]){49}(?:[a-z]){17}(?:[a-z]){72}(?:[a-z]){51}(?:[a-z]){49}(?:[a-z]){50}))', s))
