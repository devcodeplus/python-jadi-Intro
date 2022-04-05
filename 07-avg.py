# Calculate Average : While loop

num = 0 ;
count = 0;
sum = 0;

print('Enter -1 for End of Entry ...')

while(num != -1) :
  num = int(input('Enter a number :'));

  if(num != -1) :
    sum = sum + num;
    count = count + 1 ; 


avg = sum / count ;

print('Sum = ', sum);
print('Average = ', avg);

  



