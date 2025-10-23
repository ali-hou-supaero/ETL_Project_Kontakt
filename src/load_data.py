"""
Data Loading Module

This module handles loading cleaned data into PostgreSQL database:
- Load users data to users table 
- Verify data was loaded correctly
"""

import pandas as pd
from sqlalchemy import create_engine, text

# Database connection configuration
#################### YOU SHOULD MODIFY USERNAME AND PASSWORD ####################
DATABASE_CONFIG = {
    'username': 'aliho', # your PostgreSQL username
    'password': 'mdpfacile', # your PostgreSQL password
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

    # Create connection string using the function above
    connection_string = get_connection_string()
    
    try:
        # Create SQLAlchemy engine
        engine = create_engine(connection_string)

        # Load users data
        users_df.to_sql('users', engine, if_exists='replace', index=False)

        # Print loading statistics
        print(f"✅ Loaded {len(users_df)} users to database")
        
        
    except Exception as e:
        print(f"❌ Error loading data to database: {e}")
        print("💡 Make sure:")
        print("   - PostgreSQL is running")
        print("   - Database 'kontakt_db' exists") 
        print("   - Username and password are correct")
        print("   - Tables are created (run database_setup.sql)")

def verify_data():
    """
    Verify that data was loaded correctly by running some basic queries
    """
    print("🔍 Verifying data was loaded correctly...")
    
    connection_string = get_connection_string()
    
    try:
        # Create SQLAlchemy engine
        engine = create_engine(connection_string)

        # Count users in database
        users_count = pd.read_sql("SELECT COUNT(*) as count FROM users", engine)
        print(f"📊 Users in database: {users_count.iloc[0]['count']}")

        # Show sample user data
        sample_users = pd.read_sql("SELECT * FROM users LIMIT 3", engine)
        print("\n📋 Sample users:")
        print(sample_users.to_string(index=False))
        
       
    except Exception as e:
        print(f"❌ Error verifying data: {e}")

def run_sample_queries():
    """
    Run some interesting queries on the loaded data
    """
    print("📈 Running sample analysis queries...")
    
    connection_string = get_connection_string()
    
    try:
        engine = create_engine(connection_string)
        
        # Query 1: Users in Paris and proportion of total users
        print("\n🌍 Number of users in Paris area and proportion of total users:")
        query = """
        SELECT COUNT(*) as user_count, (COUNT(*) * 100.0 / (SELECT COUNT(*) FROM users)) as proportion
        FROM users
        WHERE latitude BETWEEN 48.815 AND 48.902
          AND longitude BETWEEN 2.224 AND 2.469;
        """
        results = pd.read_sql(query, engine)
        print(results.to_string(index=False))

        # Query 2: Users in Marseille and proportion of total users
        print("\n🌍 Number of users in Marseille area and proportion of total users:")
        query = """
        SELECT COUNT(*) as user_count, (COUNT(*) * 100.0 / (SELECT COUNT(*) FROM users)) as proportion
        FROM users
        WHERE latitude BETWEEN 43.20 AND 43.40
          AND longitude BETWEEN 5.30 AND 5.45;
        """
        results = pd.read_sql(query, engine)
        print(results.to_string(index=False))

        # Query 3: Users in Lyon and proportion of total users
        print("\n🌍 Number of users in Lyon area and proportion of total users:")
        query = """
        SELECT COUNT(*) as user_count, (COUNT(*) * 100.0 / (SELECT COUNT(*) FROM users)) as proportion
        FROM users
        WHERE latitude BETWEEN 45.70 AND 45.85
          AND longitude BETWEEN 4.80 AND 5.00;
        """
        results = pd.read_sql(query, engine)
        print(results.to_string(index=False))

    
    except Exception as e:
        print(f"❌ Error running sample queries: {e}")


def test_database_connection():
    """
    Test database connection without loading data
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
            AND table_name IN ('user_id', 'timestamp', 'latitude', 'longitude')
            ORDER BY table_name
            """
            tables = pd.read_sql(tables_query, engine)

            if len(tables) == 4:
                print("✅ Required tables (users) exist")
            else:
                print(f"⚠️  Found {len(tables)} tables, expected 4")
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
