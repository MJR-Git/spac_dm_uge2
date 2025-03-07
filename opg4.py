import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def main():
    df = get_data(os.path.join("/home/spac-42mjr/workspace/github.com/MJR-Git/specialisterne_dm_uge2/data/DKHousingPricesSample100k.csv"))
    
    print(df.head(10))

    df_subset = df[["house_type", "region"]]

    #group_by_purchase_price = df_subset.groupby(["region", "purchase_price"]).mean()
    group_by_purchases = df_subset.groupby(["house_type", "region"]).value_counts()
    #print(group_by_purchase_price)
    print(group_by_purchases)
    get_plot(df)

    return

def get_data(path):
    with open(path, newline="") as csv_file: 
        d = pd.read_csv(csv_file)
        df = pd.DataFrame(data=d)
        return df

def get_plot(data):
    sns.set_theme(rc={'figure.figsize':(12,10)})
    fig, axes = plt.subplots(1, 2)

 

    sns.countplot(x="region", hue="house_type", data=data, ax=axes[0])

    df_subset = data.query("year_build > 1800")
    df_subset = df_subset.drop_duplicates(subset=["house_id"])
    sns.histplot(x="year_build", hue="region", data=df_subset, ax=axes[1])

    fig1 = fig.get_figure()
    fig1.savefig("house_purchases_plot.png")
    return

if __name__ == "__main__":
     main()