# coding: utf-8

from __future__ import division
import matplotlib.pyplot as plt

# Define path
UserPath = '/Users/Desktop/'

# From Perera et al., (2018)
LMO_Solidification_Time = 30   # (in Myrs)

# From Connelly et al., (2012)
Age_SolarSystem = 4.56730      # (in Ga)

# From Touboul et al., (2009) & Boyet et al., (2015)
MoonFormation_earliest = Age_SolarSystem - (52/1000)
MoonFormation_latest = Age_SolarSystem - (152/1000)

# From Alibert et al., (1994), Apollo sample 67016
FAN_oldest = 4.56
FAN_oldest_plusError = 0.07
FAN_oldest_minusError = 0.07

# From Borg et al., (1999), Apollo sample 62236
FAN_youngest = 4.29
FAN_youngest_plusError = 0.06
FAN_youngest_minusError = 0.06

# From Borg et al., (2015), Apollo sample 60025
FAN_Sample_60025 = 4.360
FAN_Sample_60025_plusError = 0.003
FAN_Sample_60025_minusError = 0.003

# From Borg et al., (2015)
urKREEP = 4.368
urKREEP_plusError = 0.029
urKREEP_minusError = 0.029


# Set font
plt.rcParams["font.family"] = "serif"

y = 1.2
y2 = 0.90
y3 = 1.05

# Create Figure and Axes instances
fig,ax = plt.subplots(1)
ax.set_aspect(aspect=0.25)

plt.plot([Age_SolarSystem, Age_SolarSystem], [0, 2], 'k--', lw=2)
plt.text(Age_SolarSystem-0.014, 0.82, "Oldest CAI", ha='center', color='k', rotation=90, fontsize=13)

plt.plot([MoonFormation_earliest, MoonFormation_earliest], [0, 2], '#006ddb', lw=3)
plt.text(MoonFormation_earliest-0.015, 0.93, "Earliest Moon", ha='center', color='#006ddb', rotation=90, fontsize=13)
rectangle = plt.Rectangle((MoonFormation_earliest, 0), -(LMO_Solidification_Time/1000), 2, fc='#006ddb', alpha=0.2)
plt.gca().add_patch(rectangle)

plt.plot([MoonFormation_latest, MoonFormation_latest], [0, 2], '#db6d00', lw=3)
plt.text(MoonFormation_latest-0.014, 0.88, "Latest Moon", ha='center', color='#db6d00', rotation=90, fontsize=13)
rectangle = plt.Rectangle((MoonFormation_latest, 0), -(LMO_Solidification_Time/1000), 2, fc='#db6d00', alpha=0.2)
plt.gca().add_patch(rectangle)

plt.text(4.42, y-0.054, "Ferroan Anorthosites\n(FAN)", ha='center', color='#7C7C7C', fontsize=13)
plt.scatter(FAN_oldest, y, s=80, color='#7C7C7C')
plt.hlines(y, FAN_oldest-FAN_oldest_minusError, FAN_oldest+FAN_oldest_plusError, '#7C7C7C', linewidth=2)
plt.scatter(FAN_youngest, y, s=80, color='#7C7C7C')
plt.hlines(y, FAN_youngest-FAN_youngest_minusError, FAN_youngest+FAN_youngest_plusError, '#7C7C7C', linewidth=2)

plt.text(4.29, y3-0.02, "Best FAN Age", ha='center', color='#920000', fontsize=13)
plt.scatter(FAN_Sample_60025, y3, marker='s', s=80, facecolors='#920000', edgecolors='#920000')
plt.hlines(y3, FAN_Sample_60025-FAN_Sample_60025_minusError, FAN_Sample_60025+FAN_Sample_60025_plusError, '#920000', linewidth=1)

plt.text(4.275, y2-0.014, "ur-KREEP Age", ha='center', color='#009292', fontsize=13)
plt.scatter(urKREEP, y2, marker='^', s=80, facecolors='#009292', edgecolors='#009292')
plt.hlines(y2, urKREEP-urKREEP_minusError, urKREEP+urKREEP_plusError, '#009292', linewidth=1)
plt.xlabel('Time (Ga)', fontsize = 14)
plt.xticks(fontsize = 13)

plt.ylim(0.5,1.3)

ax.axes.get_yaxis().set_visible(False)

plt.gca().invert_xaxis()

plt.show()

plotName = UserPath + 'EarlyLunarTimeline.png'
plt.savefig(plotName, dpi=300, bbox_inches='tight')
plt.close()