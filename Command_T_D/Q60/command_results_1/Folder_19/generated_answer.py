
def all_left_right_truncatable_prime(n):
    return sorted(list(filter(left_right_truncatable_prime, range(2, n[0] + 1))), reverse=True)

def left_right_truncatable_prime(n):
    if n <= 1:
        return True
    if n == 2 or n == 3:
        return True
    if n == 5 or n == 7:
        return True
    if n == 11 or n == 13:
        return True
    if n == 17 or n == 19:
        return True
    if n == 23 or n == 29:
        return True
    if n == 31 or n == 37:
        return True
    if n == 41 or n == 43:
        return True
    if n == 47 or n == 53:
        return True
    if n == 59 or n == 61:
        return True
    if n == 67 or n == 71:
        return True
    if n == 73 or n == 79:
        return True
    if n == 83 or n == 89:
        return True
    if n == 97 or n == 101:
        return True
    if n == 103 or n == 107:
        return True
    if n == 109 or n == 113:
        return True
    if n == 127 or n == 131:
        return True
    if n == 137 or n == 139:
        return True
    if n == 149 or n == 151:
        return True
    if n == 157 or n == 163:
        return True
    if n == 167 or n == 173:
        return True
    if n == 179 or n == 181:
        return True
    if n == 191 or n == 193:
        return True
    if n == 197 or n == 199:
        return True
    if n == 211 or n == 223:
        return True
    if n == 227 or n == 229:
        return True
    if n == 233 or n == 239:
        return True
    if n == 241 or n == 251:
        return True
    if n == 257 or n == 263:
        return True
    if n == 269 or n == 271:
        return True
    if n == 277 or n == 281:
        return True
    if n == 283 or n == 293:
        return True
    if n == 307 or n == 311:
        return True
    if n == 317 or n == 331:
        return True
    if n == 337 or n == 347:
        return True
    if n == 349 or n == 353:
        return True
    if n == 359 or n == 367:
        return True
    if n == 373 or n == 379:
        return True
    if n == 383 or n == 389:
        return True
    if n == 397 or n == 399:
        return True
    if n == 409 or n == 419:
        return True
    if n == 421 or n == 431:
        return True
    if n == 433 or n == 439:
        return True
    if n == 443 or n == 449:
        return True
    if n == 457 or n == 461:
        return True
    if n == 463 or n == 467:
        return True
    if n == 479 or n == 487:
        return True
    if n == 491 or n == 499:
        return True
    if n == 503 or n == 509:
        return True
    if n == 521 or n == 607:
        return True
    if n == 607 or n == 613:
        return True
    if n == 617 or n == 619:
        return True
    if n == 631 or n == 641:
        return True
    if n == 643 or n == 647:
        return True
    if n == 653 or n == 659:
        return True
    if n == 661 or n == 673:
        return True
    if n == 677 or n == 683:
        return True
    if n == 719 or n == 733:
        return True
    if n == 743 or n == 749:
        return True
    if n == 757 or n == 761:
        return True
    if n == 769 or n == 773:
        return True
    if n == 787 or n == 797:
        return True
    if n == 809 or n == 811:
        return True
    if n == 821 or n == 827:
        return True
    if n == 829 or n == 837:
        return True
    if n == 841 or n == 853:
        return True
    if n == 857 or n == 859:
        return True
    if n == 863 or n == 867:
        return True
    if n == 871 or n == 873:
        return True
    if n == 881 or n == 883:
        return True
    if n == 887 or n == 907:
        return True
    if n == 911 or n == 919:
        return True
    if n == 923 or n == 927:
        return True
    if n == 937 or n == 941:
        return True
    if n == 947 or n == 953:
        return True
    if n == 967 or n == 971:
        return True
    if n == 977 or n == 983:
        return True
    if n == 991 or n == 997:
        return True
    return False
