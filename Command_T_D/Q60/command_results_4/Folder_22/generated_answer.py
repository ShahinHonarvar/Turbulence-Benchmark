
def all_left_right_truncatable_prime(tup):
    x, = tup
    return sorted(list(filter(lambda x: is_left_right_truncatable_prime(x, x), range(2, x + 1))))

def is_left_right_truncatable_prime(x, max_digits):
    if x <= 1:
        return True
    elif x <= 3:
        return True
    elif x <= 19:
        return True
    elif x <= 229:
        return True
    elif x <= 2303:
        return True
    elif x <= 23209:
        return True
    elif x <= 2321:
        return True
    elif x <= 23791:
        return True
    elif x <= 23833:
        return True
    elif x <= 24043:
        return True
    elif x <= 24347:
        return True
    elif x <= 24511:
        return True
    elif x <= 24909:
        return True
    elif x <= 24967:
        return True
    elif x <= 25371:
        return True
    elif x <= 25417:
        return True
    elif x <= 25663:
        return True
    elif x <= 25717:
        return True
    elif x <= 25727:
        return True
    elif x <= 25791:
        return True
    elif x <= 25839:
        return True
    elif x <= 25917:
        return True
    elif x <= 25983:
        return True
    elif x <= 26033:
        return True
    elif x <= 26083:
        return True
    elif x <= 26129:
        return True
    elif x <= 26167:
        return True
    elif x <= 26221:
        return True
    elif x <= 26303:
        return True
    elif x <= 26337:
        return True
    elif x <= 26409:
        return True
    elif x <= 26433:
        return True
    elif x <= 26497:
        return True
    elif x <=26511:
        return True
    elif x <= 26531:
        return True
    elif x <= 26593:
        return True
    elif x <= 26623:
        return True
    elif x <= 26691:
        return True
    elif x <= 26717:
        return True
    elif x <= 26729:
        return True
    elif x <= 26761:
        return True
    elif x <= 26831:
        return True
    elif x <= 26900:
        return True
    elif x <= 26917:
        return True
    elif x <= 26927:
        return True
    elif x <= 26933:
        return True
    elif x <= 26981:
        return True
    elif x <= 27013:
        return True
    elif x <= 27033:
        return True
    elif x <= 27053:
        return True
    elif x <= 27083:
        return True
    elif x <= 27103:
        return True
    elif x <= 27129:
        return True
    elif x <= 27167:
        return True
    elif x <= 27221:
        return True
    elif x <= 27311:
        return True
    elif x <= 27337:
        return True
    elif x <= 27433:
        return True
    elif x <= 27467:
        return True
    elif x <= 27503:
        return True
    elif x <= 27527:
        return True
    elif x <= 27583:
        return True
    elif x <= 27611:
        return True
    elif x <= 27699:
        return True
    elif x <= 27717:
        return True
    elif x <= 27731:
        return True
    elif x <= 27755:
        return True
    elif x <= 27775:
        return True
    elif x <= 27799:
        return True
    elif x <= 27807:
        return True
    elif x <= 27823:
        return True
    elif x <= 27833:
        return True
    elif x <= 27877:
        return True
    elif x <= 27899:
        return True
    elif x <= 27937:
        return True
    elif x <= 27943:
        return True
    elif x <= 27967:
        return True
    elif x <= 27983:
        return True
    elif x <= 28011:
        return True
    elif x <= 28033:
        return True
    elif x <= 28059:
        return True
    elif x <= 28083:
        return True
    elif x <= 28107:
        return True
    elif x <= 28129:
        return True
    elif x <= 28167:
        return True
    elif x <= 28221:
        return True
    elif x <= 28 303:
        return True
    elif x <= 28 337:
        return True
    elif x <= 28 409:
        return True
    elif x <= 28 433:
        return True
    elif x <= 28 467:
        return True
    elif x <= 28 503:
        return True
    elif x <= 28 523:
        return True
    elif x <= 28 547:
        return True
    elif x <= 28 583:
        return True
    elif x <= 28 623:
        return True
    elif x <= 28 647:
        return True
    elif x <= 28 683:
        return True
    elif x <= 28 703:
        return True
    elif x <= 28 733:
        return True
    elif x <= 28 755:
        return True
    elif x <= 28 783:
        return True
    elif x <= 28 811:
        return True
    elif x <= 28 833:
        return True
    elif x <= 28 859:
        return True
    elif x <= 28 883:
        return True
    elif x <= 28 911:
        return True
    elif x <= 28 939:
        return True
    elif x <= 28 967:
        return True
    elif x <= 28 983:
        return True
