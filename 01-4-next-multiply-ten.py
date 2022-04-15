# Calculate next multiply 10

myNum = int(input('Enter a number : '))
result = 0;

if(myNum <= 0) : 
    print('Entry number is out of Range:')
    exit();

if(myNum % 10 ) == 0 :
    result = myNum + 10;

# elif(myNum < 10) :
#         result = 10;

else :
    result = ((myNum // 10) * 10) + 10;


    
print('Next multiply of ten :', result)
‍‍‍‍‍


