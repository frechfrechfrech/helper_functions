import pandas as pd
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import pyplot as plt
import importlib

def plot_3d_with_hue(df, cols = ['x','y','z'], hue_col='hue', title='',xlabel='X', ylabel='Y', zlabel='Z', figsize=(8,8), hue_color_dict={}):
    '''
    Generalized function to plot pandas dataframe values in 3d
    df: DataFrame containing the datapoints to plot and a column which corresponds to hue
    cols: list of column names. default=['x','y','z']
    hue_col: Variables that define subsets of the data, which will be drawn on separate facets in the grid
    hue_color_dict: optional, dictionary of colors which correspond to each hue value. keys are values in hue_col, values are colors
    '''
    fig = plt.figure(figsize=figsize)
    ax = Axes3D(fig)
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_zlabel(zlabel)

    for val in df[hue_col].unique():
        df_val = df[df[hue_col]==val].copy()
        if val in hue_color_dict.keys():
            ax.scatter(df_val[cols[0]], df_val[cols[1]], df_val[cols[2]], label=val, color=hue_color_dict[val])
        else:
            ax.scatter(df_val[cols[0]], df_val[cols[1]], df_val[cols[2]], label=val)

    plt.legend()
    plt.show();
