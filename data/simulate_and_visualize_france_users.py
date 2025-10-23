# How to use:
#   python simulate_and_visualize_france_users.py simulate : to generate simulated data CSV
#   python simulate_and_visualize_france_users.py visualize : to plot all points
#   python simulate_and_visualize_france_users.py visualize N : to plot N random points
# Example:
#   python simulate_and_visualize_france_users.py visualize 2000 : visualize France map with 2000 random points

import sys
import os
import numpy as np
import pandas as pd
import geopandas as gpd
from shapely.geometry import Point, Polygon, MultiPolygon, box
import matplotlib.pyplot as plt

# -----------------------------
# Part 1: Data simulation
# -----------------------------

def get_metropolitan_france_geometry():
    world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
    france_all = world[world['iso_a3'] == 'FRA'].to_crs('EPSG:4326')

    # Define bounding box for mainland France using shapely
    bbox = box(-5.5, 41.0, 9.8, 51.5)
    bbox_gdf = gpd.GeoDataFrame(geometry=[bbox], crs='EPSG:4326')

    # Clip to that bounding box to remove overseas territories
    france_mainland = gpd.clip(france_all, bbox_gdf)

    return france_mainland.geometry.unary_union


def simulate_data(output_csv='simulated_users_france.csv', seed=42):
    np.random.seed(seed)
    france = get_metropolitan_france_geometry()

    total = 10000
    clusters_total = int(total * 0.70)
    paris_count = int(total * 0.50)
    lyon_count = 1000
    marseille_count = 1000
    scattered_count = total - clusters_total

    paris_center = (48.8566, 2.3522)
    lyon_center = (45.7640, 4.8357)
    marseille_center = (43.2965, 5.3698)

    def sample_cluster(center, n, lat_std=0.02, lon_std=0.03):
        lat0, lon0 = center
        pts = []
        attempts = 0
        while len(pts) < n:
            batch = max(100, n - len(pts))
            lats = np.random.normal(lat0, lat_std, size=batch)
            lons = np.random.normal(lon0, lon_std, size=batch)
            for la, lo in zip(lats, lons):
                p = Point(lo, la)
                if france.contains(p):
                    pts.append((la, lo))
            attempts += 1
            if attempts > 1000:
                break
        return pts[:n]

    paris_pts = sample_cluster(paris_center, paris_count, lat_std=0.02, lon_std=0.02)
    lyon_pts = sample_cluster(lyon_center, lyon_count, lat_std=0.02, lon_std=0.02)
    marseille_pts = sample_cluster(marseille_center, marseille_count, lat_std=0.02, lon_std=0.02)

    minx, miny, maxx, maxy = -5.5, 41.0, 9.8, 51.5
    scattered_pts = []
    attempts = 0
    while len(scattered_pts) < scattered_count:
        needed = scattered_count - len(scattered_pts)
        xs = np.random.uniform(minx, maxx, size=needed * 2)
        ys = np.random.uniform(miny, maxy, size=needed * 2)
        for x, y in zip(xs, ys):
            p = Point(x, y)
            if france.contains(p):
                scattered_pts.append((y, x))
                if len(scattered_pts) >= scattered_count:
                    break
        attempts += 1
        if attempts > 1000:
            raise RuntimeError('Too many attempts generating scattered points.')

    coords = paris_pts + lyon_pts + marseille_pts + scattered_pts

    tz = 'Europe/Paris'
    fixed_ts = pd.Timestamp('2025-10-08 18:00:00', tz=tz)
    timestamps = [fixed_ts] * 9000
    seconds_before_18h = np.random.randint(0, 18 * 3600, size=1000)
    random_ts = [pd.Timestamp('2025-10-08', tz=tz) + pd.to_timedelta(int(s), unit='s') for s in seconds_before_18h]
    timestamps.extend(random_ts)

    user_ids = np.arange(1, total + 1)
    df = pd.DataFrame({
        'user_id': user_ids,
        'timestamp': timestamps,
        'latitude': [c[0] for c in coords],
        'longitude': [c[1] for c in coords]
    })

    df = df.sample(frac=1, random_state=seed).reset_index(drop=True)
    df['timestamp'] = df['timestamp'].astype(str)
    df.to_csv(output_csv, index=False)
    print(f'Saved {len(df)} samples to {output_csv}')

# -----------------------------
# Part 2: Visualization
# -----------------------------

def visualize_data(csv_path='simulated_users_france.csv', out_png='france_users_map.png', dotsize=3, n_points=None):
    if not os.path.exists(csv_path):
        raise FileNotFoundError(f'CSV file not found: {csv_path}')

    df = pd.read_csv(csv_path)
    if n_points is not None and n_points < len(df):
        df = df.sample(n=n_points, random_state=42)
        print(f'Sampled {n_points} random points from {len(df)} total.')

    gdf_points = gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df['longitude'], df['latitude']), crs='EPSG:4326')

    france = get_metropolitan_france_geometry()
    france_gdf = gpd.GeoDataFrame(geometry=[france], crs='EPSG:4326')

    fig, ax = plt.subplots(figsize=(8, 10))
    france_gdf.boundary.plot(ax=ax, linewidth=1, color='black')
    gdf_points.plot(ax=ax, markersize=dotsize, alpha=0.6)

    minx, miny, maxx, maxy = france_gdf.total_bounds
    xmargin = (maxx - minx) * 0.05
    ymargin = (maxy - miny) * 0.05
    ax.set_xlim(minx - xmargin, maxx + xmargin)
    ax.set_ylim(miny - ymargin, maxy + ymargin)

    ax.set_title('Simulated users — Metropolitan France')
    ax.set_xlabel('Longitude')
    ax.set_ylabel('Latitude')

    plt.tight_layout()
    fig.savefig(out_png, dpi=300)
    print(f'Plot saved to {out_png}')

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: python simulate_and_visualize_france_users.py [simulate|visualize] [N_points]')
        sys.exit(1)
    cmd = sys.argv[1].lower()
    if cmd == 'simulate':
        simulate_data()
    elif cmd == 'visualize':
        n_points = int(sys.argv[2]) if len(sys.argv) > 2 else None
        visualize_data(n_points=n_points)
    else:
        print('Unknown command. Use "simulate" or "visualize".')
