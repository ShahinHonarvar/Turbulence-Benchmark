def if_contains_anagrams(list):
    count = 0
    for x in list:
        for y in list:
            if x == y:
                continue
            elif set(x.lower()) == set(y.lower()):
                count += 1
    return count <= 60
