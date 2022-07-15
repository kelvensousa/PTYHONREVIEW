#Faça um programa que convertar graus.
# ºF em ºC, ºC em ºF, ºF em K, K em ºC, K em ºF e ºC em K.

#(0 °F − 32) × 5/9 =  formula from °F to ºC.
#(0 °C × 9/5) + 32 =  formula from °C to ºF.
#0 °C + 273,15 =      formula from ºC to K.
#(0 °F − 32) × 5/9 + 273,15 = formula from ºF to K.
#(0 K − 273,15) × 9/5 + 32 = formula from K to °F.
#(303 K − 273,15) = formula from k to ºC.

celsius = float(input("Enter with value ºC: "))
fahrenheit = float(input("Enter with value ºF: "))
kelvin = float(input("Enter with value ºK: "))
print(f'{fahrenheit} ºF to {(fahrenheit - 32) * 5/9:.1f} ºC.')
print(f'{celsius} ºC to {(celsius * 9/5) + 32:.1f} ºF.')
print(f'{celsius} ºC to {(celsius + 273.15):.1f} K.')
print(f'{fahrenheit} ºF to {(fahrenheit - 32) * 5/9 + 273.15:.1f} K.')
print(f'{kelvin} K to {(kelvin - 273.15) * 9/5 + 32:.1f} ºF.')
print(f'{kelvin} K to {(kelvin - 273.15):.1f} ºC.')


