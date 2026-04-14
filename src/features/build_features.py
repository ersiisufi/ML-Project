from sklearn.base import BaseEstimator, TransformerMixin

def get_job_category(job_title):
    job_title = job_title.lower()

    if 'associate' in job_title:
        return 'Associate'

    # if 'machine learning' in job_title or 'ml' in job_title:
    #     return 'ML_Engineer'

    if 'consultant' in job_title:
        if 'data' in job_title:
            return 'Data_Consultant'
        else:
            return 'Other_Consultant'

    if 'architect' in job_title:
        if 'data' in job_title:
            return 'Data_Architect'
        elif 'ai' in job_title:
            return 'AI_Architect'
        else:
            return 'Other_Architect'


    if 'manager' in job_title:
        if 'data' in job_title:
            return 'Data_Manager'
        else:
            return 'Other_Manager' # Generic Manager role

    # Prioritize Scientist roles
    if 'scientist' in job_title:
        if 'data' in job_title:
            return 'Data_Scientist'
        elif 'research' in job_title:
            return 'Research_Scientist'
        else:
            return 'Other_Scientist' # Generic Scientist role

    # Prioritize Analyst roles
    if 'analyst' in job_title:
        if 'data' in job_title:
            return 'Data_Analyst'
        elif 'bi' in job_title:
            return 'BI_Analyst'
        else:
            return 'Other_Analyst' # Generic Analyst role

    # Then Engineer roles (from previous iteration)
    if 'engineer' in job_title:
        if 'data' in job_title:
            return 'Data_Engineer'
        elif 'machine learning' in job_title or 'ml' in job_title:
            return 'ML_Engineer'
        elif 'ai' in job_title or 'artificial intelligence' in job_title:
            return 'AI_Engineer'
        elif 'software' in job_title:
            return 'Software_Engineer'

        elif ' engineer' in job_title or 'engineer 'in job_title:
            return 'Other_Engineer' # Generic Engineer role
        else:
            return 'Engineer'

    # Other broad categories that don't fit above more specific roles
    if 'ai' in job_title or 'artificial intelligence' in job_title:
        return 'Other_AI_Role' # e.g., AI Specialist not an engineer

    if 'data' in job_title:
        return 'Other_Data_Role' # e.g., Data Manager, Data Lead not scientist, analyst, or engineer

    if 'software' in job_title:
        return 'Other_Software_Role' # e.g., Software Developer not an engineer

    return 'Other_Category' # Default for anything not matched


class FeatureEngineer (BaseEstimator, TransformerMixin):
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
    