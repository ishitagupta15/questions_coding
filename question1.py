#Ques: A central power plant, rated at 800,000 kW, generates steam at 585 K and discards heat to a river at 295 K. If the thermal efficiency of the plant is 70% of the maximum possible value, how much heat is discarded to the river at rated power?
print("Enter the power generated by the power plant in kW")
power= int(input())
print("Enter the temperature of power plant in Kelvin")
Th=int(input())
print("Enter the temperature of the river in Kelvin")
Tc=int(input())
print("Enter the thermal efficiency of the power plant in percentage")
te=int(input())
print("\nThe actual thermal efficiency is given by:\nη = (1 - Temperature of river/Temperature of power plant) X thermal efficieny")
print("η = (1 - Tc/Th) X te")
n=(1 - Tc/Th)*te/100
print("η =", n)
print("Using 1st Law:")
print("ΔU = Q + W\nΔU = 0 and Q = Qh + Qc\nTherefore,\nW = −Qh − Qc\nQc = (1−η/η) X W")
Qc=((1-n)/n)*power
print("Qc =", Qc,"kW")