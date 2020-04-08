from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import pandas

molecule = pandas.read_csv("molecules.csv")
sigma = molecule["sigma [nm]"]
intensity = molecule["intensity [photon]"]
offset = molecule["offset [photon]"]

plt.subplot(2, 2, 1)
plt.scatter(sigma, intensity, marker=".")
plt.xlabel('sigma')
plt.ylabel('intensity')

plt.subplot(2, 2, 2)
plt.scatter(sigma, offset, marker=".")
plt.xlabel('sigma')
plt.ylabel('offset')

plt.subplot(2, 2, 3)
plt.scatter(intensity, offset,  marker=".")
plt.xlabel('intensity')
plt.ylabel('offset')

fig = plt.figure()
ax = Axes3D(fig)
ax.scatter(sigma, intensity, offset,  marker='.')
ax.set_xlabel('X Sigma')
ax.set_ylabel('Y Intensity')
ax.set_zlabel('Z Offset')
plt.show()