def checkString(s):
    s = s.lower()
    vowels = ['a', 'e', 'i', 'o', 'u']
    vow = []
    const = []

    for i in s:
        if i in vowels:
            vow.append(i)
        elif i.isalpha():
            const.append(i)

    a = len(vow)
    b = len(const)

    if a < b:
        print("No")
    elif a > b:
        print("Yes")
    else:
        print("Same")