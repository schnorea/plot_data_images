import matplotlib.pyplot as plt
from scipy import signal
import numpy as np
import random

color_pallet = [
    '#4deeea',	
    '#74ee15',
    '#ffe700',
    '#f000ff'
]


def make_sine_image(start, end, inc):
    #x = np.linspace(0.1, 4 * np.pi, 41)
    x = np.linspace(start, end + start, inc)
    y = np.exp(np.sin(x))
    y = np.sin(x)
    return x, y

def make_squarewave_image(start, end, inc):
    #x = np.linspace(0.1, 4 * np.pi, 41)
    x = np.linspace(start, end + start, inc)
    y = np.exp(np.sin(x))
    y = np.sin(x)
    y = signal.square(x)
    return x, y

def make_aperiodtic_image(start, end, inc):
    #x = np.linspace(0.1, 4 * np.pi, 41)
    x = np.linspace(start, end + start, inc)
    y = np.exp(np.sin(x))
    y += np.sin(x)
    y -= signal.square(x)
    return x, y


def plot_stem(x, y, filename):
    fig = plt.figure()
    # stems = plt.stem(x, y, linefmt='b-', markerfmt='bo', basefmt='r-')
    # plt.setp(stems, 'linewidth', 2, 'color', '#4deeea')
    #plt.setp(stems, 'linewidth', 2, 'color', '#4deeea')
    #plt.stem(x, y,'#4deeea')
    markerline, stemlines, baseline = plt.stem(x, y, markerfmt='o')
    plt.setp(stemlines, 'color', color_pallet[0])
    plt.setp(markerline, 'color', color_pallet[3])
    plt.setp(baseline, 'linewidth', 10)
    #plt.setp(stemlines, 'linestyle', 'dotted')

    figure = plt.gca()
    x_axis = figure.axes.get_xaxis()
    x_axis.set_visible(False)
    y_axis = figure.axes.get_yaxis()
    y_axis.set_visible(False)
    figure.axes.axis('off')

    plt.savefig(filename, transparent=True)
    plt.close()

def unit_impulse(a, n):
    delta =[]
    for sample in n:
        if sample == a:
            delta.append(1)
        else:
            delta.append(0)
              
    return delta

def random_drop(y, drop_percent=10):
    num_points = len(y)
    drop_num_point = int(num_points * (drop_percent/100.0))
    null_these = random.sample(range(num_points), drop_num_point)

    for i, v in enumerate(y):
        if i in null_these:
            y[i] = None
    return y

for i in range(100):
    start = (4.0 * np.pi/100.0) * i
    end = 4 * np.pi
    inc = 41
    pn = i
    filename = f'images/sin_image_{pn:03}.png'
    x, y = make_sine_image(start, end, inc)
    #y = random_drop(y, drop_percent=10)
    plot_stem(x, y, filename)

    filename = f'images/sqr_image_{pn:03}.png'
    x, y = make_squarewave_image(start, end, inc - 12)
    #y = random_drop(y, drop_percent=50)
    plot_stem(x, y, filename)

    filename = f'images/np_image_{pn:03}.svg'
    x, y = make_aperiodtic_image(start, end, inc - 19)
    y = random_drop(y, drop_percent=80)
    plot_stem(x, y, filename)
    

# freq = 180
# for i in range(freq):
#     start = (2.0 * np.pi/freq) * i
#     end = 2.0 * np.pi
#     inc = 41
#     pn = i

#     filename = f'images/sqr_image_{pn:03}.png'
#     x, y = make_squarewave_image(start/3, end/3, inc - 12)
#     #y = random_drop(y, drop_percent=50)
#     plot_stem(x, y, filename)
