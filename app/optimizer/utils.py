# External imports
from pymoo.visualization.scatter import Scatter
import json


class postProcessing:
    def floatToInteger(algorithm_result):
        """
        Converts float to int.

        Parameters
        ----------
        algorithm_result:
            algorithm result

        Returns
        -------
        int_list
            list
        """
        int_list = []
        for current_result in algorithm_result.X:
            result = [round(x) for x in current_result]
            int_list.append(result)

        return int_list


class IO:
    def readJSON(pathtoJSON: str):
        """
        Read JSON file.

        Parameters
        ----------
        pathtoJSON: str
            Path to JSON file

        Returns
        -------
        data
            dict
        """
        with open(pathtoJSON) as json_file:
            data = json.load(json_file)

        return data

    def saveCSV(result_int, pathtofile: str):
        """
        Export result to csv file.

        Parameters
        ----------
        result_int: int
            Result to be saved

        pathtofile: str
            Output file path
        """
        file = open(pathtofile, 'w')
        for current_pop in result_int:
            result = str(current_pop)
            result = result.replace('[', '')
            result = result.replace(']', '')
            file.write(result+'\n')
        file.close()

    def saveCSVRaw(algorithm_result, pathtofile: str):
        """
        Export result to csv file.

        Parameters
        ----------
        result_int: int
            Result to be saved

        pathtofile: str
            Output file path
        """
        file = open(pathtofile, 'w')
        for current_pop in algorithm_result.X:
            result = str(list(current_pop))
            result = result.replace('[', '')
            result = result.replace(']', '')
            file.write(result+'\n')
        file.close()


class Visualization:
    def scatterPlot(algorithm_result, COLOR='red'):
        """
        Create scatter plot 2D.

        Parameters
        ----------
        algorithm_result:
            Result

        COLOR: str
            Plot color
        """
        plot = Scatter()
        plot.add(algorithm_result.F, color=COLOR)
        plot.show()
