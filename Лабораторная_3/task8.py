money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05

month = 0  # количество месяцев, которое можно прожить

x = (money_capital) + (salary) - (spend)
month += -1
while True:
    spend = (spend) * (1 + increase)
    x = (x) + (salary) - (spend)
    if x > 0:
        month += 1
    else:
        break
print(month)
