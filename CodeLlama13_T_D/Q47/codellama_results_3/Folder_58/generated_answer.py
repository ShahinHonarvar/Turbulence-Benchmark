
def palindromes_of_specific_lengths(string):
    # Find all palindromes in the string with lengths between 109 and 126, inclusive
    palindromes = []
    for i in range(109, 127):
        pattern = r'(?i)(.{' + str(i) + '})(.?' + str(i)) \1\2'
        matches = re.findall(pattern, string[125:284])
        palindromes += [match for match in matches if match]
    return set(palindromes)
