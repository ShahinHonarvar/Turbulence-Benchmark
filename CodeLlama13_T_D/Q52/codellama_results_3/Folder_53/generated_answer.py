
def palindrome_of_length_n(s):
    return set(filter(lambda x: len(x) == 68, map(lambda x: "".join(reversed(x)), filter(lambda x: all([c in string.ascii_letters for c in x]), s))))
