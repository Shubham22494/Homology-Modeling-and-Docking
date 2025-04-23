from modeller import *

log.verbose()
env = Environ()

env.libs.topology.read(file='$(LIB)/top_heav.lib')

# Read aligned structure(s):
aln = Alignment(env)
aln.append(file='fm00495.ali', align_codes='all')
aln_block = len(aln)

# Read aligned sequence(s):
aln.append(file='mutation3.ali', align_codes='MUT3')
# aln.append(file='C:/Users/shubh/Semester 6/CADD/Assignment 1/fm00495.ali', align_codes='7p3iA')
# aln.append(file='C:/Users/shubh/Semester 6/CADD/Assignment 1/fm00495.ali', align_codes='8yx1C')

# Structure sensitive variable gap penalty sequence-sequence alignment:
aln.salign(output='', max_gap_length=20,
           gap_function=True,   # to use structure-dependent gap penalty
           alignment_type='PAIRWISE', align_block=aln_block,
           feature_weights=(1., 0., 0., 0., 0., 0.), overhang=0,
           gap_penalties_1d=(-450, 0),
           gap_penalties_2d=(0.35, 1.2, 0.9, 1.2, 0.6, 8.6, 1.2, 0., 0.),
           similarity_flag=True)

aln.write(file='resultant3.ali', alignment_format='PIR')
aln.write(file='resultant3.pap', alignment_format='PAP')