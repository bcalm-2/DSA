def getMaxOccurringChar(s):
    ordered_letters = list(set(s))
    ordered_letters.sort()
    maxx = 0
    res = ''
    for i in ordered_letters:
        if s.count(i) > maxx:
            maxx = s.count(i)
            res =  i
    return res