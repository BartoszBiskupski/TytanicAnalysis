import pandas as pd
import os
import matplotlib.pyplot as plt
import matplotlib
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import numpy as np


"""matplotlib and pandas basic configuration of displayed format"""
matplotlib.rcParams["font.size"] = 10
matplotlib.rcParams["figure.dpi"] = 100
pd.set_option("display.max_rows", None)
pd.set_option("display.max_columns", None)
pd.set_option('display.expand_frame_repr', False)
pd.set_option('display.max_colwidth', 50)


class FileDataset:
    """Class to load data from CSV / display the table and histogram for Passenger Age"""
    def __init__(self, **kwargs):
        self.hist_attr = kwargs["hist_attr"]
        self.ylabel = kwargs["ylabel"]
        self.xlabel = kwargs["xlabel"]
        self.file_path = kwargs["file_path"]
        self.data = self._load_data()

    def _load_data(self):
        """Loads data and renames columns to more user friendly names"""
        data = pd.read_csv(os.path.join(*self.file_path))
        data = data.rename(columns={"Age": "PassengerAge", "Pclass": "TicketClass", "SibSp": "NumberOfSiblings"})
        return data

    def hist(self):
        """create histogram for passengers Age"""
        plt.hist(self.data[self.hist_attr], color="blue", edgecolor="black", bins=int(80/2))
        plt.xlabel(self.hist_attr)
        plt.ylabel(self.ylabel)
        plt.title(self.xlabel)
        return plt.show()

    def display_table(self):
        """Displays all data in a table format"""
        df = self.data
        print(df.describe())
        print(df)


class SurvivalModel(FileDataset):
    """Regresion model based on train file"""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.data = self.data.drop(["Name", "Ticket", "Cabin", "Embarked", "PassengerId", "Parch"], axis=1)
        self.data["Sex"] = self.data["Sex"].map({"female": 1, "male": 0})
        self.data = self.data.dropna()
        self.target = "Survived"
        self.features = self.data.columns.tolist()
        self.features.remove(self.target)
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(self.data[self.features], self.data[self.target], test_size=0.2, random_state=0)
        self.model = LogisticRegression(max_iter=10000)
        self.model.fit(self.X_train, self.y_train)

    def predict(self):
        """Returns accuracy rate for the mode"""
        y_pred = self.model.predict(self.X_test)
        accuracy = accuracy_score(self.y_test, y_pred)
        print(self.X_test)
        return accuracy

    def get_coefficients(self):
        """Returns coeff rate for the mode"""
        return self.model.coef_[0]

    def plot_coefficients(self):
        """generates coeff bar chart"""
        coefficients = self.get_coefficients()
        most_important_feature = self.data.columns[1:][np.argmax(coefficients)]
        plt.bar(self.data.columns[1:], coefficients)
        plt.xlabel("Feature")
        plt.ylabel("Coefficient")
        plt.title("Feature Coefficients")
        plt.xticks(rotation=45)
        plt.show()

    def predict_proba(self, passenger_data):
        """predicsts survivability based on user input"""
        passenger_data_df = pd.DataFrame(passenger_data, index=[0])
        passenger_data_df = passenger_data_df[self.features]
        proba = self.model.predict_proba(passenger_data_df)[0][1]
        return "Your survival chances are:{: .1%}".format(proba)