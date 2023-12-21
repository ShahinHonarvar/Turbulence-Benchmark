
def find_original_set(s1, s2, ..., sn):
    original = set()
    for i in range(21):
        original |= locals()["s{}".format(i+1)]
    return original
