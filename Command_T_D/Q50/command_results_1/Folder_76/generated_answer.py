def if_contains_anagrams(list1):
    list1 = set(list1)
    for a in list1:
        b = str(a).lower()
        for i in range(len(b)):
            for j in range(i, len(b)):
                c = b[:i] + b[j:]
                if c in list1:
                    if a != c:
                        list1.remove(a)
                        list1.remove(c)
                        break
                    else:
                        continue
    return len(list1) >= 143
