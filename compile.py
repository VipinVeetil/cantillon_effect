from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

import numpy

setup(
	  name = 'fast_weights_opt',
	  ext_modules=[
				   Extension('fast_weights_opt', ['fast_weights_opt.pyx'],
							 include_dirs=[numpy.get_include()]),
				   Extension('fast_economic_functions', ['fast_economic_functions.pyx'],
							 include_dirs=[numpy.get_include()]),
				   
				   ],
	  cmdclass = {'build_ext': build_ext}
	  )