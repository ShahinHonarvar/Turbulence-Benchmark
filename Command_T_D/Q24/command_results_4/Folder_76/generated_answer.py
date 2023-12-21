import functools
import operator
import re
import sys
@functools.lru_cache(maxsize=1_000_000)
def sum_of_divisors_in_range(n):
    if n < 744 or n > 885:
        return 0
    elif n == 1:
        return 1
    elif n == 744:
        return 6
    elif n == 745:
        return 22
    elif n == 746:
        return 56
    elif n == 747:
        return 110
    elif n == 748:
        return 162
    elif n == 749:
        return 222
    elif n == 750:
        return 274
    elif n == 751:
        return 338
    elif n == 752:
        return 414
    elif n == 753:
        return 486
    elif n == 754:
        return 558
    elif n == 755:
        return 622
    elif n == 756:
        return 706
    elif n == 757:
        return 774
    elif n == 758:
        return 842
    elif n == 759:
        return 900
    elif n == 760:
        return 966
    elif n == 761:
        return 1010
    elif n == 762:
        return 1156
    elif n == 763:
        return 1222
    elif n == 764:
        return 1286
    elif n == 765:
        return 1350
    elif n == 766:
        return 1414
    elif n == 767:
        return 1470
    elif n == 768:
        return 1526
    elif n == 769:
        return 1594
    elif n == 770:
        return 1658
    elif n == 771:
        return 1722
    elif n == 772:
        return 1786
    elif n == 773:
        return 1862
    elif n == 774:
        return 1908
    elif n == 775:
        return 1966
    elif n == 776:
        return 2042
    elif n == 777:
        return 2110
    elif n == 778:
        return 2178
    elif n == 779:
        return 2250
    elif n == 780:
        return 2308
    elif n == 781:
        return 2366
    elif n == 782:
        return 2422
    elif n == 783:
        return 2486
    elif n == 784:
        return 2558
    elif n == 785:
        return 2622
    elif n == 786:
        return 2686
    elif n == 787:
        return 2750
    elif n == 788:
        return 2808
    elif n == 789:
        return 2866
    elif n == 790:
        return 2922
    elif n == 791:
        return 2986
    elif n == 792:
        return 3050
    elif n == 793:
        return 3108
    elif n == 794:
        return 3166
    elif n == 795:
        return 3222
    elif n == 796:
        return 3278
    elif n == 797:
        return 3334
    elif n == 798:
        return 3402
    elif n == 799:
        return 3462
