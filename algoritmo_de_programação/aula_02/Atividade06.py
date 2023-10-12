pop1= float(input("Qual a população atual da cidade?"))
taxa1= float(input("E a taxa de crescimento anual?"))

pop2= float(input("Agora, a população de outra cidade:"))
taxa2= float(input("E sua taxa de crescimento anual:"))

cresc1= float (pop1*taxa1)+pop1
cresc2= float (pop2*taxa2)+pop2

print (f"O valor da população após 1 ano da primeira cidade é {cresc1} e da segunda é {cresc2}")
