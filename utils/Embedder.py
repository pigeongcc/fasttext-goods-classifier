import os

import fasttext
import numpy as np
import pandas as pd
from tqdm import tqdm


class Embedder:
    def __init__(self, path: str) -> None:
        self.path = path

    def vectorize_series(self,
                         series: pd.Series,
                         folder: str,
                         filename: str) -> np.ndarray:
        
        if not os.path.isdir(folder):
            os.makedirs(folder)
        
        vectorizer = fasttext.load_model(self.path)

        embeddings = []
        for index, text in zip(series.index, tqdm(series)):
            try:
                embedding = vectorizer.get_sentence_vector(text.replace('\n', ' '))
                embeddings.append(embedding)
            except:
                print(f'Exception while vectorizing index {index}:')
                print(text)
        
        del vectorizer

        embeddings = np.array(embeddings)
    
        filepath = os.path.join(folder, filename)
        np.save(filepath, embeddings)
        
        return embeddings
    
    def generate_embeddings(self,
                            df: pd.DataFrame,
                            embedded_features: list,
                            folder: str,
                            postfix: str) -> pd.DataFrame:
        embeddings = {}
        for feature in embedded_features:
            filename = f'{feature}_{postfix}.npy'
            path = f'./{folder}/{filename}'
            if not os.path.exists(path):
                embeddings[feature] = self.vectorize_series(df[feature], folder=folder, filename=filename)
            else:
                embeddings[feature] = np.load(path)

        df_embeddings = pd.DataFrame()
        for feature in embedded_features:
            df_emb_feature = pd.DataFrame(embeddings[feature], columns=[f'{feature}.' + str(i) for i in range(embeddings[feature].shape[1])])
            df_embeddings = pd.concat([df_embeddings, df_emb_feature], axis=1)

        df_embeddings = df_embeddings.set_index(df.index)
        return df_embeddings