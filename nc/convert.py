def convert(filename):
    with open(filename) as fp:
        lines = fp.readlines()
    parts = [line.split() for line in lines]
    retval = []
    for bits in parts:
        try:
            d = {}
            code = bits[0]
            #d['code'] = code
            remainder = bits[1:]
            for word in remainder:
                arg = word[0]
                number = float(word[1:])
                d[arg.lower()] = number
            retval.append(d)
        except Exception, e:
            print e

    return retval
