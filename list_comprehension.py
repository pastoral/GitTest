prizes = [5,10,20,40,80,160]
dbl_prizes = []

for prize in prizes:
    dbl_prizes.append(prize*2)
print(dbl_prizes)

#comprehensive way
dbl_prizes = [prize*2 for prize in prizes ]
print(dbl_prizes)


nums = [1,2,3,4,5,6,7,8,9,10]
squared = []

for num in nums:
    if num%2==0:
        num = num**2
        squared.append(num)
print(squared)

#comprehensive way
squared = [num**2 for num in nums if num%2 == 0]
print(squared)
print("eat pizza")

#map or functional way
def squaring(num):
    if num % 2 == 0:
        num = num ** 2
    else:
        return 
    return num

sl = list(map(squaring,nums))
print(sl)
print("done")