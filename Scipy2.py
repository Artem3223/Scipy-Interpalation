import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import UnivariateSpline

x = np.linspace(-10, 10, 50)
y = np.exp(-x ** 2) + 0.1 * np.random.randn(50)
plt.plot(x, y, 'ro', ms=5)
plt.show()
spl = UnivariateSpline(x, y)
xs = np.linspace(-10, 10, 50)
plt.plot(xs, spl(xs), 'g', lw=3)
plt.show()
