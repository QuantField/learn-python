import time, logging
logging.basicConfig(filename="timing_log.log", level= logging.INFO)



def outer_func(input_func):
    def inner_func():
        print("I am decorating")
        return input_func()
    return inner_func


def echoHi():
    print("Hi")

# version one
myfunc = outer_func(echoHi)
myfunc()

# version two (same as on)
@outer_func
def echoHi():
    print("Hello")

echoHi()
#-------------------------------------------------------------------------------
# now wiht input argument
def outer_func_args(input_func):
    def inner_func(*args,**kwargs):
        print("I am decorating")
        return input_func(*args, **kwargs)
    return inner_func

print()
def echoHi(msg):
    print(msg)

myfunc = outer_func_args(echoHi)
myfunc("Hi, I am an arg")

@outer_func_args
def echoHi(msg):
    print(msg)

echoHi("Hello, me too")

#=========================================================

print("timing decorator")
def timit(input_func):
    def inner_func(*args,**kwargs):
        t1 = time.time()
        result = input_func(*args, **kwargs)
        t2 = time.time()-t1
        dt= time.strftime("%H:%M:%S", time.gmtime(t2))
        logging.info("elapsed time :{}".format(dt))
        return result 
    return inner_func

@timit
def func(n):
    return sum(range(n))

print(func(1000000000))    


