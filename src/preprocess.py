import pandas as pd

def load_data(train_path, test_path):
    df_train = pd.read_csv(train_path)
    df_test = pd.read_csv(test_path)
    return df_train, df_test

def clean_dimensions(df):
    return df[(df['x'] > 0) & (df['y'] > 0) & (df['z'] > 0)]

def encode_features(df, categorical_columns):
    return pd.get_dummies(df, columns=categorical_columns, drop_first=True)

def align_features(train_df, test_df):
    return train_df.align(test_df, join='left', axis=1, fill_value=0)