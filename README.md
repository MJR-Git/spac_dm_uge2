# specialisterne_dm_uge2

## Table of Contents
- [Project Overview](#project-overview)
- [Data Sources](#data-sources)
- [Tools](#tools)
- [Data Sources](#data-sources)
- [Exploratory Data Analysis](#exploratory-data-analysis)
- [Data Analysis](#data-analysis)
- [Results/Findings](#resultsfindings)
- [Recommendations](#recommendations)
- [Limitations](#limitations)
- [References](#references)



### Project Overview
- [plot](#house_purchase_plot.png)


### Data Sources
All data sources can be found in the data map

- [data/app_log (logfil analyse) - random.txt](<data/app_log (logfil analyse) - random.txt>)
- [data/DKHousingPricesSample100k.csv](data/DKHousingPricesSample100k.csv)
- [data/Navne_liste.txt](data/Navne_liste.txt)
- [data/source_data.csv](data/source_data.csv)

### Opgave 1
The code works by:
1. Running it
2. inputting a path to a text file with comma-seperated words. For example the Navne_liste file in the data folder.
3. The output will then be a sorted list of names, and a count of all characters in a dictionary

In this assignment I was quickly able to get sort the names and get a dictionary. So I spent a bit of time too add the ability for the user to input their own file. And I made a function to sort the dictionary by count. I was actually struggling a bit with ho to sort the dictionary, but ended up converting the dict to a list of dictionaries each with keys "char" and "count" and then sorting this list by count before joining the dictionaries in one again.

### Opgave 2
I completed this assignment with the inbuilt filter and map functions. Afterwards I did think that just using a for loop and immediatedly writing and appending to the new file might make more sense, but I left it as is, since I think there might be some benefit to having the errors in list form as well.

### Opgave 3
I was honestly a bit unsure of what to do here. At first glance it seemed like a try exempt block with a few exemptions added might do the trick. There might be more to it, I'm not too practised in handling errors yet.

### Opgave 4
This was definitely the hardest one--I didn't really have any experience with pandas DataFrames yet. But, in completing it I feel like I learned a lot. Especially on how to think about a DataFrame--basically a dictionary where the keys are column names and the values a list of the column data.


### References
