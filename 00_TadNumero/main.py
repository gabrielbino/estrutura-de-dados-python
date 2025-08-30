from class_numero import Numero

numero = Numero()

while True:
  print("================================")
  print("     Estudo do TAD Número")
  print("================================")
  print("0 - encerrar")
  print("1 - ler valor")
  print("2 - atribuir valor")

  opc = int(input("Qual é sua opção? "))

  if (opc == 0):
    break
  elif opc == 1:
    print("\n\n", numero.valor,"\n\n")
  elif opc == 2:
    v = float((input("Forneça o novo valor: ")))
    numero.valor = v

print("--- FIM ---")
print("Até a próxima!")