def bye_duplicate ():
    noki = input ("ENTER NUMBERS:")
    noki = list (noki)
    nok = []

    for i in noki:
        if i not in nok:
            nok.append(i)

    print(nok)
bye_duplicate()