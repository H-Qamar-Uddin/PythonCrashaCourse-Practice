from car import car
from car import country
car1 = car("Yaris",2011,1200,"Toyota")
car2 = car("Hyundai i30", 2015, 1400, "Hyundai" )
print(car1.c_name)
print(car2.c_model)
print(car1.cc_engine)
print(car2.comp_name)
country1 = country("Finland", +358, "Europe","5.6m", "Finnish",True)
country2 = country("Pakistan", +923,"Asia","222m", "Urdu",False)
print(country1.country_name)
print(country1.phone_code)
print(country1.is_on_map)
print(country1.continent)
print(country2.country_name)
print(country2.population)
print(country2.continent)
print(country2.language)
print(country2.is_on_map)
