This is a Numerov 1D Schrödinger equation solver, it can simulate transmission through an arbitrary potential.

### General problem
```math
\frac{\hbar^{2}}{2m}\partial_{x}^{2}\psi(x)+V(x)\psi(x)=E\psi(x)
```
<img src="https://github.com/virshlee/numerov/blob/main/schprob.png" width=50% height=50%>

```math
$$\psi_{1}(x)=A e^{i k_{0}x}+B e^{-i k_{0}x}\qquad\psi_{3}(x)=C e^{i k_{0}x}+D e^{-i k_{0}x}$$
```
Transmission thorugh square well is analytical:
```math
$$T=\frac{1}{1+\frac{V_{0}^{2}}{4E(V_{0}-E)}\sinh^{2}2\kappa_{2}a}$$
```
### Features

* Transmissions can be plotted.
* Wavefunctions can be also plotted, I attached two of these as well.
* The transmission is calclated from a system of linear equations, I added "n" index difference because first I thought I would get singular matrix from adjacent sampling points.


### Simulated results

![](https://github.com/virshlee/numerov/blob/main/gauss_potnergy.png)
![](https://github.com/virshlee/numerov/blob/main/gauss_parenergy.png)

<img src="https://github.com/virshlee/numerov/blob/main/wavefunc1.png" width=50% height=50%>
<img src="https://github.com/virshlee/numerov/blob/main/wavefunc2.png" width=50% height=50%>
