# Change in entry string ...

myString = input('Enter a string : ');
vowels = 'aeiou';
result = '';
i = -1;

for char in myString :
  index = vowels.find(char);
  i = int(i) + 1;

  if(index == -1) :
    result = result + "." + myString[i];

result = result.lower();
print('Result = ', result);




  
  
