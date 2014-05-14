import numpy as np

def twoPtForwardDiff(x,y):
    '''
    Makes sure that the array returned is the correct size/shape.
    
    For any point except the last, the function takes the difference of 
    that point's y value and the next y value and divides it by the
    difference between that x value and the next x value.
    
    For the last point, the backward difference is taken.
    
    Returns the numerical derivative of the function as dydx.
    '''
    
    dydx = np.zeros(y.shape,float)
    dydx[0:-1] = np.diff(y)/np.diff(x)
    dydx[-1] = (y[-1]-y[-2])/(x[-1] - x[-2])
    return dydx

def twoPtCenteredDiff(x,y):
    '''
    Makes sure the array is the correct size/shape.
    Uses center differencing for all points besides first and last.
    Uses forward differencing for the first point in the array.
    Uses backward differencing for the last point in the array.
    Returns the numerical derivative of the function as dydx.
    '''
    dydx = np.zeros(y.shape,float)
    dydx[1:-1] = (y[2:] - y[:-2])/(x[2:]-x[:-2])
    dydx[0] = (y[1]-y[0])/(x[1]-x[0])
    dydx[-1] = (y[-1]-y[-2])/(x[-1]-x[-2])
    return dydx


def fourPtCenteredDiff(x,y):
    '''
    Computes numerical differential for two arrays x and y.
    Uses the four point differentiation method for the third through
    third to last points.
    Uses lowest order finite difference method for first two and last two
    points.
    '''
    
    dydx = np.zeros(y.shape,float)
    dydx[2:-2] = (y[0:-4]-8*y[1:-3]+8*y[3:-1]-y[4:]) / (12*.1)
    dydx[-1] = (y[-1]-y[-2])/(x[-1] - x[-2])
    dydx[0] = (y[1]-y[0])/(x[1]-x[0])
    dydx[1] = (y[2] - y[0])/(x[2]-x[0])
    dydx[-2] = (y[-1] - y[-3])/(x[-1]-x[-3])
    return dydx