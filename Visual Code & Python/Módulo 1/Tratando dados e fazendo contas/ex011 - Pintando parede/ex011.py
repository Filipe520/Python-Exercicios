print('-=-' * 15)
larg = float(input('Largura da parede: '))
alt = float(input('Altura da parede: '))
print('-=-' * 15)

area = (larg * alt)

print(f'Sua parede tem a dimensão de {larg}x{alt} e sua área é de {area}m².')

tinta = area / 2

print(f'Para pintar essa parede, você precisará de {tinta}l de tinta.')