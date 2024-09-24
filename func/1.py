def instens(seq1, seq2):
    res = []
    for i in seq1:
        if i in seq2:
            res.append(i)
    return res

x = 'spamM'
p = 'sram'
print(instens(x, p))