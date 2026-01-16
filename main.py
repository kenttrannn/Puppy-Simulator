#Kent Tran, Matthew Trinh
#Group 2
#December 3, 2025
#Puppy Simulator

import check_input
from puppy import Puppy

def main():
  print("Congratulations on your new puppy!")

  my_puppy = Puppy()

  while True:
    print("\nWhat would you like to do?")
    print("1. Feed the puppy")
    print("2. Play with the puppy")
    print("3. Quit")

    choice = check_input.get_int_range("Please enter your choice: ", 1, 3)

    if choice == 1:
      reaction = my_puppy.give_food()
      print(reaction)
    elif choice == 2:
      reaction = my_puppy.throw_ball()
      print(reaction)
    else:
      break
      
main()