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
    return (elapsed * 1000, ret)

print(total(1000, pow, 2, 1000)[0])
print(sys.platform[:3])

def bestof(reps, func, *pargs, **kargs):
    """
    Возвращает лучшее время, последний результат
    """
    best = 2 ** 32
    for i in range(reps):
        start = timer()
        ret = func(*pargs, **kargs)
        elapsed = timer() - start
        if elapsed < best: best = elapsed
    return (best * 1000, ret)

print(bestof(1000, pow, 2, 1000)[0])


def bestoftotal(reps1, reps2, func, *pargs, **kargs):
    """
    Лучшее сумарное время
    """
    return bestof(reps1, total, reps2, func, *pargs, **kargs)

print(bestoftotal(50, 1000, str.upper, "spam"))
