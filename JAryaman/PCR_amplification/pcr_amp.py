
import numpy as np
import matplotlib.pyplot as plt 
import matplotlib as mpl
import scipy.stats as stats

plt.close('all')
fontsize = 20
plt.rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})
plt.rc('text', usetex=True)
font = {'size' : fontsize}
plt.rc('font', **font)
mpl.rc('lines', markersize=10)
mpl.rc('lines', linewidth=2)
plt.rcParams.update({'axes.labelsize': fontsize})
mpl.rcParams['text.latex.preamble'] = [r'\usepackage{amsmath}'] 

fig, axs = plt.subplots(2,2, figsize = (10,10))
axs = axs.ravel()

def add_plot(ax, cs, mean_traj, q_low, q_high, mytitle):
	#ax.plot(cs, mean_traj, '-k', label = 'mean')
	ax.fill_between(cs, q_low, q_high, color = 'red', alpha = 0.3, label = '95\% BCI')
	ax.set_xlabel('Cycles')
	ax.set_ylabel('Copy number')
	ax.set_title(mytitle)
	ax.legend(loc = 'upper left', prop = {'size':10})

def make_traj(ps, nsim):
	trajectories = np.zeros((nsim, ncycles - 1))
	for i, p in enumerate(ps):
		trajectories[i, 0] = x0
		for k in xrange(ncycles - 2):
			trajectories[i, k + 1] = trajectories[i, k] + np.random.binomial(trajectories[i, k], p)

	#trajectories = np.log10(trajectories)

	q_low = np.percentile(trajectories, 2.5, axis = 0)
	q_high = np.percentile(trajectories, 100-2.5, axis = 0)
	mean_traj = np.mean(trajectories, axis = 0)
	return q_low, q_high, mean_traj

nsim = 100
ncycles = 20
x0 = 30
ps = stats.beta.rvs(90, 10, size = nsim)
cs = np.arange(ncycles - 1)

q_low, q_high, mean_traj = make_traj(ps, nsim)
add_plot(axs[0], cs, mean_traj, q_low, q_high, '$p_s \sim$ Beta(90,10)')

p = 0.9
ps = p*np.ones(nsim)
q_low, q_high, mean_traj = make_traj(ps, nsim)
add_plot(axs[1], cs, mean_traj, q_low, q_high, '$p_s = {}$'.format(p))

p = 0.7
ps = p*np.ones(nsim)
q_low, q_high, mean_traj = make_traj(ps, nsim)
add_plot(axs[2], cs, mean_traj, q_low, q_high, '$p_s = {}$'.format(p))

p = 0.5
ps = p*np.ones(nsim)
q_low, q_high, mean_traj = make_traj(ps, nsim)
add_plot(axs[3], cs, mean_traj, q_low, q_high, '$p_s = {}$'.format(p))

plt.tight_layout()
plt.savefig('pcr.png')



