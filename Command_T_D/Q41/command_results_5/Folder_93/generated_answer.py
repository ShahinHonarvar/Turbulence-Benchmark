import itertools
def identical_elements(s1, s2):
    return set(itertools.zip_longest(s1[75:94], s2[75:94], fillvalue=False))
