import numpy as np
import matplotlib.pyplot as plt

import matplotlib as mpl
def format(fig):
    mpl.rcParams['font.family'] = 'STIXGeneral'
    plt.rcParams['xtick.labelsize'] = 19
    plt.rcParams['ytick.labelsize'] = 19
    plt.rcParams['font.size'] = 19
    plt.rcParams['figure.figsize'] = [5.6*6, 4*3]
    plt.rcParams['axes.titlesize'] = 18
    plt.rcParams['axes.labelsize'] = 18
    plt.rcParams['lines.linewidth'] = 2
    plt.rcParams['lines.markersize'] = 6
    plt.rcParams['legend.fontsize'] = 15
    plt.rcParams['mathtext.fontset'] = 'stix'
    plt.rcParams['axes.linewidth'] = 1.5
    # plt.style.use('dark_background')


def ax_format(ax, xmaj, xmin, ymaj, ymin):
    ax.xaxis.set_tick_params(which='major', size=5, width=1,
                            direction='in', top='on')
    ax.xaxis.set_tick_params(which='minor', size=3, width=1,
                            direction='in', top='on')
    ax.yaxis.set_tick_params(which='major', size=5, width=1,
                            direction='in', right='on')
    ax.yaxis.set_tick_params(which='minor', size=3, width=1,
                            direction='in', right='on')
    ax.xaxis.set_major_locator(mpl.ticker.MultipleLocator(xmaj))
    ax.xaxis.set_minor_locator(mpl.ticker.MultipleLocator(xmin))
    ax.yaxis.set_major_locator(mpl.ticker.MultipleLocator(ymaj))
    ax.yaxis.set_minor_locator(mpl.ticker.MultipleLocator(ymin))

freq_upper = 1000

fig1 = plt.figure(figsize=(16,8))
format(fig1)

x1_list = []
y1_list = []
with open("y_plot.txt") as f:
    for line in f.readlines():
        s = line.split(',')
        x1_list.append(float(s[0]))
        y1_list.append(float(s[1]))
x1 = np.array(x1_list)
y1 = np.array(y1_list)

ax1 = fig1.add_subplot(3, 2, 1)
ax_format(ax1, 10, 2, 250, 50)
ax1.plot(x1, y1)
ax1.set_xlabel('$t$')
ax1.set_ylabel('$y_\mathrm{i}$')
ax1.set_title('Raw data')

y1_list = []
y2_list = []
with open("y_fft_plot.txt") as f:
    for line in f.readlines():
        s = line.split(',')
        y1_list.append(float(s[0]))
        y2_list.append(float(s[1]))
y1 = np.array(y1_list)
y2 = np.array(y2_list)

freq = np.zeros(y1.size)
for i in range(y1.size):
    freq[i] = 2 * i / (20 / (y1.size-1)) / y1.size

ax1 = fig1.add_subplot(3, 2, 2)
ax_format(ax1, 250, 50, 1e8, 0.2e8)
ax1.plot(freq, y1*y1+y2*y2)
ax1.set_xlabel('$\omega$')
ax1.set_ylabel('$P$')
ax1.set_title('FFT of $y_\mathrm{i}$')
ax1.set_xlim(0, freq_upper)

x1_list = []
y1_list = []
with open("zlow_plot.txt") as f:
    for line in f.readlines():
        s = line.split(',')
        x1_list.append(float(s[0]))
        y1_list.append(float(s[1]))
x1 = np.array(x1_list)
y1 = np.array(y1_list)

ax1 = fig1.add_subplot(3, 2, 3)
ax_format(ax1, 10, 2, 250, 50)
ax1.plot(x1, y1)
ax1.set_xlabel('$t$')
ax1.set_ylabel('$z_\mathrm{low}$')
ax1.set_title('Low-pass filter')

y1_list = []
y2_list = []
with open("zlow_fft_plot.txt") as f:
    for line in f.readlines():
        s = line.split(',')
        y1_list.append(float(s[0]))
        y2_list.append(float(s[1]))
y1 = np.array(y1_list)
y2 = np.array(y2_list)

ax1 = fig1.add_subplot(3, 2, 4)
ax_format(ax1, 250, 50, 1e8, 0.2e8)
ax1.plot(freq, y1*y1+y2*y2)
ax1.set_xlabel('$\omega$')
ax1.set_ylabel('$P$')
ax1.set_title('FFT of $z_\mathrm{low}$')
ax1.set_xlim(0, freq_upper)

x1_list = []
y1_list = []
with open("zhigh_plot.txt") as f:
    for line in f.readlines():
        s = line.split(',')
        x1_list.append(float(s[0]))
        y1_list.append(float(s[1]))
x1 = np.array(x1_list)
y1 = np.array(y1_list)

ax1 = fig1.add_subplot(3, 2, 5)
ax_format(ax1, 10, 2, 200, 40)
ax1.plot(x1, y1)
ax1.set_xlabel('$t$')
ax1.set_ylabel('$z_\mathrm{high}$')
ax1.set_title('High-pass filter')

y1_list = []
y2_list = []
with open("zhigh_fft_plot.txt") as f:
    for line in f.readlines():
        s = line.split(',')
        y1_list.append(float(s[0]))
        y2_list.append(float(s[1]))
y1 = np.array(y1_list)
y2 = np.array(y2_list)

ax1 = fig1.add_subplot(3, 2, 6)
ax_format(ax1, 250, 50, 0.5e8, 0.1e8)
ax1.plot(freq, y1*y1+y2*y2)
ax1.set_xlabel('$\omega$')
ax1.set_ylabel('$P$')
ax1.set_title('FFT of $z_\mathrm{high}$')
ax1.set_xlim(0, freq_upper)

plt.tight_layout()
plt.savefig('filter.png')
plt.show()
