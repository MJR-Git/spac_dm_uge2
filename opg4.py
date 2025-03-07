import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def main():
    df = get_data(os.path.join("/home/spac-42mjr/workspace/github.com/MJR-Git/specialisterne_dm_uge2/data/DKHousingPricesSample100k.csv"))
    
    print(df.head(10))

    df_subset = df[["house_type", "region", "purchase_price"]]

    group_by_purchase_price = df_subset.groupby(["region", "purchase_price"]).mean()
    group_by_purchases = df_subset.groupby(["house_type", "region"]).value_counts()
    print(group_by_purchase_price)
    print(group_by_purchases)
    get_plot(df)

    return

def get_data(path):
    with open(path, newline="") as csv_file: 
        d = pd.read_csv(csv_file)
        df = pd.DataFrame(data=d)
        return df

def get_plot(data):
    house_purchase_plot = sns.countplot(x="region", hue="house_type", data=data)
    plt.ylabel("purchases")
    fig = house_purchase_plot.get_figure()
    fig.savefig("house_purchase_plot.png")
    return

if __name__ == "__main__":
     main()