import numpy as np

# Generate a sample CSV file to run calculations on
csv_content = """Age,Salary,YearsExperience
25,50000,2
30,85000,5
45,120000,15
35,90000,7
22,45000,1
"""
with open("dataset.csv", "w") as f:
    f.write(csv_content)

# Load dataset using NumPy (skipping the string header row)
# columns: 0=Age, 1=Salary, 2=YearsExperience
data = np.genfromtxt("dataset.csv", delimiter=",", skip_header=1)

# Extract column tracks
age = data[:, 0]
salary = data[:, 1]
experience = data[:, 2]

# Calculate Summary Statistics using NumPy vector engines
mean_salary = np.mean(salary)
std_salary = np.std(salary)

# Generate a complete Pearson correlation coefficient matrix
# Rows/Cols map out relative intersections between Age, Salary, and Experience
corr_matrix = np.corrcoef(data, rowvar=False)

print(f"Dataset Loaded Shape: {data.shape}")
print(f"Mean Salary: ${mean_salary:,.2f}")
print(f"Salary Standard Deviation: ${std_salary:,.2f}")
print("\nCorrelation Matrix (Age vs Salary vs Experience):\n", corr_matrix)
print(f"Correlation between Salary and Experience: {corr_matrix[1, 2]:.4f}")