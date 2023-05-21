
# This function is used to write to a file
def file (equation):
   with open("equations.txt", "a") as f:
        f.write(equation + '\n')

# These if-elif-else statements are used to perform calculations 
def calculator(number1, number2, operation):

    if operation == "+":
        answer = number1 + number2

    elif operation == "-":
        answer = number1 - number2

    elif operation == "*":
        answer = number1 * number2
        
    elif operation == "/":
        answer = number1 / number2
    else:
      answer = None
    return answer

# Body of the program and it makes effective use of defensive programming
while True:
        
  make_a_choice  = input('Do you want to enter two numbers and an operator (1) or read equations from a file (2)? (choose number "1" or "2"): ')
  if make_a_choice == '1':
        try:
            number1 = float(input("Enter a number: "))

            number2 = float(input("Enter a number: "))

            operation = input("Enter the arithmetic operation you would like to perform (+, -, *, /): ")

            answer = calculator(number1, number2, operation)

            if operation == "+, -, *, /":
                print("answer:", answer)

                equation = f"{number1} {operation} {number2} = {answer}"
                file(equation)  
            else:
                print("Invalid operation")

        except ValueError:
            print("Invalid input!")

        except ZeroDivisionError:
            print("Cannot divide by zero!")

        except Exception as e:
            print(f"An error occurred: {e}")

  elif make_a_choice == "2":
        
        while True:
            filename = input("Enter file name: ")

            try:
                with open(filename, "r") as f:
                    equations = f.readlines()

                    for item in equations:
                        numbers, operation, answer = item.split("=")
                        number1, number2 = map(float, numbers.split())
                        print(f"{number1} {operation} {number2} = {answer.strip()}")
                break
            except FileNotFoundError:
                print(f"File {filename} not found!")
            except Exception as e:
                print(f"An error occurred: {e}")
  else:
    print("Invalid choice!")
    continue

  make_a_choice = input("Do you want to perform another calculation or read equations from a file? (choose y or n): ")
  if make_a_choice.lower() != "y":
    break