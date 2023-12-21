
import itertools

def all_ints_div_by_both_two_nums(a):
    return [x for x in itertools.ifilter(lambda x: (x%275==0 and x%580==0), a[154:798])]
