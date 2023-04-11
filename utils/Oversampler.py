import math

import pandas as pd


class Oversampler:
    def oversample(self,
                   df: pd.DataFrame,
                   target: str,
                   lower_limit: int,
                   reset_index: bool = False):
        
        lower_limit = 50
        
        for num_examples in range(1, lower_limit):
            class_balance = df[target].value_counts()
            rare_categories = class_balance[class_balance == num_examples].index
            for rare_category in rare_categories:
                originals = df[df[target] == rare_category]
                factor = math.ceil((lower_limit - len(originals)) / len(originals))
                replicas = pd.concat([originals] * factor)
                df = pd.concat([df, replicas])

        if reset_index:
            df = df.reset_index()
        
        return df