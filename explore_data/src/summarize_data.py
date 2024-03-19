import pandas as pd
import numpy as np
import seaborn as sns


# TODO Probably creating a class here but not sure
# make function for categorical variables as well (cat=True)
# mean, median, nulls, distinct answers, total answers, percentiles, 
def explore_numerics(df: pd.DataFrame, cat=False) -> pd.Series:
    df = df.select_dtypes(include="np.numeric")
    count_rows = df.count()
    sum_columns = df.sum()
    mean = sum_columns/count_rows
    return mean

def explore_cats(df) -> pd.DataFrame:
    pass

def explore_visuals(df: pd.DataFrame, interact=False) :
    pass




