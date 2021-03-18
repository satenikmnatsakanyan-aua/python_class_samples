def main():
  length = int(input("Ներմուծիր ուղղանկյան երկարությունը` "))
  width = int(input("Ներմուծիր ուղղանկյան լայնությունը` "))

  print("")

  current_width = 0
  while(current_width < width):
    current_length = 0
    
    while(current_length < length):
      if (current_width == 0 or current_width == width-1 or current_length == 0 or current_length == length-1):
        print("*", end="")
      else:
        print(" ", end="")
      
      current_length = current_length + 1

    print("")
    current_width = current_width + 1

main()