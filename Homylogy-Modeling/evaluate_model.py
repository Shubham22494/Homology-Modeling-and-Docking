from modeller import *
from modeller.scripts import complete_pdb

log.verbose()    # request verbose output
env = Environ()
env.libs.topology.read(file='$(LIB)/top_heav.lib') # read topology
env.libs.parameters.read(file='$(LIB)/par.lib') # read parameters

# read model file
mdl = complete_pdb(env, 'MUT3.B99990003.pdb')

# Assess all atoms with DOPE:
s = Selection(mdl)
s.assess_dope(output='ENERGY_PROFILE NO_REPORT', file='mut3.profile',
              normalize_profile=True, smoothing_window=15)