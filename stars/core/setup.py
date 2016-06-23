#!/usr/bin/env python

"""
setup.py file for SWIG example

For windows 7:
	1.install Mingw32
	2.install pthreads-win32 (POSIX pthreads library for windows)
	2.1 get latest version (pthreads-w32-...-release.exe), extract to some temp location
	    In the Pre-built.2 directory, locate the \lib and \include subdirectories and copy
	    their contents, respectively to your MSYS library and include paths
	    (e.g. C:\Msys\1.0\local\lib and C:\Msys\1.0\local\include)
	2.2 copy the DLL files (or at least PthreadVC2.Dll) from lib\ subdirectory to your 
	    c:\Windows\System directory.
	2.3 check if "libpython27(6 or 5).a in your MinGW\lib directory; if not, copy it from your
	    Python\libs directory.
	3.python setup.py build_ext -c mingw32 --inplace
	3.1 remove compiler flag "-mcygwin" from Python\Lib\distutils\cygwincompiler.py; otherwise, you will meet
	    some errors when compile this extension
	3.2 when you meet compiler error "udefined reference to `_imp__pthread_join'" or
	    "udefined reference to `_imp__pthread_create'", try to check and add "-lpthread" at the end of
	    compiling cmd: python setup.py build_ext -c mingw32 --inplace -lpthread
"""

from distutils.core import setup, Extension


extensions = [Extension('_mt_densitymap',
                        sources=['mt_densitymap_wrap.cpp', 'mt_densitymap.cpp'],
                        ),
              Extension('_lisa',
                        sources=['Lisa_wrap.cpp', 'Lisa.cpp', 'Randik.cpp', 'GalWeight.cpp'],
                        ),
              Extension('_weights',
                        sources=['Weight_wrap.cxx', 'GalWeight.cpp','GwtWeight.cpp'],
                        )
              ]

setup (name = 'CAST',
       version = '0.1',
       author      = "Xun Li",
       description = """Python wrapper for C++ KDE/LISA/Weigth""",
       ext_modules = extensions,
       py_modules = ["mt_densitymap","lisa","weight"],
       )




