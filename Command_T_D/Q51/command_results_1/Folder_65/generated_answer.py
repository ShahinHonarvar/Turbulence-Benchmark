def if_contains_anagrams(s):
    res = set()
    for x in s:
        flag = True
        for y in x:
            if y.lower() not in 'qwertyuiopasdfghjklzxcvbnm' or len(y) < 3:
                flag = False
                break
        if flag:
            res.add(x)
    return len(res) <= 72
