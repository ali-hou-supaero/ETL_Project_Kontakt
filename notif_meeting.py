import pandas as pd
import numpy as np
from sklearn.cluster import DBSCAN
from sqlalchemy import create_engine

def notif_meeting(db_url: str, table_name: str, R=1000, N=10, timestamp_filter=None):
    """
    Detects groups of users (>=N) within radius R (meters).
    
    Args:
        db_url: URL SQLAlchemy (ex: "postgresql://user:pwd@localhost/db")
        table_name: Table name containing user data
        R: Maximum radius (m)
        N: Minimum number of users in the group
        timestamp_filter: Optional timestamp filter (ex: '2025-10-21 12:00:00')

    Returns:
        List[List[int]] : list of user_id groups
    """
    engine = create_engine(db_url)
    query = f"SELECT user_id, timestamp, latitude, longitude FROM {table_name}"
    if timestamp_filter:
        query += f" WHERE timestamp = '{timestamp_filter}'"
    df = pd.read_sql(query, engine)
    if df.empty:
        return []

    coords = np.radians(df[['latitude', 'longitude']].values)
    eps_rad = R / 6371000  # conversion meters → radians

    clustering = DBSCAN(eps=eps_rad, min_samples=N, metric='haversine').fit(coords)
    df['cluster'] = clustering.labels_

    clusters = []
    for cluster_id in set(df['cluster']):
        if cluster_id == -1:
            continue
        members = df[df['cluster'] == cluster_id]['user_id'].tolist()
        if len(members) >= N:
            clusters.append(members)

    # Generate CSV file with clusters in format user_id, timestamp, latitude, longitude
    clusters_data = []
    for cluster_id in set(df['cluster']):
        if cluster_id == -1:
            continue
        cluster_members = df[df['cluster'] == cluster_id]
        for _, row in cluster_members.iterrows():
            clusters_data.append({
                'cluster_id': cluster_id,
                'user_id': row['user_id'],
                'timestamp': row['timestamp'],
                'latitude': row['latitude'],
                'longitude': row['longitude']
            })
    clusters_df = pd.DataFrame(clusters_data)
    clusters_df.to_csv('data/detected_clusters.csv', index=False)

    # Return list of clusters
    return clusters
