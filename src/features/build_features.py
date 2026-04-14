from sklearn.base import BaseEstimator, TransformerMixin

class FeatureEngineeri (BaseEstimator, TransformerMixin):
    def __init__(self):
        pass

    def fit(self, X, y=None):
        return self
    
    def transform (slef, X):
        X = X.copy()

        # Add seniority flags
        X['Is_Lead'] = X['job_title'].apply(lambda x: 1 if 'lead' in x.lower() else 0)
        X['Is_manager'] = X['job_title'].apply(lambda x: 1 if 'manager' in x.lower() else 0)
        X['Is_director'] = X['job_title'].apply(lambda x: 1 if 'director' in x.lower() else 0)
        X['Is_Principal'] = X['job_title'].apply(lambda x: 1 if 'principal' in x.lower() else 0)

        # Add job_category
        X['job_category'] = X['job_title'].apply(get_job_category)

        return X
    