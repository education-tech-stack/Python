import matplotlib.pyplot as plt
import matplotlib.patches as patches

plt.subplot(2,3,1)

plt.gca().add_patch(patches.Circle((0,0),5,ec = 'b', fc  = 'r', color = 'w',lw=2,linestyle='dashdot'))
plt.axis('scaled')
plt.title('Circle')

plt.subplot(2,3,2)

plt.gca().add_patch(patches.Ellipse((0,0),5,8,angle=15,fc='cyan',ec='red',linestyle='dashed',lw=2.2))
plt.axis('scaled')
plt.title('Ellipse')

plt.subplot(2,3,3)

plt.gca().add_patch(patches.Rectangle((0,0),5,8,angle=15,fc='cyan',ec='red',linestyle='dashed',lw=2.2))
plt.axis('scaled')
plt.title('Rectangle')

plt.subplot(2,3,4)

plt.gca().add_patch(patches.Polygon([[2.5,5],[2,6],[4,8],[6,6],[5.5,4]],fc='cyan',ec='red',linestyle='dashed',lw=2.2))
plt.axis('scaled')
plt.title('Polygon')

plt.subplot(2,3,5)

plt.gca().add_patch(patches.Arrow(1,2,-9,3,fill=False,hatch='o'))
plt.axis('scaled')
plt.title('Arrow')

plt.tight_layout()
plt.show()
