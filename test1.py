d = 0
a = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
b = ["SUN", "MON","TUE", "WED", "THU", "FRI", "SAT"]
 
x, y = map(int,input().split())
 
for i in range(x-1):
    d = d + a[i]
d = (d + y) % 7
 
print(b[d])