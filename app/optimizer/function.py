# Externel imports
import random


class Function:
    def __init__(self, data):
        # self.mean_notable = data['notable'][0]['mean']
        self.mean_full = list(data['mean'][0]['active'].values())

    def full_sum(self):
        '''
        Summation of the quantity "attributes" distributed in the whole FP
        '''
        function = ''
        for iter_gen in range(1, len(self.mean_full)):
            if iter_gen == len(self.mean_full)-1:
                function = function + f'x[{iter_gen}]'
            else:
                function = function + f'x[{iter_gen}] + '

        return function

    def full_dist(self):
        '''
        Euclidian distance from gen FP to mean notable FP
        '''
        function = ''
        for iter_gen in range(1, len(self.mean_full)):
            if iter_gen == len(self.mean_full)-1:
                function = function + \
                    f'abs({self.mean_full[iter_gen]} - x[{iter_gen}])'
            else:
                function = function + \
                    f'abs({self.mean_full[iter_gen]} - x[{iter_gen}]) + '

        return function

    def full_dist_variable(self):
        '''
        Euclidian distance from gen FP to mean notable FP
        '''
        function = ''
        for iter_gen in range(1, len(self.mean_full)):
            scale = random.uniform(-1, 1)

            if iter_gen == len(self.mean_full)-1:
                function = function + \
                    f'abs({self.mean_full[iter_gen] + (self.mean_full[iter_gen] * scale)} - x[{iter_gen}])'
            else:
                function = function + \
                    f'abs({self.mean_full[iter_gen] + (self.mean_full[iter_gen] * scale)} - x[{iter_gen}]) + '

        return function

    def notable_sum(self):
        '''
        Summation of the quantity "attributes" distributed in the notable FP
        '''
        function = ''
        for iter_gen in range(1, len(self.mean_notable)):
            if iter_gen == len(self.mean_notable)-1:
                function = function + f'x[{iter_gen}]'
            else:
                function = function + f'x[{iter_gen}] + '

        return function

    def notable_dist(self):
        '''
        Euclidian distance from gen FP to mean notable FP
        '''
        function = ''
        for iter_gen in range(1, len(self.mean_notable)):
            if iter_gen == len(self.mean_notable)-1:
                function = function + \
                    f'abs({self.mean_notable[iter_gen]} - x[{iter_gen}])'
            else:
                function = function + \
                    f'abs({self.mean_notable[iter_gen]} - x[{iter_gen}]) + '

        return function


class Constrain:
    def __init__(self, data):
        # self.mean_notable = data['notable'][0]['mean']
        self.mean_full = list(data['mean'][0]['active'].values())

    def full_sum(self, signal: str, operation_signal: str):
        '''
        Summation of the quantity "attributes" distributed in the notable FP.
        signal dictates addition or subtraction operation for sum value
        operation_signal dictates final addition or subtraction operation
        '''

        # value_tolerance = max(self.mean_full) - min(self.mean_full)
        # value = sum(self.mean_full)
        final_number = eval(f'value {signal} value_tolerance')

        function = ''
        for iter_gen in range(1, len(self.mean_full)):
            if iter_gen == len(self.mean_full)-1:
                function = function + \
                    f'x[{iter_gen}] {operation_signal} {final_number}'
            else:
                function = function + f'x[{iter_gen}] + '

        return function

    def full_sumnot(self, signal: str, operation_signal: str):
        '''
        Summation of the quantity "attributes" distributed in the notable FP.
        signal dictates addition or subtraction operation for sum value
        operation_signal dictates final addition or subtraction operation
        '''

        # value_tolerance = max(self.mean_full) - min(self.mean_full)
        # value = sum(self.mean_full)
        final_number = eval(f'value {signal} value_tolerance')

        function = ''
        for iter_gen in range(1, len(self.mean_full)):
            if iter_gen == len(self.mean_full)-1:
                function = function + \
                    f'- x[{iter_gen}] {operation_signal} {final_number}'
            else:
                function = function + f'- x[{iter_gen}] '

        return function

    # @ --------------------------------

    def notable_sum(self, signal: str, operation_signal: str):
        '''
        Summation of the quantity "attributes" distributed in the notable FP.
        signal dictates addition or subtraction operation for sum value
        operation_signal dictates final addition or subtraction operation
        '''

        # value_tolerance = max(self.mean_notable) - min(self.mean_notable)
        # value = sum(self.mean_notable)
        final_number = eval(f'value {signal} value_tolerance')

        function = ''
        for iter_gen in range(1, len(self.mean_notable)):
            if iter_gen == len(self.mean_notable)-1:
                function = function + \
                    f'x[{iter_gen}] {operation_signal} {final_number}'
            else:
                function = function + f'x[{iter_gen}] + '

        return function

    def notable_sumnot(self, signal: str, operation_signal: str):
        '''
        Summation of the quantity "attributes" distributed in the notable FP.
        signal dictates addition or subtraction operation for sum value
        operation_signal dictates final addition or subtraction operation
        '''

        # value_tolerance = max(self.mean_notable) - min(self.mean_notable)
        # value = sum(self.mean_notable)
        final_number = eval(f'value {signal} value_tolerance')

        function = ''
        for iter_gen in range(1, len(self.mean_notable)):
            if iter_gen == len(self.mean_notable)-1:
                function = function + \
                    f'- x[{iter_gen}] {operation_signal} {final_number}'
            else:
                function = function + f'- x[{iter_gen}] '

        return function
