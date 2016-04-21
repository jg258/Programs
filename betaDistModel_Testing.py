__author__ = 'Jason'
# Program Calculates Beta Distribution as well as graphcal output with individual chart display

import numpy as np

class betaDistributionModel:

    def __init__(self, min, max, shapeAlpha, shapeBeta):
        testArray = np.random.beta(0,1)
        self.mean = calcMeanU(min,max, shapeAlpha, shapeBeta)
        self.variance = calcVariance(min,max,shapeAlpha,shapeBeta)
        self.minimum
        self.maximum

    def calcAlpha(self):


    def calcBeta(self ):
        pass

    def calcMeanU(self, min, max, shapeAlpha, shapeBeta):
        self.mean = min + (max - min)( (shapeAlpha)/(shapeAlpha + shapeBeta) )

    def calcVariance(self, min, max, shapeAlpha, shapeBeta):
        return ((max-min)^2)( (shapeAlpha*shapeBeta)/ ( (shapeAlpha+shapeBeta)^2 * (shapeAlpha+shapeBeta+1) ) )

    def calcEigen(self):
        pass

    def determineMode(self, ):

    def getBetaDist(self):
        pass

    def getAlpha(self):
        pass

    def getMeanU(self):
        return self.mean