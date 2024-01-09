# count = 0


def countVowel(n):
    # global count
    if len(n) == 0:
        return 0
    elif (
        n[0] == "a"
        or n[0] == "e"
        or n[0] == "i"
        or n[0] == "o"
        or n[0] == "u"
        or n[0] == "A"
        or n[0] == "E"
        or n[0] == "I"
        or n[0] == "O"
        or n[0] == "U"
    ):
        return 1 + countVowel(n[1:])
    else:
        return countVowel(n[1:])


print(countVowel("aiouwsadereIOU"))
