def annual_net_income(gross_salary):
    # complete your function implementation here...
    if gross_salary >= 45000:
        net_salary = gross_salary * (1 - 0.5)
    elif gross_salary >= 30000 and gross_salary < 45000:
        net_salary = gross_salary * (1 - 0.3)
    elif gross_salary < 30000:
        net_salary = gross_salary * (1 - 0.15)
    return net_salary

print(annual_net_income(60000)) #Outputs 30000
print(annual_net_income(30000)) #Outputs 21000
print(annual_net_income(20000)) #Outputs 17000



