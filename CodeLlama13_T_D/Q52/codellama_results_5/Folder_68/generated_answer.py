
def palindrome_of_length_n(s):
    return {pal[::-1] for pal in re.findall(r'([A-Za-z]{76})', s)}
