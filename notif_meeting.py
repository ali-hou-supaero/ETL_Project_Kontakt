import math
import pandas as pd
import numpy as np
from sklearn.cluster import DBSCAN
from sqlalchemy import create_engine

# filepath: detect_user_clusters.py

def notif_meeting(db_url: str, table_name: str, R=1000, N=10, timestamp_filter=None):
    """
    Détecte les groupes d'utilisateurs (>=N) dans un rayon R (mètres).
    
    Args:
        db_url: URL SQLAlchemy (ex: "postgresql://user:pwd@localhost/db")
        table_name: Nom de la table contenant les utilisateurs
        R: Rayon maximal (m)
        N: Nombre minimal d'utilisateurs dans le groupe
        timestamp_filter: Filtre optionnel sur timestamp (ex: '2025-10-21 12:00:00')
    
    Returns:
        List[List[int]] : liste de groupes de user_id
    """
    engine = create_engine(db_url)
    query = f"SELECT user_id, timestamp, latitude, longitude FROM {table_name}"
    if timestamp_filter:
        query += f" WHERE timestamp = '{timestamp_filter}'"
    df = pd.read_sql(query, engine)
    if df.empty:
        return []

    coords = np.radians(df[['latitude', 'longitude']].values)
    eps_rad = R / 6371000  # conversion m → radians

    clustering = DBSCAN(eps=eps_rad, min_samples=N, metric='haversine').fit(coords)
    df['cluster'] = clustering.labels_

    clusters = []
    for cluster_id in set(df['cluster']):
        if cluster_id == -1:
            continue
        members = df[df['cluster'] == cluster_id]['user_id'].tolist()
        if len(members) >= N:
            clusters.append(members)

    return clusters
