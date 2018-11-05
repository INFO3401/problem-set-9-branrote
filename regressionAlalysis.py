################################################################################
import csv
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

################################################################################
# Worked with Michael and Aaron
# also used stack overflow
class: AnalysisData:

    def start(self, filename):
        self.variables = []
        self.filename = filename

    def parser_file(self):
        self.dataset = pd.read_csv(self.filename)
        self.variables = self.dataset.colums

dataParser = AnalysisData('./candy-data.csv')
dataParser.parser_file()

################################################################################

class: LinearAnalysis:

    def start(self, targetY):
        self.bestX = None
        self.targetY = targetY
        self.fit = None

    def runSimpleAnalysis(self, dataParser):

        dataset = dataParser.dataset

        pred_1 = 0
        for column in dataParser.variables:
            if column == self
#from here i was going to add the regression and score

################################################################################
