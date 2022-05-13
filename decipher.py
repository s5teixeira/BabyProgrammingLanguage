def decipher(babyExp):
    srcCode = ""
    # main part
    for i in range(len(babyExp)):

        # join elements of text with whitespaces
        if babyExp == "":
            srcCode = srcCode.strip("")

        # replacing baby exp with srcCode and count
        elif babyExp == "pee":
            srcCode = srcCode.replace("pee", "+",5)
        elif babyExp == "gah":
            srcCode = srcCode.replace("gah", "-",5)
        elif babyExp == "milk":
            srcCode = srcCode.replace("heh", "/",5)
        elif babyExp == "mama":
            srcCode = srcCode.replace("heh", "/",5)
        elif babyExp == "dada":
            srcCode = srcCode.replace("dada", ")",5)
        elif babyExp == "b":
            srcCode = srcCode.replace("b", "0",5)
        elif babyExp == "ba":
            srcCode = srcCode.replace("ba", "1",5)
        elif babyExp == "baa":
            srcCode = srcCode.replace("baa", "2",5)
        elif babyExp == "baaa":
            srcCode = srcCode.replace("baaa", "3",5)
        elif babyExp == "baaaa":
            srcCode = srcCode.replace("baaaa", "4",5)
        elif babyExp == "baaaaa":
            srcCode = srcCode.replace("baaaaa", "5",5)
        elif babyExp == "baaaaaa":
            srcCode = srcCode.replace("baaaaaa", "6",5)
        elif babyExp == "baaaaaaa":
            srcCode = srcCode.replace("baaaaaaa", "7",5)
        elif babyExp == "baaaaaaaa":
            srcCode = srcCode.replace("baaaaaaaa", "8",5)
        elif babyExp == "baaaaaaaaa":
            srcCode = srcCode.replace("baaaaaaaaa", "9",5)
    return srcCode



