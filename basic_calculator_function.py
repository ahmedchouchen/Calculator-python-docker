def basic_calculator(a,b,operation):

  if (a.isnumeric() & b.isnumeric()):
    a=float(a)
    b=float(b)
    if operation == "+":
      result = a + b
    elif operation == "-":
      result = a - b
    elif operation == "/":
      result = a / b
    elif operation == "*":
      result = a * b
    else:
      result = "Operations supported: add +, sub -, div /, mult * only"
    
  else:
    result = "Please enter a valid number for a & b"
    

  return result
