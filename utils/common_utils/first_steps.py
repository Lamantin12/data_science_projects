import numpy as np
import pandas as pd
from IPython.display import display

def first_descriptions(df: pd.DataFrame) -> None:
    print(' Dataset first description '.center(126, '*'))

    print(' Head of dataset '.center(126, '*'))
    display(df.head(5))

    print(' Pandas-Generated info '.center(126, '*'))
    display(df.info())

    print(' Categorical features unique '.center(126, '*'))
    for column in df.select_dtypes(include=['object']):
        print(column)
        print(df[column].unique(), '\n')

    print(' Dublicate check '.center(126, '*'))
    print(f"Number of dublicates is : {df.duplicated().sum()}")

    print(' NaN check '.center(126, '*'))
    print(f"Total number of NaN is : {df.isna().sum().sum()}")
    print(f"Number of NaN by column  : \n {df.isna().sum()}")