import pandas as pd
import os
import matplotlib.pyplot as plt
import matplotlib
from tabulate import tabulate


matplotlib.rcParams['font.size'] = 10
matplotlib.rcParams['figure.dpi'] = 100


class FileDataset:
    def __init__(self, **kwargs):
        self.kwargs = kwargs
        self.data = self._load_data()
#        self.hist = scatter

    def _load_data(self):
        path = os.path.join(*self.kwargs["file_path"])
        delim = self.kwargs["delimiter"]
        if os.path.splitext(path)[-1] == ".csv":
            data = pd.read_csv(path, delimiter=delim, header=0)
        else:
            raise ValueError(f"File format not supported: {path}")
        return data

    def scatter(self):
        hist_attr = self.kwargs["hist_attr"]
        ylabel = self.kwargs["ylabel"]
        xlabel = self.kwargs["xlabel"]
        plt.hist(self.data[hist_attr], color="blue", edgecolor="black", bins=int(45 / 1))
        plt.xlabel(hist_attr)
        plt.ylabel(ylabel)
        plt.title(xlabel)
        return plt.show()

    def display_table(self, **kwargs):
        df = self.data
        """Displays all data in a table format"""
        print(tabulate(df.data.head(250), headers="keys", tablefmt="psql"))


