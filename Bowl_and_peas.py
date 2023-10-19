n = int(input())
m = 1
for i in range(0,n):
    x , y = map(int,input().split(" "))
    if m == x:
        m = y
    elif m == y:
        m = x
print(m)
    