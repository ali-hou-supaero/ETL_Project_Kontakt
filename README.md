# ETL_Project_Kontakt

## Authors
HOUSSENALY Ali
GERARD François
DUSOLLIER Baptiste
SECHET Edouard

## Project overview

This ETL project extracts user-related data, transforms it for analysis, and loads results into a PostgreSQL database. The pipeline also produces a cluster visualization image that summarizes grouping results and includes a notification script for meeting-related alerts.

## Repository organization

- data/ — raw and processed datasets with simulation and visualization code
- src/ — source code
    - extract_data.py — extract data from CSV file
    - load_data — script that handles PostgreSQL connection and loading
    - transform_data — script that handles non-valid data
- ./
    - main.py — main pipeline entrypoint (extract → transform → load → visualize)
    - notif_meeting.py — small notifier for meeting-related events
    - cluster_visualisation.png — generated output showing clustering results

## How to run

1. Configure database authentication
     - Edit the PostgreSQL authentication parameters in src/load_data DATABASE_CONFIG (username and password).

2. Run the pipeline
     - Execute the main pipeline:
         - python src/main.py

3. Output
     - In the terminal, prints should notify that the pipeline was correctly executed
     - cluster_visualiztion.png should have been created or updated - you can modify parameters in the main function to test different cluster detection and visualization
