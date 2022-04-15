# Calculate (mirror of a number) * 2

myNum = int(input('Input a Number :'));
num = myNum;
mirrorNum = '';
result = 0;

while(num>0) :

    divideRemaining = num % 10;
    mirrorNum = mirrorNum + str(divideRemaining);
    num //= 10;

   
result = int(mirrorNum) * 2;

print('---------------------------------')
print('Mirror Number = ', mirrorNum);

print('---------------------------------')
print('Result =>', mirrorNum, '* 2 ='  , result);




