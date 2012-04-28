import IPython.lib.demo as ipd

# To use, run ipython, then
#
# In [1]: %run Demos.py
# In [2]: d = ImageDemo()
# In [3]: d()
# In [4]: d()

def ImageDemo ():
    return ipd.ClearIPDemo ( 'BasicTutorial1/Image.py' )

def InputOutputDemo ():
    return ipd.ClearIPDemo ( 'BasicTutorial1/InputOutput.py' )

def MemoryManagementDemo ():
    return ipd.ClearIPDemo ( 'BasicTutorial1/MemoryManagement.py' )

def FiltersDemo ():
    return ipd.ClearIPDemo ( 'BasicTutorial2/Filters.py' )

def MorphologyDemo ():
    return ipd.ClearIPDemo ( 'BasicTutorial2/Morphology.py' )

def MeasureRegionsDemo ():
    return ipd.ClearIPDemo ( 'InteractiveTutorial/MeasureRegions.py' )

def BorderChangeDemo ():
    return ipd.ClearIPDemo ( 'InteractiveTutorial/05-01-BorderChange.py' )

def NumpyDemo ():
    return ipd.ClearIPDemo ( 'InteractiveTutorial/05-02-Numpy.py' )

def RidgeDetectionDemo ():
    return ipd.ClearIPDemo ( 'InteractiveTutorial/05-04-RidgeDetection.py' )

