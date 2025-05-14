# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

# Set style for better looking plots
sns.set(style="whitegrid")

# Task 1: Load and Explore the Dataset
def load_and_explore_data():
    """Load and explore the Iris dataset"""
    try:
        # Load the iris dataset
        iris = load_iris()
        df = pd.DataFrame(data=np.c_[iris['data'], iris['target']],
                         columns=iris['feature_names'] + ['target'])
        
        # Map target values to species names
        df['species'] = df['target'].map({0: 'setosa', 1: 'versicolor', 2: 'virginica'})
        
        # Display first few rows
        print("\nFirst 5 rows of the dataset:")
        print(df.head())
        
        # Explore structure
        print("\nDataset information:")
        print(df.info())
        
        # Check for missing values
        print("\nMissing values per column:")
        print(df.isnull().sum())
        
        # Since there are no missing values, no cleaning needed
        # But we'll demonstrate the cleaning step anyway
        df_clean = df.dropna()  # This won't do anything since there are no NAs
        
        return df_clean
    
    except Exception as e:
        print(f"Error loading dataset: {e}")
        return None

# Task 2: Basic Data Analysis
def perform_basic_analysis(df):
    """Perform basic statistical analysis on the dataset"""
    if df is None:
        return
    
    print("\nBasic statistics for numerical columns:")
    print(df.describe())
    
    # Group by species and compute mean for numerical columns
    print("\nMean values by species:")
    print(df.groupby('species').mean())
    
    # Find interesting patterns
    print("\nInteresting findings:")
    print("- Setosa has significantly smaller petal dimensions than other species")
    print("- Versicolor and virginica have more overlap in measurements")
    print("- Sepal width has the smallest variation across species")

# Task 3: Data Visualization
def create_visualizations(df):
    """Create various visualizations of the data"""
    if df is None:
        return
    
    # Set up the figure layout
    plt.figure(figsize=(15, 12))
    
    # 1. Line chart (simulating trends over time - we'll use index as pseudo-time)
    plt.subplot(2, 2, 1)
    df['sepal length (cm)'].plot(kind='line', title='Sepal Length Trend (by index)')
    plt.xlabel('Index (pseudo-time)')
    plt.ylabel('Sepal Length (cm)')
    
    # 2. Bar chart (average petal length per species)
    plt.subplot(2, 2, 2)
    df.groupby('species')['petal length (cm)'].mean().plot(kind='bar', color=['red', 'green', 'blue'])
    plt.title('Average Petal Length by Species')
    plt.ylabel('Petal Length (cm)')
    
    # 3. Histogram (distribution of sepal width)
    plt.subplot(2, 2, 3)
    sns.histplot(df['sepal width (cm)'], bins=15, kde=True)
    plt.title('Distribution of Sepal Width')
    plt.xlabel('Sepal Width (cm)')
    
    # 4. Scatter plot (sepal length vs petal length)
    plt.subplot(2, 2, 4)
    sns.scatterplot(data=df, x='sepal length (cm)', y='petal length (cm)', hue='species')
    plt.title('Sepal Length vs Petal Length by Species')
    
    plt.tight_layout()
    plt.show()
    
    # Additional visualization: Pairplot to show all relationships
    print("\nGenerating pairplot (this may take a moment)...")
    sns.pairplot(df, hue='species')
    plt.suptitle('Pairwise Relationships in Iris Dataset', y=1.02)
    plt.show()

# Main execution
if __name__ == "__main__":
    print("Starting data analysis...")
    
    # Task 1
    print("\n=== TASK 1: LOAD AND EXPLORE DATASET ===")
    iris_df = load_and_explore_data()
    
    # Task 2
    print("\n=== TASK 2: BASIC DATA ANALYSIS ===")
    perform_basic_analysis(iris_df)
    
    # Task 3
    print("\n=== TASK 3: DATA VISUALIZATION ===")
    create_visualizations(iris_df)
    
    print("\nAnalysis complete!")