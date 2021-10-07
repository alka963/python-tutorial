num = int(input('enter a number'))
temp = num
sum = 0
while(num>0):
    sum = sum + (num%10) * (num%10) * (num%10)
    num = num//10
if(temp == sum):
    print('armstrong number')
else:
    print('not armstrong number')
