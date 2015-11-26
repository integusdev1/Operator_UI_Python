
##SetUp 
from distutils.core import setup

# py2exe stuff
import py2exe, os

# getting pythoncard to work by editing Setup.py.I found this code from http://www.py2exe.org/index.cgi/PythonCardSetup 
# find pythoncard resources, to add as 'data_files'
pycard_resources=[]
for filename in os.listdir('.'):
    if filename.find('.rsrc.')>-1:
        pycard_resources+=[filename]



# includes for py2exe


includes=[]
for comp in ['button','image','staticbox',\
            'statictext','textarea','textfield','passwordfield']:
    includes += ['PythonCard.components.'+comp]
print 'includes',includes

## by mistake py2exe adds powrprof.dll and mswsock.dll when packages are built in vista or windows7.
## winXp contains its own copy of these dll,so removing these dll is required.
opts = { 'py2exe': { 'includes':includes ,'dll_excludes':[ 'mswsock.dll', 'powrprof.dll','MSVCP90.dll' ]
                   }
       }
print 'opts',opts


# end of py2exe stuff

setup(name='RunVMSWithPythonCard_WithResults',
    version='0.3',
    url='about:none',
    author='bt',
    author_email='btanti@integus.in',
    package_dir={'RunVMSWithPythonCard_WithResults':'.'},
    packages=['RunVMSWithPythonCard_WithResults'],
    data_files=[('.',pycard_resources)],
    console=['RunVMSWithPythonCard_WithResults.py'],
    options=opts
    )

