# function for addition
def add(n1, n2):
  return n1 + n2

## function for subtraction
def subtract(n1, n2):
  return n1 - n2

## function for multiplication
def multiply(n1, n2):
  return n1 * n2

## function for division
def division(n1, n2):
  return n1 / n2

def calculator():
#dictionary to call the addition , subtraction, multiplication,and division functions by there kay symbol
  cal = {"+" : add, "-": subtract, "*": multiply, "/": division}

  num1 = float(input("Enter the 1st number : "))
  keys = list(cal.keys())


  should_continue = True

  while should_continue:
    operation_symbol = input(f"Pick a symbol from {keys} : ")
    num2 = float(input("Enter the next number: "))
    answer = cal[operation_symbol](num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")
    continue_process = input(f"Type 'y' to continue with {answer} or type 'n' to exit: ")
    if continue_process == 'y':
      num1 = answer
    elif continue_process == 'n':
      should_continue = False
      break
      calculator()
    
calculator()