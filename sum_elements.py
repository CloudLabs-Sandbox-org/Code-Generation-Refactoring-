import sys

MAX = 100

#A poorly written example of a program in Python. It prompts the user for the number of elements to sum, takes those integers as input, and handles some basic error cases
def get_number_of_elements():
   while True:
      try:
         n = int(input("Enter the number of elements (1-100): "))
         if 1 <= n <= MAX:
            return n
         else:
            print("Invalid input. Please provide a number ranging from 1 to 100.")
      except ValueError:
         print("Invalid input. Please enter a valid integer.")

def get_elements(n):
   arr = []
   print(f"Enter {n} integers:")
   for _ in range(n):
      while True:
         try:
            arr.append(int(input()))
            break
         except ValueError:
            print("Invalid input. Please enter a valid integer.")
   return arr
   
def main():
   n = get_number_of_elements()
   arr = get_elements(n)
   print(f"Sum of the elements: {sum(arr)}")

if __name__ == "__main__":
   main()