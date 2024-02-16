from temp import evaluate_equation

Equation = input("Enter The Equation: ")
upper_limit = float(input("Enter Upper Limit: "))
lower_limit = float(input("Enter Lower Limit: "))
decimals = int(input("Enter the Decimal Accuracy: "))
n = float(input("Enter the Number of Divisions: "))
h = (upper_limit - lower_limit)/n

dict_of_values = {}
i = lower_limit
while(i<=upper_limit):
    if i == 0.9999999999999999:
        i = 1.0
    dict_of_values[i] = evaluate_equation(Equation, i)
    i += h

print(dict_of_values)
result = (h/2) * (dict_of_values[lower_limit]+ dict_of_values[upper_limit])
i = lower_limit + h
while(i<=upper_limit-h):
    result += h*dict_of_values[i]
    i += h

print(round(result,decimals))

