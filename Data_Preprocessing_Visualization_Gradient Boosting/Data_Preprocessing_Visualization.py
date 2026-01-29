import kagglehub
import pandas as pd
import numpy as np
import warnings
import matplotlib.pyplot as plt
from scipy import stats
from sklearn.preprocessing import minmax_scale 

# Suppress all warnings.
warnings.filterwarnings("ignore")

# A blank.
print ("\n" * 25)

# Download latest version.
path = kagglehub.dataset_download("fedesoriano/heart-failure-prediction")

# The dataset path.
print("Path to dataset files:", path)

# Read a csv file into a dataframe(Data Structure).  
df = pd.read_csv("C:\\Users\\User\\.cache\\kagglehub\\datasets\\fedesoriano\\heart-failure-prediction\\versions\\1\\heart.csv", sep = ",")

# Print with a blank. 
def print_function(p):
    print(f"\n{p}")

# Print dataframe.
print_function(df)

# Data types for each column.
print_function(df.dtypes)

# An Optimization have been made based on data type.  
df = df.convert_dtypes(convert_integer = False, convert_floating = False)

# Display data types.
print_function(df.dtypes)

# Summing the missing values for each column. 
print_function(df.isnull().sum(axis = 0))

# Display numbers that contain how often a value appears for string variables from the data frame.  
for i in range(len(df.columns)):
    if (df.iloc[:,i]).dtypes == "string[python]": 
        print_function(df.iloc[:,i].value_counts())

# Display numbers containing the frequency of a value, but for integers, each number represents a category. 
for i in range(5, 12, 6):
    print_function(df.iloc[:,i].value_counts())

##### WE WILL USE DIAGRAMS TO PRESENT THE VARIABLES, MAKING THE DATA STRUCTURE CLEARER AND PROVIDING AN INITIAL OVERVIEW FROM WHICH IMPORTANT INFORMATION CAN BE GAINED.

# Style sheets.         
plt.style.use("ggplot")

# Creates an image that contains multiple charts at once, in this case it contains histograms. A histogram is the frequency of occurrence(number) of multiple bins(category) in a data set.  
fig, axs = plt.subplots(nrows = 2, ncols= 2)

axs[0, 0].hist(df["Age"], color = "b", edgecolor = "black", bins = 50) # Histogram for variable Age.   

axs[0, 0].set_xlabel("Years", fontsize = 12)

axs[0, 1].hist(df["RestingBP"], color = "g", edgecolor = "black", bins = 50) # Histogram for variable RestingBP. 

axs[0, 1].set_xlabel("Resting Blood Pressure (mm Hg)", fontsize = 12)

axs[1, 0].hist(df["Cholesterol"], color = "r", edgecolor = "black", bins = 50) # Histogram for variable Cholesterol. 

axs[1, 0].set_xlabel("Serum Cholesterol (mm/dl)", fontsize = 12)

axs[1, 1].hist(df["MaxHR"], color = "m", edgecolor = "black", bins = 50) # Histogram for variable MaxHR. 

axs[1, 1].set_xlabel("Maximum Heart Rate Achieved", fontsize = 12)

fig.suptitle("Age(Blue), RestingBP(Green), Cholesterol(Red), MaxHR(Purple)", fontweight = "bold")  # A central image caption. 

fig.tight_layout() # Adjusts subplot parameters so that graphs are visible and do not overlap.

fig, ax = plt.subplots()

ax.hist(df["Oldpeak"], bins = 70, color = "k", edgecolor = "w" ) # Histogram for variable Oldpeak.

ax.set_xlabel("Oldpeak", size = "large")

plt.show()

index_list = [0, 3, 4, 7]

fig, axs = plt.subplots(nrows = 2, ncols= 2)

flierprops = dict(markersize = 9) # We define the color and size of the outliers.

for i in index_list:
    if i == 0:
        row = 0
        col = 0
    elif i == 4:
        row = 1
        col = 0
    box_plot = axs[row, col].boxplot(df.iloc[:,i], patch_artist=True, whis = 3, flierprops=flierprops) # Boxplots(Color parameters are defined and also lines that extend beyond the box plot(whisker).                                                                                                        
    axs[row, col].set_xlabel(df.columns[i])                                                            # Beyond these lines there are variables that differ significantly from the sample(outliers).)
    axs[row, col].set_xticks([])   
    for median in box_plot['medians']: # Set color for boxplot median.
        median.set_color('black')
    col += 1

fig, ax = plt.subplots()

box_plot = ax.boxplot(df["Oldpeak"], patch_artist=True, whis = 3, flierprops=flierprops)
ax.set_xlabel("Oldpeak")
ax.set_xticks([])   
for median in box_plot['medians']:
    median.set_color('black')

plt.show()

###### PEARSON CORRELATION ######

correlation = round(df.select_dtypes("int64").corr(), 2) # We use pearson correlation. It calculates the linear correlation between variables.
                                                         # It is used if we want to check if there is a strong correlation between two variables, positive or negative.
print(correlation) # A matrix with correlations.

correlation = np.array(correlation) # The 6 by 6 vector.

min_correlation, max_correlation = 1, 0


