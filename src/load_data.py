"""
Data Loading Module

This module handles loading cleaned data into PostgreSQL database:
- Load users data to users table 
- Verify data was loaded correctly
"""

import pandas as pd
from sqlalchemy import create_engine, text
import psycopg2

# Database connection configuration
# TODO: Update these values with your actual database credentials
DATABASE_CONFIG = {
    'username': 'fgerard',
    'password': 'salmonelle', 
    'host': 'localhost',
    'port': '5432',
    'database': 'kontakt_db'
}

def get_connection_string():
    """Build PostgreSQL connection string"""
    return f"postgresql://{DATABASE_CONFIG['username']}:{DATABASE_CONFIG['password']}@{DATABASE_CONFIG['host']}:{DATABASE_CONFIG['port']}/{DATABASE_CONFIG['database']}"

def load_to_database(users_df):
    """
    Load cleaned data into PostgreSQL database
    
    Args:
        users_df (pandas.DataFrame): Cleaned users data
    """
    print("💾 Loading data to PostgreSQL database...")
    
    # TODO: Create connection string using the function above
    connection_string = get_connection_string()
    
    try:
        # TODO: Create SQLAlchemy engine
        engine = create_engine(connection_string)
        
        
        # TODO: Load users data
        
        users_df.to_sql('users', engine, if_exists='replace', index=False)
        # 
        # Parameters explanation:
        # - 'users': table name in database
        # - engine: database connection
        # - if_exists='replace': replace table if it exists (use 'append' to add to existing data)
        # - index=False: don't include pandas row index as a column
        
              
        # TODO: Print loading statistics
        print(f"✅ Loaded {len(users_df)} users to database")
        
        
    except Exception as e:
        print(f"❌ Error loading data to database: {e}")
        print("💡 Make sure:")
        print("   - PostgreSQL is running")
        print("   - Database 'airlife_db' exists") 
        print("   - Username and password are correct")
        print("   - Tables are created (run database_setup.sql)")

def verify_data():
    """
    Verify that data was loaded correctly by running some basic queries
    """
    print("🔍 Verifying data was loaded correctly...")
    
    connection_string = get_connection_string()
    
    try:
        # TODO: Create SQLAlchemy engine
        engine = create_engine(connection_string)
               
        # TODO: Count users in database 
        users_count = pd.read_sql("SELECT COUNT(*) as count FROM users", engine)
        print(f"📊 Users in database: {users_count.iloc[0]['count']}")
        
    
        # TODO: Show sample airport data
        sample_users = pd.read_sql("SELECT * FROM users LIMIT 3", engine)
        print("\n📋 Sample users:")
        print(sample_users.to_string(index=False))
        
       
    except Exception as e:
        print(f"❌ Error verifying data: {e}")

def run_sample_queries():
    """
    Run some interesting queries on the loaded data
    Students can use this to explore their data
    """
    print("📈 Running sample analysis queries...")
    
    connection_string = get_connection_string()
    
    try:
        engine = create_engine(connection_string)
        
        # Query 1: Airports by country
        print("\n🌍 Number of users in Marseille:")
        country_query = """
        SELECT *
        FROM users
        WHERE latitude BETWEEN 43.20 AND 43.40
          AND longitude BETWEEN 5.30 AND 5.45;
        kontakt_db=# SELECT COUNT(*)
        FROM users
        WHERE latitude BETWEEN 43.20 AND 43.40
          AND longitude BETWEEN 5.30 AND 5.45;
        """
        country_results = pd.read_sql(country_query, engine)
        print(country_results.to_string(index=False))
    
    except Exception as e:
        print(f"❌ Error running sample queries: {e}")

def test_database_connection():
    """
    Test database connection without loading data
    Students can use this to debug connection issues
    """
    print("🔌 Testing database connection...")
    
    connection_string = get_connection_string()
    
    try:
        engine = create_engine(connection_string)
        
        # Try a simple query
        result = pd.read_sql("SELECT 1 as test", engine)
        
        if result.iloc[0]['test'] == 1:
            print("✅ Database connection successful!")
            
            # Check if our tables exist
            tables_query = """
            SELECT table_name 
            FROM information_schema.tables 
            WHERE table_schema = 'public' 
            AND table_name IN ('airports', 'flights')
            ORDER BY table_name
            """
            tables = pd.read_sql(tables_query, engine)
            
            if len(tables) == 2:
                print("✅ Required tables (users) exist")
            else:
                print(f"⚠️  Found {len(tables)} tables, expected 2")
                print("💡 Run database_setup.sql to create tables")
            
            return True
        else:
            print("❌ Database connection test failed")
            return False
            
    except Exception as e:
        print(f"❌ Database connection failed: {e}")
        print("💡 Check your connection settings in DATABASE_CONFIG")
        return False

if __name__ == "__main__":
    """Test the loading functions"""
    print("Testing database loading functions...\n")
    
    # Test database connection first
    if test_database_connection():
        print("\nDatabase connection OK. Ready for data loading!")
        
        # Create some sample data for testing
        sample_users = pd.DataFrame({
            'user_id': [28],
            'timestamp': ['2025-10-08 18:00:00+02:00'], 
            'latitude': [48.8566],
            'longitude': [2.3522]
        })
        
        sample_flights = pd.DataFrame()  # Empty for testing
        
        # Test loading (won't work until students implement it)
        load_to_database(sample_users)
    else:
        print("Fix database connection before testing loading functions")
