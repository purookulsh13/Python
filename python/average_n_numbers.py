n = int(input('Enter the number of variables : '))
i=1
sum=0
for i in range(n):
    num=int(input('Enter the number : '))
    sum=sum+num

avg = sum/n
print('Average of the give number is :',avg)