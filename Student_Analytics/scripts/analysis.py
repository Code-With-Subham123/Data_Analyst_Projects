import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Creating a Professional Dummy Dataset
def generate_data():
    np.random.seed(42)
    data = {
        'Student_ID': range(1, 101),
        'Attendance': np.random.randint(50, 100, 100),
        'Study_Hours': np.random.randint(1, 10, 100),
    }
    df = pd.DataFrame(data)
    # Logic: Exam Score is influenced by Study Hours and Attendance
    df['Exam_Score'] = (df['Study_Hours'] * 5) + (df['Attendance'] * 0.4) + np.random.randint(1, 15, 100)
    df['Exam_Score'] = df['Exam_Score'].clip(0, 100) # Max marks 100
    return df

def perform_analysis(df):
    print("\n--- Statistical Summary ---")
    print(df[['Attendance', 'Study_Hours', 'Exam_Score']].describe())

    # Visualization: Study Hours vs Exam Score
    plt.figure(figsize=(10, 6))
    sns.regplot(data=df, x='Study_Hours', y='Exam_Score', color='#2563eb')
    plt.title('Correlation: Study Hours vs Exam Score')
    plt.xlabel('Daily Study Hours')
    plt.ylabel('Exam Score (%)')
    plt.grid(True, alpha=0.3)
    
    # Save the plot for GitHub
    plt.savefig('performance_correlation.png')
    print("\n[Success] Analysis plot saved as 'performance_correlation.png'")
    plt.show()

if __name__ == "__main__":
    student_data = generate_data()
    perform_analysis(student_data)