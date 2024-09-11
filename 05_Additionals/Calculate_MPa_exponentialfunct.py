import numpy as np
import matplotlib.pyplot as plt

# numbers taken from Räsänen et al. :
x1 = 1.3 # lowest UPV 
y1 = 20 # lowest MPa

x2 = 3.5 # highest UPV
y2 = 80 # highest MPa

UPV_results = [1.4, 3.5, 3.5, 1.8, 3.0]


def calc_a_b(x1, y1, x2, y2) :

    # function : y = a * e^(b*x)  
    # if x1 = 0.7, y1 = 3, x2 = 7.9, y2 = 92
    # 3 =  a * e^(b*0.7)  
    # 92 =  a * e^(b*7.9)
    # 92 / 3 = a * e^(b*7.9) / a * e^(b*0.7)
    # 92 / 3 = e^(b*(7.9 - 0.7))

    b = np.log(y2 / y1) / (x2 - x1)
    a = y1 / np.exp(b * x1)
    return a, b


def upv_to_mpa(upv, a, b):
    mpa = a * np.exp(b * upv)
    return max(min(mpa, 90), 0)

def test_conversion():
    a, b = calc_a_b(x1, y1, x2, y2)

    upv_values = np.linspace(0.5, 4.0, 100)
    mpa_values = [upv_to_mpa(upv, a, b) for upv in upv_values]
    # visualise function in plot
    plt.figure(figsize=(10, 6))
    plt.plot(upv_values, mpa_values)
    plt.xlabel("UPV [km/s]")
    plt.ylabel("Druckfestigkeit [MPa]")
    plt.title("Umrechnung von UPV zu Druckfestigkeit (MPa)")
    plt.grid(True)
    plt.show()
    plt.close()
    
    for upv in UPV_results :
        print(f"Test Result UPV : {upv} km/s, Compressive Strength : {upv_to_mpa(upv, a, b):.2f} MPa")

test_conversion()