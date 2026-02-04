import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class World_happiness:
    def __init__(self):
        self.data = None
        self.arr = np.array([])
        self.last_plot = None
        self.sub_plot = None

    def load_data(self, path=None):
        path = input("Enter CSV file path: ").strip().strip('"')
        try:
             self.data = pd.read_csv(path)
             print("\nFile loaded successfully...")
        except FileNotFoundError:
            print("\nFile not found..")
    
    def explore_data(self):
        if self.data.empty:
            print("load data first.")
            return

        while True:
            print("--------------------------------")
            print("1.Display first 5 row")
            print("2.Display last 5 row")
            print("3.Display columns name")
            print("4.Display data type ")
            print("5.Display basic information")
            print("6.Go Back ")
        
            ch = int(input("Enter your choice:"))

            if ch == 1:
                print(self.data.head())
            elif ch == 2:
                print(self.data.tail())
            elif ch == 3:
                print(self.data.columns)
            elif ch == 4:
                print(self.data.dtypes)
            elif ch == 5:
                print(self.data.info())
            elif ch == 6:
                break
            else:
                print("Invalid  choice")

    def clean_data(self):
        if self.data is None:
            print("Please load dataset first")
            return
        while True:
            print("--------------------------------")
            print("\n1.Display Rows with missing value")
            print("2.Fill missing value with mean")
            print("3.Check Duplicated value")
            print("4.Drop column")
            print("5.Replace missing value with specific value")
            print("6.Go back \n")
    
            ch = int(input("Enter your choice:"))
            if ch == 1:
                print(self.data.isnull().sum())

            elif ch == 2:
                self.data.fillna(self.data.mean(numeric_only=True),inplace=True)
                print(self.data.isnull().sum())

            elif ch == 3:
                print(self.data.duplicated().sum())
            
            elif ch == 4:
                print(self.data.columns)
                col=input("Enter columns name:")
                if col in self.data.columns:  
                    self.data.drop(columns=[col],inplace=True)
                    print(f"\nColumns {col} Dropped successfully...\n")
                else:
                    print("Columns not found")
                    return
                print(self.data.columns)
            
            elif ch == 5: 
                print(self.data.isnull().sum())
                col=input("Enter columns name:")
                value=input("Enter value:")
                self.data.fillna({col:value},inplace=True)
                print(self.data.isnull().sum())
            
            elif ch == 6:
                break
            else:
                print("invalid choice")
    
    def Statistical_Operations(self):
        while True:
            print("--------------------------------")
            print("1.Mean")
            print("2.Medain")
            print("3.Mode")
            print("4.Correlation")
            print("5.Standard Deviation")
            print("6.Variance")
            print("7.Exit")
        
            ch = int(input("Enter your choice"))
        
            if ch == 1:
                res = self.data.mean(numeric_only=True)
                print(res)
            elif ch == 2:
                res = self.data.median(numeric_only=True)
                print(res)
            elif ch == 3:
                col = input("Enter Categorical columns:")
                res = self.data[col].mode()
                print(res)
            elif ch == 4:
                res = self.data.corr(numeric_only=True)
                print(res)
            elif ch == 5:
                res = self.data.std(numeric_only=True)
                print(res)
            elif ch == 6:
                res= self.data.var(numeric_only=True)
                print(res)
        
            elif ch == 7:
                break

    
    def create_numpy(self):
        print("--------------------------------")
        print(self.data.columns)
        cols = input("Enter column names to convert to NumPy (comma-separated, or leave blank for all): ").strip()
        if cols:
            cols = [c.strip() for c in cols.split(',')]
            self.arr = self.data[cols].values
        else:
            self.arr = self.data.values
        print(self.arr[:4])
        print("\nData successfully converted into a NumPy array.") 

    def indexing_slicing(self):
        print("--------------------------------")
        ind = int(input("Enter index:"))
        print("Element :",self.arr[ind])
        s = int(input("Enter start index:"))
        e = int(input("Enter end index:"))
        print("Slice:",self.arr[s:e])
    
    def mathmetical_operation(self):
        print("--------------------------------")
        print("\nAddition :",(self.arr + 3)[:5])
        print("\nSubtract :",(self.arr - 2)[:5])
        print("\nmultiplication :",(self.arr * 2)[:5])
        print("\ndivide :",(self.arr / 2)[:5])



    def search_data(self):
        if self.arr.size == 0:
            print("NumPy array is empty. Convert DataFrame first.")
            return
        print("--------------------------------")
        value = float(input("Enter value to search: "))

        result = self.arr[self.arr == value]

        if result.size > 0:
            print("Value found:", result)
        else:
            print("Value not found.")

    def sort_data(self):
        print("--------------------------------")
        col = input("Enter column name for sorting: ")
        result = self.data.sort_values(by=col, ascending=False)
        print(result)

    def filter_data(self):
        print("--------------------------------")
        value = input("Enter Name:")
        result = self.arr[self.arr["Name"].str.lower() == value.lower()]
        print(result)

    def aggrigation_function(self):
        while True:
            print("--------------------------------")
            print("\n--- Grouping Operations ---")
            print("1. Country-wise Average Happiness Score")
            print("2. Country-wise Score Statistics (Mean / Max / Min)")
            print("3. Country-wise Average GDP")
            print("4. Country vs Happiness Score (Pivot Table)")
            print("5. Country-wise GDP vs Happiness Score")
            print("6. Exit")

            ch = int(input("Enter choice: "))

            if ch == 1:
                result = self.data.groupby("Country")["Score"].mean()
                print(result)

            elif ch == 2:
                result = self.data.groupby("Country")["Score"].agg(["mean", "max", "min"])
                print(result)

            elif ch == 3:
                result = self.data.groupby("Country")["GDP per capita"].mean()
                print(result)

            elif ch == 4:
                res=pd.pivot_table(self.data,values="Score",index="OverallRank",columns="Country",aggfunc="mean")
                print(res)

            elif ch == 5:
                result = self.data.groupby("Country")[["Score", "GDP per capita"]].mean()
                print(result)

            elif ch == 6:
                print("Exit successful.")
                break

            else:
                print("Invalid option! Try again.")

    def data_visuliazation(self):
        sns.set_theme(style="darkgrid",context="paper",font_scale=1.2)

        while True:
            print("--------------------------------")
            print("1.Bar plot")
            print("2.Pie Plot")
            print("3.Line plot")
            print("4.Scatter plot")
            print("5.Histogram plot")
            print("6.Heat Map")
            print("7.Box Plot")
            print("8.Go back")

            ch=int(input("Enter your choice:"))

            if ch == 1:
                d = self.data.sort_values("Score", ascending=False).head(10)
                a = sns.barplot(x="Score", y="Country", data=d)
                a.set_title("Top 10 Happiest Countries")

                for c in a.containers:
                    a.bar_label(c, fmt="%.2f")

                plt.show()


            elif ch==2:
                labels = ["GDP", "Social", "Health", "Freedom"]

                values = self.data[[
                    "GDP per capita",
                    "Social support",
                    "Healthy life expectancy",
                    "Freedom to make life choices"
                ]].mean()

                plt.pie(values, labels=labels, autopct="%.1f%%")
                plt.title("Average Contribution of Happiness Factors")
                plt.show()


            elif ch==3:
                d=self.data.sort_values("OverallRank")
                plt.plot(d["OverallRank"],d["Score"])
                plt.xlabel("Rank")
                plt.ylabel("Score")
                plt.title("Rank vs Happiness Score")
                plt.show()

            elif ch==4:
                sns.scatterplot(x="GDP per capita",y="Score",data=self.data)
                plt.title("GDP vs Happiness Score")
                plt.show()

            elif ch == 5:
                a = sns.histplot(self.data["Score"], bins=15)
                a.set_title("Score Distribution")

                for c in a.containers:
                    a.bar_label(c)

                plt.show()

            elif ch==6:
                sns.heatmap(self.data.corr(numeric_only=True),annot=True)
                plt.title("Correlation Heatmap")
                plt.show()

            elif ch==7:
                sns.boxplot(y="Score",data=self.data)
                plt.title("Happiness Score Spread")
                plt.show()

            elif ch==8:
                break
    
                   
                
    def subplots(self):
        print("--------------------------------")
        fig, a = plt.subplots(2, 3, figsize=(18, 10), dpi=150)

        top10 = self.data.sort_values("Score", ascending=False).head(10)

        sns.barplot(x="Score", y="Country", data=top10, ax=a[0,0])
        a[0,0].set_title("Top 10 Happiest Countries")
        for c in a[0,0].containers:
            a[0,0].bar_label(c, fmt="%.1f")

        a[0,1].pie(top10["Score"], labels=top10["Country"], autopct="%.1f%%")
        a[0,1].set_title("Score Share (Top 10)")

        d = self.data.sort_values("OverallRank")
        a[0,2].plot(d["OverallRank"], d["Score"])
        a[0,2].set_title("Rank vs Score")

        sns.scatterplot(x="GDP per capita", y="Score", data=self.data, ax=a[1,0])
        a[1,0].set_title("GDP vs Score")

        p=sns.histplot(x="Score",data=self.data,ax=a[1,1])
        for i in p.containers:
            p.bar_label(i)
        a[1,1].set_title("Histogram")

        sns.boxplot(y="Score", data=self.data, ax=a[1,2])
        a[1,2].set_title("Score Spread")

        plt.tight_layout()
        plt.show()

   
