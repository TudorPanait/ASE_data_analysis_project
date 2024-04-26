import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def main():
    st.set_page_config(
    page_title="Data Analysis Project",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded")

    # Sidebar configuration
    with st.sidebar:
        ## Add a title to the sidebar
        st.markdown("# Authors\n\n"
                    "Tudor-Alexandru PANAIT\n\n"
                    "Andrei-Florin VREMĂROIU\n\n")
        
        st.link_button(url="https://github.com/TudorPanait", label="See GitHub Repository")

    # Page title
    st.markdown("# Data Analysis Project\n\n"
                "Version: April 26, 2024\n")
    
    # First section - Dataset
    st.markdown("## Dataset\n\n"
                "The dataset used in this project is one that we've created using collected data publicly available on the internet.\n\n"
                "It contains information about the players that are expected to play at the EURO 2024 competition.\n\n")
    
    # Import the dataset
    df = pd.read_csv('dataset.csv')

    # Display the dataframe
    st.dataframe(df)
    
    # Second section - Data Analysis
    st.markdown("## Data Analysis\n\n"
                "In this section, we will analyze the dataset to extract valuable insights about the players.\n\n")
    
    st.markdown("### Player Info\n\n"
                "Let's analyze general information about our players.\n\n")
    
    # Age Distribution of Players
    plt.figure(figsize=(10,6))
    sns.histplot(df['Age'], bins=20, kde=False)
    plt.title('Age Distribution of Players')
    st.pyplot(plt)
    
    col1, col2 = st.columns(2)

    with col1: 
        # Clubs Distribution of Players
        club_counts = df['Current club'].value_counts()
        plt.figure(figsize=(10,6))
        club_counts[::-1].plot.barh()
        plt.title('Clubs Distribution of Players')
        st.pyplot(plt)

    with col2:
        # Club League Distribution of Players
        league_counts = df['Club league'].value_counts()
        plt.figure(figsize=(10,6))
        league_counts[::-1].plot.barh()  # Reverse the order
        plt.title('Club League Distribution of Players')
        st.pyplot(plt)

    st.markdown("### Player Performance\n\n"
                "Let's analyze the performance of our players.\n\n")
    
    # Market Value Distribution of Players
    bins = [0, 1000000, 5000000, 10000000, float('inf')]
    labels = ['<1M', '1M-5M', '5M-10M', '10M-50M']

    df['Market value bin'] = pd.cut(df['Market value'], bins=bins, labels=labels)
    market_value_counts = df['Market value bin'].value_counts()

    plt.figure(figsize=(10,6))
    plt.pie(market_value_counts, labels=market_value_counts.index, autopct='%1.1f%%')
    plt.title('Market Value Distribution of Players')
    st.pyplot(plt)
    
    col1, col2 = st.columns(2)

    with col1: 
        # Goals Scored vs. Assists
        plt.figure(figsize=(10,6))
        sns.scatterplot(x='Goals scored', y='Assists', data=df)
        plt.axhline(df['Assists'].median(), color='red', linestyle='--')  # Median line for Assists
        plt.axvline(df['Goals scored'].median(), color='blue', linestyle='--')  # Median line for Goals scored
        plt.title('Goals Scored vs. Assists')
        st.pyplot(plt)

    with col2:
        # Goals Scored vs. Selections
        plt.figure(figsize=(10,6))
        sns.scatterplot(x='Goals scored', y='Selections', data=df)
        plt.axhline(df['Selections'].median(), color='red', linestyle='--')  # Median line for Selections
        plt.axvline(df['Goals scored'].median(), color='blue', linestyle='--')  # Median line for Goals scored
        plt.title('Goals Scored vs. Selections')
        st.pyplot(plt)
    
if __name__ == "__main__":
    main()