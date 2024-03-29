# Simple-Digital-Filter
Generate an original data
```math
t_i = \frac{20(i-1)\pi}{N-1}, 
y_i = \Sigma_{j=1}^{999} {sin(jt_i)}
```
with various frequencies sine wave, where $j$ is odd and $y_{N+1} = y_1$. 

## Low-pass filter
```math
z_{low} = \frac{1}{2}(y_k+y_{k+1}) 
```
## High-pass filter
```math
z_{high} = \frac{1}{2}(y_k-y_{k+1}) 
```

## Result
![Image](https://github.com/ChenYingShan1114/Simple-Digital-Filter/blob/main/filter.png)

### Reference
A. L. Garcia, "Numerical Methods for Physics": \
    Chapter 5 Analysis of Data \
The header file of **Matrix.h** and **fft.h** are from "Numerical Methods for Physics Second Edition -- Alejandro L. Garcia".
