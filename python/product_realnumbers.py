n = int(input('Enter the number of real numbers : '))
i=0
pro=1
for i in range(n):
    num=float(input('Enter the number : '))
    pro=pro*num

print('Product of the number is :',pro)