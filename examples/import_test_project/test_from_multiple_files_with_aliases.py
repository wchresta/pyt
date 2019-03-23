from .multiple_files.C import foo as foo_c
from .multiple_files.D import foo as foo_d

c = foo_c('from_c')
d = foo_d('from_d')
