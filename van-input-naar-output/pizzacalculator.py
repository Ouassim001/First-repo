print("----------------------------------------------")

print("pizza small kost 5$")
print("pizza medium kost 8$")
print("pizza large kost 10$")
pizzasmall = int(input("hoeveel pizza small wil je? "))
pizzamedium = int(input("hoeveel pizza medium wil je? "))
pizzalarge = int(input("hoeveel pizza large wil je? "))
pricesmall = (pizzasmall * 5)
pricemedium = (pizzamedium * 8)
pricelarge = (pizzalarge * 10)

print("de prijs van uw bestelling is dan " + str(pricesmall + pricemedium + pricelarge) + " euro")
