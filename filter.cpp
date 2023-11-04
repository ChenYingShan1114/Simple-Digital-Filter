#include <iostream>
#include <fstream>
#include <math.h>
#include "Matrix.h"
#include "fft.h"
using namespace std;

int main(){
    const double pi = 3.1415926;
    int N = 32768;
    Matrix x(N), y(N), imag(N);

    for (int i = 1; i <= N; i++ ){
        imag(i) = 0;
        x(i) = (i - 1) * 20 * pi / (N - 1);
        for (int j = 1; j <= 999; j=j+2){
            y(i) = y(i) + sin(j * x(i));
        }
    }

    Matrix z_low(N), z_high(N), z_low_imag(N), z_high_imag(N);
    for (int i = 1; i <= N-1; i++ ){
        z_low(i) = 0.5 * (y(i) + y(i+1));
        z_high(i) = 0.5 * (y(i) - y(i+1));
        z_low_imag(i) = 0;
        z_high_imag(i) = 0;
    }
    z_low(N) = 0.5 * (y(N) + y(1));
    z_high(N) = 0.5 * (y(N) - y(1));

    ofstream y_plotOut("y_plot.txt");
    for (int i = 1; i <= N; i++ ){
        y_plotOut << x(i) << "," << y(i) << endl;
    }

    fft(y, imag);
    ofstream y_fft_plotOut("y_fft_plot.txt");
    for (int i = 1; i <= N; i++){
        y_fft_plotOut << y(i) << "," << imag(i) << endl;
    }

    ofstream zlow_plotOut("zlow_plot.txt");
    for (int i = 1; i <= N; i++ ){
        zlow_plotOut << x(i) << "," << z_low(i) << endl;
    }
    
    fft(z_low, z_low_imag);
    ofstream zlow_fft_plotOut("zlow_fft_plot.txt");
    for (int i = 1; i <= N; i++){
        zlow_fft_plotOut << z_low(i) << "," << z_low_imag(i) << endl;
    }

    ofstream zhigh_plotOut("zhigh_plot.txt");
    for (int i = 1; i <= N; i++ ){
        zhigh_plotOut << x(i) << "," << z_high(i) << endl;
    }
    
    fft(z_high, z_high_imag);
    ofstream zhigh_fft_plotOut("zhigh_fft_plot.txt");
    for (int i = 1; i <= N; i++){
        zhigh_fft_plotOut << z_high(i) << "," << z_high_imag(i) << endl;
    }

}
