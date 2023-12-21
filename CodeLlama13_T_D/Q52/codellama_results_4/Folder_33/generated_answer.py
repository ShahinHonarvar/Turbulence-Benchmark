
def palindrome_of_length_n(string):
    return set(s for s in re.findall('(?i)([a-z]{475})', string))
