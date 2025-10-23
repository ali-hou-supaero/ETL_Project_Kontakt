"""
Data Extraction Module

This module handles extracting data from the CSV file:
- Extract users data from simulated CSV file
"""

import pandas as pd

def extract_users():
    """
    Extract user data from CSV file
    
    Returns:
        pandas.DataFrame: User data containing user_id, timestamp, latitude, longitude
    """
    print("📄 Reading user data from CSV...")
    
    try:
        # The file is located at: data/simulated_users_france.csv
        df = pd.read_csv("data/simulated_users_france.csv")
    
        print(f"Loaded {len(df)} users")

        return df
        
    except Exception as e:
        print(f"❌ Error reading user data: {e}")
        return pd.DataFrame()



if __name__ == "__main__":
    """Test the extraction functions"""
    print("Testing extraction functions...\n")
    
    # Test user extraction
    users = extract_users()
    print(f"User extraction returned DataFrame with shape: {users.shape}")

    

