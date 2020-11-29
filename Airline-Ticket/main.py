def ticket(city_1,city_2):
  city_1 = city_1[0:4]
  city_1 = city_1.upper()

  city_2 = city_2[0:4]
  city_2 = city_2.upper()

  result = city_1 + "-"  + city_2
  return result


print(ticket("London" , "Madrid"))

