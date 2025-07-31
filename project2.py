from multiprocessing import Pool, cpu_count
from time import time
def divider(num):
    result =[]
    for i in range(1 , num+1) :
        if num % i ==0:
            result.append(i)
    return result

def factorize(*args):
    result=[]
    for num in args:
        a = divider(num)
        result.append(a)
    return result

def measurement_time(*args):
    start = time()
    factorize(*args)
    return time() - start

def in_parallel(*args):
    n = cpu_count()
    with Pool(n) as pool:
        result=pool.map(divider,args)
        return result
if __name__ == "__main__":
    print(factorize(128, 255, 99999, 10651060))
    print(in_parallel(128, 255, 99999, 10651060))

    print("Синхронно", measurement_time(128, 255, 99999, 10651060))

    start = time()
    in_parallel(128, 255, 99999, 10651060)
    print("Паралельно:", time() - start)