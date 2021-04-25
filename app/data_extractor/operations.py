from sklearn.feature_selection import VarianceThreshold
import pandas as pd
import json

class ProcessFingerprint:
    def __init__(self, inputdataframe, variance:float, minmargin:float,
            maxmargin:float, save_variance:bool, outputcsvpath:str, outputjsonpath:str):

        inputcontribution = None
        contribution = None

        self.inputdataframe = inputdataframe
        self.inputcontribution = inputcontribution
        self.variance = variance
        self.contribution = contribution
        self.minmargin = minmargin
        self.maxmargin = maxmargin
        self.save_variance = save_variance
        self.outputcsvpath = outputcsvpath
        self.outputjson = outputjsonpath

    def execute(self):
        self._gen_dataframes()
        self._compute_fingerprint()
        self.data = self._gen_JSON()
        self._save_varianceDF()
        self._saveJSON(self.data)

    def _gen_dataframes(self):
        self.df_all = self.inputdataframe
        self.df_active = self.df_all[self.df_all['Activity']==1]
        self.df_inactive = self.df_all[self.df_all['Activity']==0]

        self.activity_status = self.df_all.Activity
        self.df_all = self.df_all.drop('Activity', axis=1)
        self.df_active = self.df_active.drop('Activity', axis=1)
        self.df_inactive = self.df_inactive.drop('Activity', axis=1)

        self.df_variance = self._variance_threshold_selector(self.df_all)
        self.df_variance = pd.concat([self.df_variance, self.activity_status], axis=1)

    def _variance_threshold_selector(self, data):
        selector = VarianceThreshold(self.variance)
        selector.fit(data)
        return data[data.columns[selector.get_support(indices=True)]]

    def _compute_fingerprint(self):
        self.mean_all = {}
        self.mean_active = {}
        self.mean_inactive = {}
        self.std_all = {}
        self.std_active = {}
        self.std_inactive = {}
        self.min_all = {}
        self.min_active = {}
        self.min_inactive = {}
        self.max_all = {}
        self.max_active = {}
        self.max_inactive = {}

        self.columns_name_all = list(self.df_all.columns)
        self.columns_name_remaining = list(self.df_variance.columns)
        self.columns_name_removed = list(set(self.columns_name_all)-set(self.columns_name_remaining))

        self.mean_all = (self.df_all.mean(axis = 0)).to_dict(self.mean_all)
        self.mean_active = (self.df_active.mean(axis = 0)).to_dict(self.mean_active)
        self.mean_inactive = (self.df_inactive.mean(axis = 0)).to_dict(self.mean_inactive)

        self.sum_all = ((self.df_all.sum(axis = 1)).sum()) / self.df_all.shape[0]
        self.sum_active = ((self.df_active.sum(axis = 1)).sum()) / self.df_active.shape[0]
        self.sum_inactive = ((self.df_inactive.sum(axis = 1)).sum()) / self.df_inactive.shape[0]

        self.std_all = (self.df_all.std(axis = 0)).to_dict(self.std_all)
        self.std_active = (self.df_active.std(axis = 0)).to_dict(self.std_active)
        self.std_inactive = (self.df_inactive.std(axis = 0)).to_dict(self.std_inactive)

        self.min_all = ((self.df_all.min() - (self.df_all.min()*self.minmargin)).round(0).astype(int)).to_dict(self.min_all)
        self.min_active = ((self.df_active.min() - (self.df_active.min()*self.minmargin)).round(0).astype(int)).to_dict(self.min_active)
        self.min_inactive = ((self.df_inactive.min() - (self.df_inactive.min()*self.minmargin)).round(0).astype(int)).to_dict(self.min_inactive)

        self.max_all = ((self.df_all.max() + (self.df_all.min()*self.maxmargin)).round(0).astype(int)).to_dict(self.max_all)
        self.max_active = ((self.df_active.max() + (self.df_active.min()*self.maxmargin)).round(0).astype(int)).to_dict(self.max_active)
        self.max_inactive = ((self.df_inactive.max() + (self.df_inactive.min()*self.maxmargin)).round(0).astype(int)).to_dict(self.max_inactive)

    def _gen_JSON(self):
        data = {}
        data['fingerprint'] = []
        data['mean'] = []
        data['sum'] = []
        data['std'] = []
        data['min'] = []
        data['max'] = []
        data['fingerprint'].append({'complete': self.columns_name_all,
                            'removed': self.columns_name_removed,
                            'remaining': self.columns_name_remaining})

        data['mean'].append({'complete': self.mean_all,
                            'active': self.mean_active,
                            'inactive': self.mean_inactive})

        data['sum'].append({'complete': self.sum_all,
                            'active': self.sum_active,
                            'inactive': self.sum_inactive})

        data['std'].append({'complete': self.std_all,
                            'active': self.std_active,
                            'inactive': self.std_inactive})
        data['min'].append({'complete': self.min_all,
                            'active': self.min_active,
                            'inactive': self.min_inactive})

        data['max'].append({'complete': self.max_all,
                            'active': self.max_active,
                            'inactive': self.max_inactive})

        if self.inputcontribution is not None:
            data['contributions'] = []
            data['notable'] = []

            data['contributions'].append(contrib)

            data['notable'].append({'fingerprint': self.great_fp,
                                    'mean': self.mean_great_fp,
                                    'std': self.std_great_fp,
                                    'min': self.min_great_fp,
                                    'max': self.max_great_fp})

        return data

    def _save_varianceDF(self):
        if self.save_variance == True:
            self.df_output.to_csv(self.outputcsv, index=True)

    def _saveJSON(self, data):

        with open(self.outputjson, 'w') as outfile:
            json.dump(data, outfile, indent=4)


    # def _gen_notable(self):
    #     self.contrib = {}
    #     cf = pd.read_csv(inputcontribution, index_col=0, delimiter=',')
    #     cf_series = cf.squeeze()
    #     self.contrib = cf_series.to_dict(contrib)

    # def _compute_notable(self):
    #     self.great_fp = []
    #     for current_fp in self.columns_name_remaining:
    #         if self.contrib.get(current_fp) >= 0.6:
    #             self.great_fp.append(current_fp)

    #     self.mean_great_fp = []
    #     for current_great_fp in self.great_fp:
    #         mean_fp = mean_active.get(current_great_fp)
    #         self.mean_great_fp.append(mean_fp)

    #     self.std_great_fp = []
    #     for current_great_fp in self.great_fp:
    #         std_fp = std_active.get(current_great_fp)
    #         self.std_great_fp.append(std_fp)

    #     self.min_great_fp = []
    #     for current_great_fp in self.great_fp:
    #         min_fp = min_active.get(current_great_fp)
    #         min_fp = min_fp + min_fp*minmargin
    #         self.min_great_fp.append(int(round(min_fp, 0)))

    #     self.max_great_fp = []
    #     for current_great_fp in self.great_fp:
    #         max_fp = max_active.get(current_great_fp)
    #         max_fp = max_fp + max_fp*maxmargin
    #         self.max_great_fp.append(int(round(max_fp, 0)))
