""" Christoffer's host-subtracted photometry
Plot the light curve! """

import matplotlib.pyplot as plt
plt.rc("font", family="serif")
plt.rc("text", usetex=True)
import numpy as np
from astropy.table import Table
from astropy.cosmology import Planck15
import glob


DATA_DIR = "/Users/annaho/Dropbox/Projects/Research/ZTF18abukavn/data/phot"

fig,ax = plt.subplots(1,1,figsize=(8,5))

f = DATA_DIR + "/ZTF18abukavn_opt_phot.dat"
dat = np.loadtxt(f, dtype=str, delimiter=' ')
instr = dat[:,0]
mjd = dat[:,1].astype(float)
filt = dat[:,2]
mag = dat[:,3].astype(float)
emag = dat[:,4].astype(float)

det = np.logical_and(mag<99, ~np.isnan(mag))
zp = mjd[det][0]
print(zp)
dt = mjd-zp

rcol = 'k'
ucol = '#f98e09'

band = filt=='u'
choose = np.logical_and(det, band)
ax.errorbar(
        dt[choose], mag[choose], emag[choose], fmt='o', ms=5,
        mec=ucol, mfc=ucol, c=ucol, label='u', zorder=8)
order = np.argsort(dt[choose])
#ax.plot(
#        dt[choose][order], mag[choose][order], c='k')

band = filt=='g'
choose = np.logical_and(det, band)
ax.errorbar(
        dt[choose], mag[choose], emag[choose], fmt='o', ms=5,
        mec='#57106e', mfc='white', c='#57106e', label='g')

band = filt=='r'
choose = np.logical_and(det, band)
ax.errorbar(
        dt[choose], mag[choose], emag[choose], fmt='s', ms=6,
        mec=rcol, mfc=rcol, c=rcol, label='r', zorder=9)
 
band = filt=='i'
choose = np.logical_and(det, band)
ax.errorbar(
        dt[choose], mag[choose], emag[choose], fmt='v', ms=5,
        c='grey', label='i')
 
band = filt=='z'
choose = np.logical_and(det, band)
ax.errorbar(
        dt[choose], mag[choose], emag[choose], fmt='s', ms=6,
        mec='k', mfc='white', label='z', c='k', zorder=1)
# 

ax.set_ylabel("Apparent Magnitude", fontsize=16)
ax.set_xlabel("Days since JD 2458370.6634 (2018 Sept 09 UT)", fontsize=16)
ax.yaxis.set_tick_params(labelsize=14)
ax.xaxis.set_tick_params(labelsize=14)
ax.legend(loc='upper right', fontsize=12)
#ax.set_xscale('log')
plt.gca().invert_yaxis()
plt.show()
