def Initials(first_name,middle_name,surname):
  if middle_name is not None:
    code = first_name[0] + middle_name[0] + surname[0]
    code = code.upper()
  else:
    code = first_name[0] + "Z" + surname[0]

  return code

first_name = "John"
middle_name = None
surname = "Smith"

print("your username is" , Initials(first_name , middle_name , surname))
