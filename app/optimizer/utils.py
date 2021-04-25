from pymoo.visualization.scatter import Scatter
import json

#@ -----------------------------------------------------------------------------------

class Polish:
    '''
    Post processing tools
    '''

    def floatToInteger(algorithm_result):
        '''
        Converts float to int
        '''
        int_list = []
        for current_result in algorithm_result.X:
            result = [round(x) for x in current_result]
            int_list.append(result)
        
        return int_list

#@ -----------------------------------------------------------------------------------

class Imports:
    '''
    '''
    def readJSON(pathtoJSON:str):
        with open(pathtoJSON) as json_file:
            data = json.load(json_file)

        return data

#@ -----------------------------------------------------------------------------------

class Exports:
    '''
    Class to export files
    '''

    def saveCSV(result_int, pathtofile:str):
        '''
        Export result to csv from integer values
        '''
        file = open(pathtofile, 'w')
        for current_pop in result_int:
            result = str(current_pop)
            result = result.replace('[', '')
            result = result.replace(']', '')
            file.write(result+'\n')
        file.close()

    def saveCSVRaw(algorithm_result, pathtofile:str):
        '''
        Export result to csv from algorithm result
        '''
        file = open(pathtofile, 'w')
        for current_pop in algorithm_result.X:
            result = str(list(current_pop))
            result = result.replace('[', '')
            result = result.replace(']', '')
            file.write(result+'\n')
        file.close()

#@ -----------------------------------------------------------------------------------

class Visualization:
    '''
    Visualization utils
    '''

    def scatterPlot(algorithm_result, COLOR='red'):
        '''
        Create scatter plot 2D
        '''
        plot = Scatter()
        plot.add(algorithm_result.F, color=COLOR)
        plot.show()