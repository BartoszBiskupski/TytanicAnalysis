import pandas as pd
import os
import matplotlib.pyplot as plt
import matplotlib
from tabulate import tabulate
import seaborn as sns
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import numpy as np

matplotlib.rcParams["font.size"] = 10
matplotlib.rcParams["figure.dpi"] = 100
pd.set_option("display.max_rows", None)
pd.set_option("display.max_columns", None)
pd.set_option('display.expand_frame_repr', False)
pd.set_option('display.max_colwidth', 50)



class FileDataset:
    def __init__(self, **kwargs):
        self.hist_attr = kwargs["hist_attr"]
        self.ylabel = kwargs["ylabel"]
        self.xlabel = kwargs["xlabel"]
        self.file_path = kwargs["file_path"]
        self.data = self._load_data()

    def _load_data(self):
        data = pd.read_csv(os.path.join(*self.file_path))
        data = data.rename(columns={"Age": "PassengerAge", "Pclass": "TicketClass", "SibSp": "NumberOfSiblings"})
        return data

    def hist(self):
        plt.hist(self.hist_attr, color="blue", edgecolor="black", bins=int(45 / 1))
        plt.xlabel(self.hist_attr)
        plt.ylabel(self.ylabel)
        plt.title(self.xlabel)
        return plt.show()

    def display_table(self):
        """Displays all data in a table format"""
        df = self.data
        print(df.describe())
       #print(tabulate(df, headers="keys", tablefmt="fancy_grid", showindex=False, col_width=30))
        print(df)

    def categorical_correlation(self):
        corr = {}
        for column in self.data.columns:
            if column != "Survived":
                corr[column] = self.data["Survived"].corr(self.data[column])
        return corr

    def corr_chart(self):
        df = self.data
        df = df.dropna()
        sns.regplot(x="Sex", y="Survived", data=df)
        plt.title("Regression Plot of Age vs Survived")
        return plt.show()


class SurvivalModel(FileDataset):
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
        y_pred = self.model.predict(self.X_test)
        accuracy = accuracy_score(self.y_test, y_pred)
        print(self.X_test)
        return accuracy

    def get_coefficients(self):
        return self.model.coef_[0]

    def plot_coefficients(self):
        coefficients = self.get_coefficients()
        most_important_feature = self.data.columns[1:][np.argmax(coefficients)]
        plt.bar(self.data.columns[1:], coefficients)
        plt.xlabel("Feature")
        plt.ylabel("Coefficient")
        plt.title("Feature Coefficients")
        plt.xticks(rotation=45)
        plt.show()

    def predict_proba(self, passenger_data):
        passenger_data_df = pd.DataFrame(passenger_data, index=[0])
        passenger_data_df = passenger_data_df[self.features]
        proba = self.model.predict_proba(passenger_data_df)[0][1]
        return "Your survival chances are:{: .1%}".format(proba)


# file_obj = FileDataset(**kwargs)
# obj = SurvivalModel(**kwargs)
# print(obj.features)
# coeffis = obj.get_coefficients()
# print(coeffis)
#
# passenger = {"TicketClass": 2,
#              "Sex": 0,
#              "PassengerAge": 24,
#              "NumberOfSiblings": 0,
#              "Fare": 44
#              }
#
#
# most_important_feature = obj.data.columns[1:][np.argmax(coeffis)]
# print("The most important feature for survival is:", most_important_feature)
# print(obj.predict_proba(passenger))
#