def main():
    hp = World_happiness()

    while True:
        print("--------------------------------")
        print("\n---Main Menu---")
        print("1.Load Dataset")
        print("2.Explore data")
        print("3.handing missing value")
        print("4.Performing DataFrame Operation")
        print("5.Data Visulization")
        print("6.Subplots")
        print("7.Exit\n")

        ch = int(input("Enter your choice:"))
        if ch == 1:
            hp.load_data()
        elif ch == 2:
            hp.explore_data()
        elif ch == 3:
            hp.clean_data()
        elif ch == 4:
            while True:
                print("--------------------------------")
                print("1.Convert DataFrame to Numpy Array")
                print("2.Indexing and Slicing")
                print("3.mathmetical operation")
                print("4.Statistical_Operations")
                print("5.Search data")
                print("6.sort data")
                print("7.filter data")
                print("8.aggrigation_function")
                print("9.Go back")
        
                ch = int(input("Enter your choice:"))
                if ch == 1:
                    hp.create_numpy()
                elif ch == 2:
                    hp.indexing_slicing()
                elif ch == 3:
                    hp.mathmetical_operation()
                elif ch == 4:
                    hp.Statistical_Operations()
                elif ch == 5:
                    hp.search_data()
                elif ch == 6:
                    hp.sort_data()
                elif ch == 7:
                    hp.filter_data()
                elif ch == 8:
                    hp.aggrigation_function()
                elif ch == 9:
                    break
                else:
                    print("Invalid choice")
                
        elif ch == 5:
            hp.data_visuliazation()
        elif ch == 6:
            hp.subplots()
        elif ch == 7:
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
# "C:\Users\Ritu\Desktop\DATA_ANAYLIST\Practice Datasets-20250813T151928Z-1-001 (1)\Practice Datasets\world_happiness.csv"
