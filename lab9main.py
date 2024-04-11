def encode(password):
  new_password = " "
  for char in password:
    new_char = str((int(char) + 3) % 10)
    new_password += new_char
  return new_password


    
