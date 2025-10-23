# ETL_Project_Kontakt

## Authors
HOUSSENALY Ali

GERARD François

DUSOLLIER Baptiste

SECHET Edouard

## Project overview

This ETL project extracts user-related data, transforms it for analysis, and loads results into a PostgreSQL database. The pipeline also produces a cluster visualization image that summarizes grouping results and includes a notification script for meeting-related alerts.

## Repository organization

- docs/ — Report documents
    - report.pdf — project report
    - business_presentation.pdf — presentation done during the business model class
    - dashboard.png — example dashboard to monitor business performances

- data/ — Simulation and visualization code with associated csv data file and png visualization
    - simulate_and_visualize_france_users.py — script to generate simulated data and visualize it in a France map
    - simulated_users_france.csv — output csv data of simulated users
    - france_users_map.png — output visualization of simulated users
    

- src/ — ETL pipeline
    - extract_data.py — extract data from CSV file
    - load_data — script that handles PostgreSQL connection and loading
    - transform_data — script that handles non-valid data

- output/ — Output of notif_meeting.py
    - detected_clusters.csv — output csv data of detected clusters as calculated in notif_meeting.py
    - cluster_visualization.png — output visualization of clusters

- ./ — Code execution
    - main.py — main pipeline entrypoint (extract → transform → load → visualize)
    - notif_meeting.py — notifier for meeting-related events
    - cluster_visualisation.png — generated output showing clustering results

## How to run

1. Configure database authentication
     - Edit the PostgreSQL authentication parameters in src/load_data DATABASE_CONFIG (username and password).

2. Run the pipeline
     - Execute the main pipeline: python src/main.py

3. Output
     - In the terminal, prints should notify that the pipeline was correctly executed
     - output/cluster_visualiztion.png should have been created or updated - you can modify parameters in the main function to test different cluster detection and visualization
