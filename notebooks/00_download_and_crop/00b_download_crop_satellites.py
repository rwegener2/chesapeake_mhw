#########
# This script ...
# Runtime on my local machine ~2 hours
# This script generates the file L4_GHRSST-SSTfnd-Geo_Polar_Blended_Night-GLOB-v02.0-fv01.0_CB_{start_date}_{end_date}.nc
# at the location of the output directory specified in this file
#########

import os
import glob
import time
import requests
from requests.exceptions import Timeout
from datetime import datetime

import xarray as xr

# global variables
# Path to a .txt file containing a \n seperated list of filepaths to download
start_date = '20020901'
end_date = '20230831'
FILEPATHS_TXT = f'filepaths_geopolar_{start_date}_{end_date}.txt'
REPO_ROOT = '/Users/rwegener/repos/chesapeake_mhw/'

# OUTPUT_DIR = '/Users/rwegener/repos/mhw_ocetrac_census/data/SST-geopolar-chesapeake/v2/'

# Build output filepath
def create_filepath(url):
    # Use original name, with _CB appended
    filename = os.path.basename(url).split('.nc')[0] + '_CB.nc'
    return os.path.join(OUTPUT_DIR, filename)

# Read the filepaths from the file into a list
with open(FILEPATHS_TXT) as f:
    filepaths = f.read().splitlines()

# Check that files were found
if len(filepaths) == 0:
    raise Exception('No lines found in FILEPATHS.TXT')

# Create the temp dir, if it doesn't exist
if not os.path.exists('./scratch'):  
    os.mkdir('./scratch')

# loop through each file in the list
for url in filepaths:
    print(datetime.now().strftime("[%Y-%m-%d %H:%M:%S] -- Beginning processing for"))
    print(os.path.basename(url))

    # Check if file already exists, skip download and crop if it does
    output_path = create_filepath(url)
    if os.path.exists(output_path):
        print(output_path, 'aready found. Progressing to the next url.')
        continue

    # Download the file to a temp folder
    # timeout after 30 seconds and retry after a pause
    # if 3 retries fail then raise an error
    max_retries = 3
    for i in range(max_retries):
        try:
            response = requests.get(url, timeout = 30)
        except Timeout:
            print('Caught a timeout error')
            # sleep 10 seconds
            time.sleep(10)
        # If the request succeeds then leave the loop
        break
    else:
        raise TimeoutError('MAX_RETRIES attempted. All timed out.')

    # Raise an error if the there is a bad http response
    response.raise_for_status()

    output_path_tmp = os.path.join('./scratch', os.path.basename(url))
    open(output_path_tmp, "wb").write(response.content)

    # Open and subset the file
    ds = xr.open_dataset(output_path_tmp)

    ds_chesapeake = ds.sel(lat=slice(36.75, 40), lon=slice(-77.5, -75.5))

    # Save the subset
    ds_chesapeake.to_netcdf(output_path)

    # Remove the file from the temp folder
    os.remove(output_path_tmp)

# After downloading all of the files roll them up to create a single netcdf
# Note: doing this manually instead of invoking open_mfdataset() to avoid using dask
# on the backend, which has in the past resulted in conflicts.
all_files = []
for filepath in sorted(glob.glob(OUTPUT_DIR + '*_CB.nc')):
    print(filepath)
    all_files.append(xr.open_dataset(filepath))

full_year = xr.concat(all_files, dim='time')

# Create the new filename and save the merged file
concat_output_filename = f'L4_GHRSST-SSTfnd-Geo_Polar_Blended_Night-GLOB-v02.0-fv01.0_CB_{start_date}_{end_date}.nc'
output_filename = os.path.join(REPO_ROOT, 'data/raw', concat_output_filename)
full_year.to_netcdf(output_filename)
