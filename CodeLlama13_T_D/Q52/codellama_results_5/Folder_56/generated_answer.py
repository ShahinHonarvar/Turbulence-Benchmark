
def palindrome_of_length_n(s):
    return set((x,) for x in re.findall('(?i)[a-z]{95}', s))
