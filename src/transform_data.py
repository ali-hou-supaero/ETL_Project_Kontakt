"""
Data Transformation Module

This module handles cleaning and transforming the extracted data:
- Clean user data (remove invalid coordinates, handle missing values)
"""

import pandas as pd

def clean_users(user_df):
    """
    Clean and validate user data
    
    Args:
        user_df (pandas.DataFrame): Raw user data from CSV
        
    Returns:
        pandas.DataFrame: Cleaned user data
    """
    if user_df.empty:
        print("⚠️  No user data to clean")
        return user_df
    
    print(f"🧹 Cleaning user data...")
    print(f"Starting with {len(user_df)} users")
    
    # Make a copy to avoid modifying the original
    df = user_df.copy()
    
    # Remove rows with missing latitude or longitude
    df = df.dropna(subset=['latitude', 'longitude'])
    
    # Remove users with invalid coordinates
    # Latitude should be between -90 and 90
    # Longitude should be between -180 and 180
    df = df[(df['latitude'] >= -90) & (df['latitude'] <= 90)]
    df = df[(df['longitude'] >= -180) & (df['longitude'] <= 180)]
    
    # Convert timestamp to DataTime
    df['timestamp'] = pd.to_datetime(df['timestamp'], errors = 'coerce')
    # Remove users with invalid timestamp
    # Should be at 18:00:00
    df = df[df['timestamp'].dt.hour == 18]
       
    # Convert altitude and longitude to numeric (handle non-numeric values)
    df['latitude'] = pd.to_numeric(df['latitude'], errors='coerce')
    df['longitude'] = pd.to_numeric(df['longitude'], errors='coerce')
       
    # Print how many users remain after cleaning
    print(f"After cleaning: {len(df)} users remain")
    
    return df

def validate_data_quality(df):
    """
    Helper function to check data quality
    
    Args:
        df (pandas.DataFrame): Data to validate
    """
    if df.empty:
        print(f"⚠️  No 'users' data to validate")
        return
    
    print(f"📊 Data quality report for 'users':")
    print(f"   Total records: {len(df)}")
    
    # Check for missing values
    missing_values = df.isnull().sum()
    if missing_values.any():
        print("   Missing values:")
        for col, count in missing_values[missing_values > 0].items():
            print(f"     {col}: {count}")
    else:
        print("   ✅ No missing values")
    
    # Check coordinate bounds if applicable
    if 'latitude' in df.columns and 'longitude' in df.columns:
        invalid_coords = (
            (df['latitude'] < -90) | (df['latitude'] > 90) |
            (df['longitude'] < -180) | (df['longitude'] > 180)
        ).sum()
        
        if invalid_coords > 0:
            print(f"   ⚠️  {invalid_coords} records with invalid coordinates")
        else:
            print("   ✅ All coordinates are valid")

if __name__ == "__main__":
    """Test the transformation functions with sample data"""
    print("Testing transformation functions...\n")
    
    # Create sample users data for testing
    sample_users = pd.DataFrame({
        'id': ['6253', '1003', '2570'],
        'timestamp': ['2025-10-08 18:00:00+02:00', '2025-10-08 18:00:00+02:00', '2025-10-08 17:00:00+02:00'], #Last one is invalid
        'latitude': [48.8566, 51.4700, 999],  # Last one is invalid
        'longitude': [2.3522, -0.4543, -999],  # Last one is invalid
    })
    
    # Test airport cleaning
    cleaned_users = clean_users(sample_users)
    validate_data_quality(cleaned_users)
    
    print("\nTransformation testing complete!")