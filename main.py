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
from src.transform_data import clean_users
from src.load_data import load_to_database, verify_data, run_sample_queries

def main():
    """Run the complete ETL pipeline"""
    print("Starting Kontakt ETL Pipeline...")
    print("=" * 50)
    
    # Step 1: Extract data
    print("\n=== EXTRACTION ===")
    print("📥 Extracting data from sources...")
    
    # TODO: Call the extraction functions
    users = extract_users()

   
    # Step 2: Transform data
    print("\n=== TRANSFORMATION ===")
    print("🔄 Cleaning and transforming data...")
    
    # TODO: Call the transformation functions
    clean_users_data = clean_users(users)
    
    
    # Step 3: Load data
    print("\n=== LOADING ===")
    print("💾 Loading data to database...")
    
    # TODO: Call the loading function
    load_to_database(clean_users_data)
    
    # Step 4: Verify everything worked
    print("\n=== VERIFICATION ===")
    print("✅ Verifying data was loaded correctly...")
    
    # TODO: Call the verification function
    verify_data()

    run_sample_queries()
    
    print("\n🎉 ETL Pipeline completed!")
    print("=" * 50)

if __name__ == "__main__":
    main()


from notif_meeting import notif_meeting

# Étape 1 : définir ta chaîne de connexion PostgreSQL
db_url = "postgresql://fgerard:salmonelle@localhost:5432/kontakt_db"

# Étape 2 : appeler la fonction sur la table "users"
clusters = notif_meeting(
    db_url=db_url,
    table_name="users",
    R=100,       # rayon de 1 km
    N=10,          # au moins 2 utilisateurs dans le groupe
    timestamp_filter='2025-10-08 18:00:00+02:00'  # optionnel : filtre temporel
)

# Étape 3 : afficher les résultats
print("📍 Clusters détectés :")
for i, cluster in enumerate(clusters, 1):
    print(f"Cluster {i}: {cluster}")


