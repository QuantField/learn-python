
# search in a list if found return position of element else return -1
s = [3,5,6,7,8,8,9]
search_val = 10

def fn(x):
    for i,r in enumerate(s):
        if r==x:
            return i
    else:
        return -1

print(fn(search_val))