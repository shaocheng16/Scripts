"""
Demo file for plotting figure in python
version: 0.10
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

colors = ['#e6194B', '#3cb44b', '#ffe119', '#4363d8', '#f58231', '#911eb4', '#42d4f4', '#f032e6', '#bfef45', '#fabebe',
    |   ¦ '#469990', '#e6beff','#9A6324', '#fffac8', '#800000', '#aaffc3', '#808000', '#ffd8b1', '#000075', '#a9a9a9']
names = ['red', 'green', 'yellow', 'blue', 'orange', 'purple','cyan','megenta', 'lime','pink',
    |   ¦'teal','lavender', 'brown', 'beige','maroon','mint','olive','apricot','navy','grey']

my_color = dict(zip(names, colors))



# custom the position of legend
plt.legend(frameon=False,loc='upper left')


## set the ratio of xaxis and yaxis
plt.gca().set_aspect('equal', adjustable='box')


# adjust distance between sub_plot
plt.subplots_adjust(wspace=0.0, hspace = 0.0, right=0.8, top=0.9, bottom=0.1)

#====================
# hide ticks label
#====================
plt.gca().set_xticklabels([])
plt.gca().set_yticklabels([])
# or
plt.xticks(visible = False)

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

##===========
## specify the location of legend box
## change the linewidth in legend
##===========
leg = ax2.legend(frameon=False, bbox_to_anchor=(1.0, .75))
for line in leg.get_lines():
    line.set_linewidth(4.0)

# change the order of legend
handles, labels = ax1.get_legend_handles_labels()
order = [0,2,1]
ax1.legend([handles[idx] for idx in order],[labels[idx] for idx in order], frameon=False)

# custom marker size in scatter plot
v_val=1.0
h_val=2.0
verts = list(zip([-h_val,h_val,h_val,-h_val],[-v_val,-v_val,v_val,v_val]))
ax.scatter([0.5,1.0],[1.0,2.0], marker=(verts,0))


### Plot 3d figure
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
fig = plt.figure(1)
ax = fig.add_subplot(111, projection='3d')
ax.scatter(kx, ky, kz)
plt.gca().set_aspect('equal',adjustable='box')
plt.show()

