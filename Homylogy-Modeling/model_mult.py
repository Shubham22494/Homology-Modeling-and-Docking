from modeller import *
from modeller.automodel import *

env = Environ()
a = AutoModel(env, alnfile='resultant3.ali',
              knowns=('8yx1C','7p3iA','6faxR'), sequence='MUT3')
a.starting_model = 1
a.ending_model = 5
a.make()