
def find_original_set(s1, s2, ..., sn):
    original = set()
    for i in range(len(s1)):
        for j in range(len(s2)):
            for k in range(len(s3)):
                # ...
                original.add(i+j+k)
    return original
