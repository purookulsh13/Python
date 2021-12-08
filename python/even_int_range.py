for i in range(100,200):
    num=i
    sum=0
    while(num!=0):
        temp=num%10
        sum=sum+temp
        num=num//10
    if(sum%2==0):
        print(i)


