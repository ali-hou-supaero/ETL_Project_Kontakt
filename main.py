#!/usr/bin/env python3
"""
Kontakt ETL Pipeline - Simple Version

This script runs the complete ETL pipeline:
1. Extract user data from CSV file
2. Clean and transform the data
3. Load the data into PostgreSQL database

Run with: python main.py
"""

from src.extract_data import extract_users
from src.transform_data import clean_users
from src.load_data import load_to_database, verify_data, run_sample_queries, get_connection_string
from notif_meeting import notif_meeting
from data.simulate_and_visualize_france_users import visualize_data

def main():
    """Run the complete ETL pipeline"""
    print("Starting Kontakt ETL Pipeline...")
    print("=" * 50)
    
    # Step 1: Extract data
    print("\n=== EXTRACTION ===")
    print("📥 Extracting data from sources...")
    
    # Call the extraction functions
    users = extract_users()

   
    # Step 2: Transform data
    print("\n=== TRANSFORMATION ===")
    print("🔄 Cleaning and transforming data...")

    # Call the transformation functions
    clean_users_data = clean_users(users)
    
    
    # Step 3: Load data
    print("\n=== LOADING ===")
    print("💾 Loading data to database...")

    # Call the loading function
    load_to_database(clean_users_data)
    
    # Step 4: Verify everything worked
    print("\n=== VERIFICATION ===")
    print("✅ Verifying data was loaded correctly...")

    # Call the verification function
    verify_data()

    run_sample_queries()
    
    print("\n🎉 ETL Pipeline completed!")
    print("=" * 50)

    # Step 5: Example of cluster analysis
    print("\n=== EXAMPLE CLUSTER ANALYSIS ===")
    print("📍 Detecting user clusters in the database...")

    # Step 5.1: Define database connection parameters based on load_data.py information
    db_url = get_connection_string()

    # Step 5.2: Call the function on the "users" table
    clusters = notif_meeting(
        db_url=db_url,
        table_name="users",
        R=150,         # 150 meters radius
        N=5,          # At least 5 users in the group
        timestamp_filter='2025-10-08 18:00:00+02:00'  # Time filter
    )

    # Step 5.3: Display the results
    print("📍 Detected clusters:")
    for i, cluster in enumerate(clusters, 1):
        print(f"Cluster {i}: {cluster}")

    # Step 6: Visualize user data
    print("\n=== VISUALIZATION ===")
    print("📊 Visualizing user data...")
    visualize_data(csv_path='output/detected_clusters.csv', out_png='output/cluster_visualization.png', dotsize=3, n_points=None)
    print("\n")
    print("📊 Visualization saved to 'output/cluster_visualization.png'")

if __name__ == "__main__":
    main()




