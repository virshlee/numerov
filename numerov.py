import numpy as np
import matplotlib.pyplot as plt


def externalPotential(x, welldepth, wellwidth):
    """
    :param x: x coordinate in l0 unit
        :param welldepth: depth in eV
        :param wellwidth: width in nm
        :return: gives back the value of potential at x
    """
    if abs(x) > wellwidth / 2 / l0:
        return 0
    return -welldepth

"""
def externalPotential(x, welldepth, wellwidth):
    return -welldepth*np.exp(-x**2/((wellwidth/l0)**2))

"""


def k2(energy, x, depth, width):
    """
    Calulates k^2, as in solving Schroedinger equation
    """
    return 2 * (energy - externalPotential(x, welldepth=depth, wellwidth=width))


def trans(E, welldepth, wellwidth):
    return 1 / (1 + welldepth ** 2 / (4 * E * (E - (-welldepth))) * (
        np.sin(2 * np.sqrt(2 * (E - (-welldepth))) * (wellwidth / 2 / l0))) ** 2)


def numerov(xVals, energy, depth, width, xMax, xMin, N):
    """
    Calculates the values of the wavefunction in i*dx positions
    """
    k2Vals = [k2(energy, xVals[i], depth, wellwidth) for i in range(N + 1)]
    phiVals = [None] * (N + 1)
    phiVals[1] = 1
    phiVals[0] = np.exp(-1j * h * np.sqrt(2 * energy))
    for i in range(1, N):
        prevPhiHat = (1 + (1 / 12) * (h ** 2) * k2Vals[i - 1]) * phiVals[i - 1]
        nextPhiHat = (2 - (5 / 6) * (h ** 2) * k2Vals[i]) * phiVals[i] - prevPhiHat
        phiVals[i + 1] = nextPhiHat / (1 + (1 / 12) * (h ** 2) * k2Vals[i + 1])
    phiVals.reverse()
    return phiVals


def getTransmission(xVals, phiVals, energy):
    """
    Calculates the transmission from the wavefunction
    """
    phi1 = phiVals[0]
    n = 1
    phi2 = phiVals[n]
    M = np.array([[np.exp(-1j * np.sqrt(2 * energy) * xVals[0]), np.exp(1j * np.sqrt(2 * energy) * xVals[0])],
                  [np.exp(-1j * np.sqrt(2 * energy) * xVals[n]), np.exp(1j * np.sqrt(2 * energy) * xVals[n])]])
    AB = np.linalg.solve(M, [phi1, phi2])
    A = AB[0]
    B = AB[1]
    return 1 / abs(A ** 2)


def plotTrueWaveFunctions(xVals, phiVals, title="Plot of Numerov Calculation"):
    plt.plot(xVals, [x.imag for x in phiVals], label='Imaginary part of $\phi$')
    plt.plot(xVals, [x.real for x in phiVals], label='Real part of $\phi$')
    plt.ylabel("Amplitude of Wave Function $\phi$, Potential")
    plt.title(title)
    plt.xlim(xMin, xMax)
    plt.xlabel("Positional Parameter $x$")
    plt.plot(xVals, [externalPotential(x, welldepth=welldepth, wellwidth=wellwidth) for x in xVals], label='Potential')
    plt.legend()
    plt.show()


if __name__ == '__main__':
    """
    Measurement units
    """
    hbar = 1.05e-34
    m0 = 9.11e-31
    l0 = 0.276e-9
    t0 = 0.658e-15

    """
    N: number of dxis
    xMin: minimal position in l0 unit
    xMax: maximal position in l0 unit
    resolution: number of steps in investigated energy interval
    interval: size of investigated energy interval in eVs
    welldepth: depth of potential in eV
    wellwidth: width of potential in nm
    """
    N = 1000
    xMin = -10
    xMax = 10
    resolution = 300
    interval = 4
    welldepth = 2
    wellwidth = 1e-9
    energy = 4
    transmissions = [None] * resolution
    analytical = [None] * resolution
    energies = [None] * resolution
    h = (xMax - xMin) / N
    xVals = [xMin + i * h for i in range(N + 1)]

    for i in range(1, resolution):
        dE = interval / (resolution - 1)
        energies[i] = i * dE
        phiVals = numerov(xVals=xVals, energy=i * dE, depth=welldepth, width=wellwidth, xMin=xMin, xMax=xMax, N=N)
        transmissions[i] = getTransmission(xVals=xVals, phiVals=phiVals, energy=i * dE)
        analytical[i] = trans(E=i * dE, wellwidth=wellwidth, welldepth=welldepth)
        # plotTrueWaveFunctions(xVals, phiVals)
    plt.plot(energies, transmissions, label="Numerov result")
    plt.plot(energies, analytical, label="Analytical result")
    plt.legend()
    plt.title("Transmission through squarewell")
    plt.xlabel("Potential depth [eV]")
    plt.ylabel("Transmission")
    plt.show()
