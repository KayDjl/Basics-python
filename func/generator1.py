def geq2(seq):
    if not seq:
        yield seq
    else:
        for i in range(len(seq)):
            rest = seq[:i] + seq[i+1:]
            for x in geq2(rest):
                yield seq[i:i+1] + x
                
g = list(geq2("liks"))
print(len(g))