for i in range(len(correlation)): # A loop to find the minimum and maximum value for the Pearson correlation for our variables. 
    for j in range(len(correlation)):
        if abs(correlation[j,i]) > abs(max_correlation) and correlation[j,i] != 1:
            max_correlation = abs(correlation[j,i])
        elif abs(correlation[j,i]) < abs(min_correlation):
            min_correlation = abs(correlation[j,i])

print(f"min_correlation = {min_correlation}, max_correlation = {max_correlation}")

fig, ax = plt.subplots()  

data_image = ax.imshow(correlation, cmap = "Greys") # Displaying data in two-dimensional space as an image.

variable_names_corr = ["Age", "RestingBP", "Cholesterol", "FastingBS", "MaxHR", "HeartDisease"] 

ax.set_xticks(ticks = [0, 1, 2, 3, 4, 5], labels = variable_names_corr, rotation=45, ha="right", rotation_mode="anchor") # Labels in the tick position(x - axis) with some additional variables so the tags are visible.  

ax.set_yticks(ticks = [0, 1, 2, 3, 4, 5], labels = variable_names_corr) # Labels in the tick position(y - axis). 

for i in range(len(variable_names_corr)): # Using the correlation table, text is generated for each block based on the size of the chart.  
    for j in range(len(variable_names_corr)):
        text = ax.text(j, i, correlation[i, j],
                       ha="center", va="center", color="b")
        
ax.grid(False) # Hide grid lines(The pre-expansion of ticks).

fig.tight_layout()

plt.show() # |r| < 0.4 in all cases, indicating a weak linear correlation between variables.

# We can see three lists containing values and strings. These lists will be used to generate loops, which will be used for the creation of bar charts.
value_list = [[496, 203, 173, 46], [552, 188, 178], [460, 395, 63]] # Frequency of each class for variables ChestPainType, RestingECG, ST_Slope.       

name_list = [["Asymptomatic", "Non-Anginal Pain", "Atypical Angina", "Typical Angina"], ["Normal", "LVH", "ST"], ["Flat", "Upsloping", "Downsloping"]] # Variable categories (ChestPainType, RestingECG, ST_Slope).     

color_list = ["b", "r", "g", "k"] # A list containing colors will help with the appearance of bar charts.  

# An image containing multiple bar graphs. A bar chart is used for variables that can take on a limited range of values and the height represents frequency.
fig, axs = plt.subplots(nrows = 2, ncols = 2, sharey=True, layout = "constrained")

for i in range(0, 1): # Conditions are used to add a bar graph to the second line of the image(fig).
    for name in range(0,3):
        if name == 1:
            i = 1
        elif name == 2:
            col = 1
            i = 0
        else:
            col = 0
        for j in range(len(name_list[name])): # Bar plots for variables ChestPainType, RestingECG, ST_Slope. 
            axs[col, i].bar(name_list[name][j], value_list[name][j], label = name_list[name][j], color = color_list[j]) # Creating a bar graph with its parameters.
            axs[col, i].set(xticklabels=[]) # Remove labels from the x-axis.
            axs[col, i].legend() # brief note about the x-axis labels.

axs[1, 1].set_axis_off() # Hides the y,x axes for the selected position.

plt.show() 

two_group = [["Men", "Female"], ["No", "Yes"], ["FastingBS < 120 mg/dl", "FastingBS > 120 mg/dl"], ["heart disease", "Normal"]]

two_group_frequency = [[725, 193], [547, 371], [704, 214], [508, 410]]

count = 0

line = 0

fig, axs = plt.subplots(nrows = 2, ncols = 2, sharey=True, layout = "constrained")

width = 0.27 # The width of the bar on the bar graph.

positions =(0.2, 0.6) # The location of the bars on the x axis. 

for i in range(0,4): 
        if i == 2:
            line = 1
            count = 0
        for j in range(0,1): # Bar plots for variables.  
            axs[line, count].bar(positions[0], two_group_frequency[i][0], width, label = two_group[i][0], color = ["b"], hatch= '/') 
            axs[line, count].bar(positions[1], two_group_frequency[i][1] , width, label = two_group[i][1] , color = ["r"], hatch='\\')
            axs[line, count].set(xticklabels=[])
            axs[line, count].legend()
            count += 1

plt.show()

####### OUTLIERS #######
for out_lier in [3, 4, 9]:
    Q_1 = df.iloc[:,out_lier].quantile(0.25)
    Q_3 = df.iloc[:,out_lier].quantile(0.75) 
    IQR = Q_3 - Q_1
    Lower_Fence = Q_1 - (3 * IQR)
    Upper_Fence = Q_3 + (3 * IQR)
    if out_lier == 3:
        outliers_list = []
    for line in range (df.shape[0]):
        if  df.iloc[line, out_lier]< Lower_Fence or  df.iloc[line, out_lier]> Upper_Fence:
            outliers_list.append(line)

outliers_list.sort()

print(outliers_list)

df = df.drop(outliers_list)

####### Feature Scaling Between 0 and 1 ####### 
df["Age"], df["RestingBP"], df["Cholesterol"], df["MaxHR"], df["Oldpeak"] = (minmax_scale(df["Age"], axis=0), minmax_scale(df["RestingBP"], axis=0), minmax_scale(df["Cholesterol"], axis=0),
minmax_scale(df["MaxHR"], axis=0), minmax_scale(df["Oldpeak"], axis=0)) 

print(df)

print(df.min(axis = 0))

print(df.max(axis = 0))
