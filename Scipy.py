import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

x = np.linspace(0, 4, 10)
y = np.cos(x ** 2 / 3 + 4)
plt.plot(x, y, 'o')
plt.show()
f1 = interp1d(x, y, kind='linear')
f2 = interp1d(x, y, kind='cubic')
# f3 = interp1d(x, y, kind='nearest')
xnew = np.linspace(0, 4, 10)
plt.plot(x, y, 'o', xnew, f1(xnew), '-', xnew, f2(xnew), '--')
plt.legend(['Тип', 'linear', 'cubic'], loc='best')
plt.show()
