import xarray as xr
from datetime import datetime

start = datetime.now()
print('staring process', start.strftime("%H:%M:%S"))
# Access NOAA Geopolar SST
filepath = 'https://ncsa.osn.xsede.org/Pangeo/pangeo-forge/noaa-coastwatch-geopolar-sst-feedstock/noaa-coastwatch-geopolar-sst.zarr'
geopolar = xr.open_zarr(filepath)
geopolar = geopolar.analysed_sst

min_lat, max_lat, min_lon, max_lon = (36.75, 40, -77.5, -75.5)
geopolar = geopolar.sel(lat=slice(min_lat, max_lat), lon=slice(min_lon, max_lon))

geopolar.to_dataset().to_netcdf('./data/raw/geopolar_sst_chesapeakebay.nc')

end = datetime.now()
print('ending process', end.strftime("%H:%M:%S"))
print('total time', end - start, '(HH:MM:SS.microseconds)')
