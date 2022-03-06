import math

a, b, c = input().split(" ")
maiorAB = (int(a) + int(b) + abs(int(a)-int(b))) / 2

if int(maiorAB) > int(c):
    print("{} eh o maior".format(int(maiorAB)))
else:
    print("{} eh o maior".format(int(c)))