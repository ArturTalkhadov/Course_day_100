print("Привет, это калькулятор чаевых.")
total=float(input("Какова итоговая сумма в чеке? "))
proc=float(input("Какой процент от суммы вы хотите отдать в виде чаевых? "))
many_peopl=int(input("На сколько человек делим счет? "))

print(f"Каждый должен заплатить по: {round(((total + (total * (proc/100) ))  / many_peopl),2)} рублей")
