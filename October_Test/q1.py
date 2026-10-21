print('To check whether the number is harshad number or not')
num=int(input('Enter a number: '))

temp=num
sum=0

while num!=0:
    sum=sum+(num%10)
    num=num//10
if temp%sum==0:
    print(f"{temp} is HARSHAD number")
else:
    print(f"{temp} is not harshad")