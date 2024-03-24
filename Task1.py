import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Task 1: Data Exploration
#load dataset
youtube_data = pd.read_csv("youtubers_df.csv")
print(youtube_data.info())

# Check for missing data and outliers
print(youtube_data.describe())
plt.boxplot(youtube_data['Subscribers'])
plt.show()

# Task 2: Trend Analysis
# Identify popular categories using bar plots or pie charts
category_counts = youtube_data['Categories'].value_counts()
category_counts.plot(kind='bar')
plt.xlabel('Categories')
plt.ylabel('Count')
plt.title('Popular Categories')
plt.show()

# Explore correlation between subscribers and likes/comments using scatter plots
sns.scatterplot(x='Subscribers', y='Likes', data=youtube_data)
plt.show()

# Task 3: Audience Study
# Analyze audience distribution by country using bar plots or maps
country_counts = youtube_data['Country'].value_counts()
country_counts.plot(kind='bar')
plt.xlabel('Country')
plt.ylabel('Count')
plt.title('Audience Distribution by Country')
plt.show()

# Task 4: Performance Metrics
# Calculate and visualize average metrics using summary statistics and boxplots
avg_metrics = youtube_data[['Subscribers', 'Visits', 'Likes', 'Comments']].mean()
print(avg_metrics)
sns.boxplot(data=youtube_data[['Subscribers', 'Visits', 'Likes', 'Comments']])
plt.xticks(rotation=45)
plt.show()

# Task 5: Content Categories
# Explore distribution of content categories using bar plots or pie charts
category_counts = youtube_data['Categories'].value_counts()
category_counts.plot(kind='bar')
plt.xlabel('Categories')
plt.ylabel('Count')
plt.title('Content Categories Distribution')
plt.show()

# Task 6: Brands and Collaborations
# Analyze relationships between performance metrics and brand collaborations using scatter plots
#sns.scatterplot(x='Performance Metric', y='Brand Collaborations', data=youtube_data)
#plt.show()

# Task 7: Benchmarking
# Identify top-performing content creators using ranking and comparison metrics
top_creators = youtube_data[(youtube_data['Subscribers'] > youtube_data['Subscribers'].mean()) &
                            (youtube_data['Likes'] > youtube_data['Likes'].mean()) &
                            (youtube_data['Comments'] > youtube_data['Comments'].mean())]
print(top_creators)
