
#initial and surname problefunction
def NameFormat(first_name, surname):
  username = first_name[0]
  username = username.upper()
#.upper() changes the string to all uppercase
  surname = surname.upper()

  username = username + "" + surname

  return username

#Outputs the required username and gives a value to NameFormat
print("your username is"   , NameFormat("123" , "Smith"))