menu = "Menu\n------------\n1. Encode\n 2. Decode\n 3. Quit
def main():
  while True:
    print(menu)
    option = int(imput("Please enter an option: ")
    password = imput("Please enter the password to encode")
    if option == 1:
      encode(password)
      print("Your password has been encoded and stored")
    elif option == 2:
      new_password = decode(password)
      print(f"The encoded password is {encode(password)}, and the original password is {new_password}") 
      
    elif option == 3:
      break
    
  
def encode(password):
  new_password = " "
  for char in password:
    new_char = str((int(char) + 3) % 10)
    new_password += new_char
  return new_password



  
  
    
