import os
import pickle

import pandas as pd
from category_encoders import TargetEncoder


class TargetEncodersWrapper:
    def __init__(self) -> None:
        self.encoders_order = None
        
    def load(self, encoders_path: str):
        if os.path.exists(encoders_path):
            with open(encoders_path, 'rb') as f:
                encoders, self.encoders_order = pickle.load(f)
            return encoders
        else:
            return None

    def fit(self,
            df: pd.DataFrame,
            feature: str,
            target: str,
            save_path: str = None) -> dict:
        
        encoders = {}
        self.encoders_order = []
        target_vals = df[target].unique()
        for target_val in target_vals:
            target_aux = df[target].apply(lambda x: 1 if x == target_val else 0)
            encoder = TargetEncoder().fit(df[feature], target_aux)
            encoders[target_val] = encoder
            self.encoders_order.append(target_val)
        
        if save_path is not None:
            with open(save_path, 'wb') as f:
                pickle.dump((encoders, self.encoders_order), f, protocol=pickle.HIGHEST_PROTOCOL)
        
        return encoders

    def transform(self,
                  df: pd.DataFrame,
                  feature: str,
                  encoders: dict) -> pd.DataFrame:
        
        encodings = []
        for key in self.encoders_order:
            encoding = encoders[key].transform(df[feature])
            encodings.append(encoding)

        return pd.concat(encodings, axis=1)

    def fit_transform(self,
                      df: pd.DataFrame,
                      feature: str,
                      target: str,
                      save_path: str = None) -> pd.DataFrame:
        
        encoders = self.fit(df, feature, target, save_path)
        df_encodings = self.transform(df, feature, encoders)
        return df_encodings