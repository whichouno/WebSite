# b=6
# print(4<b<7)
# print(1==b<20)
#
# a= [1,2,3,4,5]
# for e in a:
#     print(e)
#     if e == 3:
#         break
# else:
#     print("no break")



def debug(func):
    def wrapper(*args,**kwargs):
        print("[DEBUG]: enter {}()".format(func.__name__))
        return func(*args,**kwargs)
    return wrapper

@debug
def say_hello(something):
    print("hello {}!".format(something))


say_hello('world')