#!/usr/bin/env python3
"""
Kontakt ETL Pipeline - Simple Version

This script runs the complete ETL pipeline:
1. Extract airport data from CSV and flight data from API
2. Clean and transform the data
3. Load the data into PostgreSQL database

Run with: python main.py
"""

from src.extract_data import extract_users
# from src.transform_data import clean_airports, clean_flights, combine_data
from src.load_data import load_to_database, verify_data

def main():
    """Run the complete ETL pipeline"""
    print("Starting Kontakt ETL Pipeline...")
    print("=" * 50)
    
    # Step 1: Extract data
    print("\n=== EXTRACTION ===")
    print("📥 Extracting data from sources...")
    
    # TODO: Call the extraction functions
    users = extract_users()

   
    
    # Uncomment the lines above once you've implemented the functions
    # print("⚠️  Extraction functions not yet implemented")
    
    
    # Step 2: Transform data
    print("\n=== TRANSFORMATION ===")
    print("🔄 Cleaning and transforming data...")
    
    # TODO: Call the transformation functions
    clean_airports_data = clean_airports(airports)
    clean_flights_data = clean_flights(flights)
    final_airports, final_flights = combine_data(clean_airports_data, clean_flights_data)
    
    # Step 3: Load data
    print("\n=== LOADING ===")
    print("💾 Loading data to database...")
    
    # TODO: Call the loading function
    load_to_database(final_airports, final_flights)
    
    # Step 4: Verify everything worked
    print("\n=== VERIFICATION ===")
    print("✅ Verifying data was loaded correctly...")
    
    # TODO: Call the verification function
    verify_data()
    
    print("\n🎉 ETL Pipeline completed!")
    print("=" * 50)

if __name__ == "__main__":
    main()
