total=int(input("digite a quantia de reais desejada: "))
nota100=total/100
restante=total%100
nota50=restante/50
restante=restante%50
nota20=restante/20
restante=restante%20
nota10=restante/10
restante=restante%10
nota5=restante/5
restante=restante%5
nota2=restante/2
restante=restante%2
nota1=restante/1
nota100=int(nota100)
nota50=int(nota50)
nota20=int(nota20)
nota10=int(nota10)
nota5=int(nota5)
nota2=int(nota2)
nota1=int(nota1)


print(nota100,"nota(s) de R$100,00")
print(nota50,"nota(s) de R$50,00")
print(nota20,"nota(s) de R$20,00")
print(nota10,"nota(s) de R$10,00")
print(nota5,"nota(s) de R$5,00")
print(nota2,"nota(s) de R$2,00")
print(nota1,"nota(s) de R$1,00")