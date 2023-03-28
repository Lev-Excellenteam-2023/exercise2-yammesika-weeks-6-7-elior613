import time
def timer(func, *arg):
    start=time.time()
    func(*arg)
    return time.time()-start
