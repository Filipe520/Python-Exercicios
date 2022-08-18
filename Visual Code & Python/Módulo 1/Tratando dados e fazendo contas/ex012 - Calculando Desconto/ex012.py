produto = float(input('Qual é o preço do produto? R$'))
desconto = (produto * 5) / 100
print(f'O produto que custava R${produto:.5}, na promoção com desconto de 5% vai custar R${produto - desconto:.5}')