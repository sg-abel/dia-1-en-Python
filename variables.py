import math

print('Day 2: 30 days of python programming')
first_name = 'abel'
print(type(first_name))
last_name = 'Salazar'
print(type(last_name))
full_name = 'Abel Salazar Galindo'
print(type(full_name))
country = 'Mexico'
print(type(country))
city = 'Ciudad Juarez'
print(type(city))
Age = 36
print(type(Age))
year = 2014
print(type(year))
is_married = True
print(type(is_married))
is_light_on = True
print(type(is_light_on)) 
hijas, trabajo, cuenta_face, nick_name = 2, True, 'si', 'Abelito'
print(type(hijas),type(trabajo),type(cuenta_face),type(nick_name))

print('Numero de letras en primer nombre: ', len(first_name))
print('Numero de letras en el Apeliido: ', len(last_name))

num_one = 5
print('Valor uno: ', num_one)
num_two = 4
print('valor dos: ', num_two)
suma = num_one + num_two
print('la suma es: ', suma)
resta = num_one - num_two
print('la resta es: ', resta)
multiplicacion = num_one * num_two
print('La multiplicacion es: ', multiplicacion)
division = num_one / num_two
print('division es: ', division)
exp = num_one ** num_two
print('exponecial es:', exp)
floor_division = num_one // num_two
print('residuo de division: ', floor_division)

print('Circulo: Area, Circunferencia y Radio de 30 metros')
radio = 30
area_of_circle = ( math.pi * (radio ** 2))
print('El area es: ', area_of_circle)
circum_of_circle = 2 * math.pi * radio
print('La circunferencia es: ', circum_of_circle)
radio_de_usuario = int(input('Escribe el radio del circulo: '))
area_new = (math.pi * (radio_de_usuario ** 2))
print('el area es: ', area_new)

first_name = input('Escribe tu nombre: ')
last_name = input('escribe tu apellido: ')
country = input('Escribe tu pais: ')
Age = input('escribe tu edad: ')



