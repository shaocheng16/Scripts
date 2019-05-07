"""
Demo file for plotting figure in python 
version: 0.1
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator, FormatStrFormatter


# select the style to used for plot
plt.style.use('presentation')

# https://matplotlib.org/users/customizing.html
params = {
   'axes.labelsize': 12,
   'text.fontsize': 8,
   'legend.fontsize': 10,
   'xtick.labelsize': 10,
   'ytick.labelsize': 10,
   'text.usetex': False,
   'lines.markeredgewidth' : 0,
   'lines.markersize' : 9,
   'legend.numpoints' : 1,
   'figure.figsize': [4.8, 3.6]
}
plt.rcParams.update(params)


# custom the position of legend
plt.legend(frameon=False,loc='upper left')


## set the ratio of xaxis and yaxis
plt.gca().set_aspect('equal', adjustable='box')


# adjust distance between sub_plot
plt.subplots_adjust(wspace=0.0, hspace = 0.0, right=0.8, top=0.9, bottom=0.1)

# hide ticks label
plt.gca().set_xticklabels([])
plt.gca().set_yticklabels([])

# set ticks range
plt.gca().set_xticks([-0.1,0,0.1])


## scatter plot
plt.scatter(x, y, markersize=25, np.linalg.norm(sed,axis = 1)**2, edgecolor = 'none', cmap = 'jet')
plt.clim(cmin,cmax)

##add a shared colorbar
im = plt.gca().get_children()[0]
cax = fig.add_axes([0.85,0.1,0.03,0.8])
fig.colorbar(im, cax=cax,label = 'Energy, $\Phi (\mathbf{k})$ (a.u.)')


## add shared x label and y label
fig.add_subplot(111, frameon=False)
# hide tick and tick label of the big axes
plt.tick_params(labelcolor='none', top='off', bottom='off', left='off', right='off')
plt.grid(False)

plt.xlabel(r'k$_x (2\pi/a)$')
plt.ylabel(r'k$_y (2\pi/a)$')
plt.gca().xaxis.set_label_coords(0.5, -0.035)
plt.gca().yaxis.set_label_coords(-0.05, 0.5)

## arrow in plot
plt.annotate("Some text", xy=(1.2, 2.8), xytext=(0.8, -2), arrowprops=dict(arrowstyle="->"))

## add text to plot
plt.text(0.45, 0.15, 'Bmim', fontsize = 18 ,color = 'r', transform = plt.gca().transAxes)

