numbers = []

count = 0;
while count < 5:
    temp = int(input('Enter a number: '))
    numbers.append(temp)
    count += 1
    
def even_or_odd(num):
    if num % 2 != 0:
        print(str(num) + ' is an odd number.')
    else:
        print(str(num) + ' is an even number.')
        
        
print('\n\n')
        
def main():
    for num in numbers:
        even_or_odd(num)

main()
