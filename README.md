This is a Numerov 1D Schrödinger equation solver, it can simulate transmission through arbitrary potential.

### General problem
```math
\frac{\hbar^{2}}{2m}\partial_{x}^{2}\psi(x)+V(x)\psi(x)=E\psi(x)
```
![](https://github.com/virshlee/numerov/blob/main/wavefunc1.png)

```math
$$\psi_{1}(x)=A e^{i k_{0}x}+B e^{-i k_{0}x}\qquad\psi_{3}(x)=C e^{i k_{0}x}+D e^{-i k_{0}x}$$
```
### Features

* Transmissions can be plotted.
* Wavefunctions can be also plotted, I attached two of these as well.
* The transmission is calclated from a system of linear equations, I added "n" index difference because first I thought I would get singular matrix from adjacent sampling points.


My results are attached in the folder.

![](https://github.com/virshlee/numerov/blob/main/wavefunc1.png)
![](https://github.com/virshlee/numerov/blob/main/wavefunc2.png)
![](https://github.com/virshlee/numerov/blob/main/gauss_potnergy.png)
![](https://github.com/virshlee/numerov/blob/main/gauss_parenergy.png)
