# Smallest Factor of Integers Other Than 1
print("Finding the Smallest Factor of Integers n")
print("*****************************************")
def find_smallest_factor (n_value):
    if n_value < 2:
        return None
    factor = []
    for i in range(2, n_value + 1):
        if (n_value % i == 0):
            factor.append(i)
    factor.sort()
    return factor
n_value = int(input("Enter an integer >= 2:"))
result = find_smallest_factor(n_value)
if result:
    factor = result
    print("The smallest factor other than 1 for", n_value, "is", factor[0])
else:
    print("Invalid input. Please enter a number greater than 2.")