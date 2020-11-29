def check(address):
  x = address.find("@")
  if x != -1:
    print("valid")

  x = address.find(".")
  if x != -1:
    print("valid")
  else:
    print("invalid")

  
check("bobsmithgmail.com")