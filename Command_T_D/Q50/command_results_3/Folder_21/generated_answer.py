def if_contains_anagrams(st):
    res = set()
    for i in range(len(st)):
        for j in range(i+1, len(st)):
            if st[i].lower() == st[j].lower():
                if len(st[i]) > 2:
                    res.add(st[i])
    return len(res) > 135
