import time, sys
timer = time.perf_counter if sys.platform[:3] == 'win' else time.time

def total(reps, func, *pargs, **kargs):
    """
    Возвращает суммарное время, последний результат
    """
    repslist = list(range(reps))
    start = timer()
    for i in repslist:
        ret = func(*pargs, **kargs)
    elapsed = timer() - start
    return (elapsed, ret)

print(total(1000, pow, 2, 1000))
print(sys.platform[:3])
