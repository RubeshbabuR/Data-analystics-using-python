import pandas as pd

# Load the dataset
data = """
Name,Age,Grade,Subject,Score
Alice,15,9,Math,85
Bob,14,9,Science,92
Catherine,15,10,English,78
David,15,10,Math,90
Emily,14,9,Science,88
Frank,16,11,English,75
Grace,15,10,Math,92
Henry,14,9,Science,85
Ivy,16,11,English,80
Jack,15,10,Math,88
"""

# You can save this data to a CSV file and load it with pd.read_csv('filename.csv')
# For this example, we'll load it directly as a string
df = pd.read_csv(pd.compat.StringIO(data))

# Display the dataset
print("Dataset:")
print(df)

# Calculate average score
average_score = df['Score'].mean()
print("\nAverage Score:", average_score)

# Find the highest score
highest_score = df['Score'].max()
print("Highest Score:", highest_score)

# Find the lowest score
lowest_score = df['Score'].min()
print("Lowest Score:", lowest_score)

# Group by Subject and calculate the average score for each subject
subject_scores = df.groupby('Subject')['Score'].mean()
print("\nAverage Scores by Subject:")
print(subject_scores)
