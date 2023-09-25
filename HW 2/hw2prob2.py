priceOfCar = float(input("Enter the price of the car: $"))
milesPerYear = float(input("Enter estimated miles driven per year: "))
priceOfGas = float(input("Enter the estimated price of gas (per gallon): $"))
efficiencyOfGas = float(input("Enter miles per gallon (MPG): "))
resaleValue = float(input("Enter estimated resale value after five years: $"))

# milesPerYear / efficiencyOfGas = number of gallons used
# number of gallons used * priceOfGas = price of drive
# milesPerYear / efficiencyOfGas = price of drive / priceOfGas
# priceOfGas * milesPerYear / efficiencyOfGas = price of drive

priceOfDrive = priceOfGas * milesPerYear / efficiencyOfGas
depreciation = priceOfCar - resaleValue

print(f'Cost of owning the car for five years: ${"%.2f" % (priceOfDrive + depreciation)}')