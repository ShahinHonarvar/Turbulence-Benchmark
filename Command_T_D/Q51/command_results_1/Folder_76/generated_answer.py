def if_contains_anagrams(test_list):
    res = set()
    for el in test_list:
        el = str(el).lower()
        if len(el) < 3:
            continue
        for i in range(len(el)):
            el_ = el[:i] + el[i+1:]
            el_ = el_.lower()
            if el_ in res:
                res.remove(el_)
            res.add(el_)
            if len(res) > 91:
                return False
    return True
