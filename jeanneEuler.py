# ok voyons voir !!!

# problemes euler

#num 1
sum = 0
for i in range(1,1000):
    if i%3==0 or i%5==0:
        sum = sum + i
print(sum)

#num 2 bien brute force
avav = 1
av = 2
sum = 2
curent=3
while curent<4000000:
    curent = av + avav
    avav = av
    av = curent

    if curent<4000000 and curent%2==0:
        print(curent)
        sum = sum+curent

print("")
print(sum)

# num 3
