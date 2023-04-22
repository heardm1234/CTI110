# Generatoring random numbers 
# 21 APR 23
# CTI-110 P5HW - Math Quiz
# Mallory Heard
#
import random
count = 1


print('Welcome to Math Quiz')

def main_menu():
  print()
  print('MAIN MENU')
  print('--------------------')
  print('1. Adding Random Numbers')
  print('2. Subtracting Random Numbers')
  print('3. Exit')

quit_program = False

while not quit_program :
  main_menu()
  option = int(input('Please choose one of the menu options:  '))
  if option == 3:
    print('Thank you for playing... \nBye!!')
    quit_program = True
  else:
    if option == 1:
      num1 = random.randint(1,150)
      num2 = random.randint(1, 150)
      
      print(' ',num1, '\n+', num2, end='') 
      option = int(input('\nEnter Answer.'))  
      product = num1+num2
      while option < product:
        print('Sorry, guess is too low.')
        count += 1
        print()
        option = int(input('Try Again: '))
      while option > product:
        print('Sorry, guess it too high.')
        count += 1
        print()
        option = int(input('Try Again: '))
      else:
        print('Congradulations!!!!! Your answer is correct')
        print('Number of guesses:', count)
    
    elif option == 2:
      num1 = random.randint(100,150)
      num2 = random.randint(1, 99)
      
      print(' ',num1, '\n-', num2, end='') 
      option = int(input('\nEnter Answer.'))
      product = num1-num2
      while option < product:
        print('Sorry, guess is too low.')
        count += 1
        print()
        option = int(input('Try Again: '))
      while option > product:
        print('Sorry, guess it too high.')
        count += 1
        print()
        option = int(input('Try Again: '))
      else:
        print('Congradulations!!!!! Your answer is correct')
        print('Number of guesses:', count)
        
      print()
    
    


