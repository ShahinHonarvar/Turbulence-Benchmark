def identical_elements(s1, s2):
    return set(i for i in range(31, 73) if s1[i] in s2 and s2[i] in s1)
