import numpy as np
import matplotlib.pyplot as plt

date = 240828

# numbers taken from Dizhur et al. :
x1 = 0.7 # lowest UPV 
y1 = 10 # lowest MPa

x2 = 2.2 # highest UPV
y2 = 40 # highest MPa

UPV_results = [1.5, 1.1, 0.7, 0.7, 0.8, 1.4]


def calc_m_c(x1, y1, x2, y2) :

    # y = m*x+c

    m = (y2 - y1) / (x2 - x1)  
    c = y1 - m * x1           
    return m, c


def upv_to_mpa_linear(upv, m, c):
    mpa = m * upv + c
    return max(min(mpa, 90), 0)


def test_conversions_linear():
    m, c = calc_m_c(x1, y1, x2, y2)

    upv_values = np.linspace(0.5, 4.0, 100)
    mpa_values = [upv_to_mpa_linear(upv, m, c) for upv in upv_values]

    plt.figure(figsize=(10, 6))
    plt.plot(upv_values, mpa_values)
    plt.xlabel("UPV [km/s]")
    plt.ylabel("Compressive Strength [MPa]")
    plt.title("Relation between UPV (km/s) and Compressive Strength (MPa)")
    plt.grid(True)

    plt.savefig(f"{date}_Linearfunction_MPa.png")
    plt.show()
    plt.close()

    for upv in UPV_results :
        print(f"Test Result UPV : {upv} km/s, Compressive Strength : {upv_to_mpa_linear(upv, m, c):.2f} MPa")

test_conversions_linear()