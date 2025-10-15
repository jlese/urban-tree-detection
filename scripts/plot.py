import rasterio
import matplotlib.pyplot as plt
import geopandas as gpd

# Load TIFF image
with rasterio.open('naip_image.tif') as src:
    img = src.read([1, 2, 3])  # For RGB bands
    extent = (src.bounds.left, src.bounds.right, src.bounds.bottom, src.bounds.top)

# Load results.json
gdf = gpd.read_file('outputs/results.json')

# Plot
plt.figure(figsize=(10, 10))
plt.imshow(img.transpose(1, 2, 0), extent=extent)
gdf.plot(ax=plt.gca(), marker='o', color='red', markersize=5)
plt.title('Detected Trees')
plt.show()