#Numlistgen v0.2 by Riccardo3000
#Questo script genera un elenco di numeri in ordine crescente.

n = int(input('inserire il numero finale: '))
n1 = int(input('Inserire il numero di partenza: ' ))

for i in range(n+1):
  if i >= n1:
    print(i)

input('per uscire, scrivere "z".')
if input == 'z':
  quit()
