import matplotlib.pyplot as plt
from PIL import Image, ImageDraw

# Load the Earth map image
earth_image_path = "./textures/00_earthmap1k.jpg"
earth_image = Image.open(earth_image_path)

# Define pollution data (fake data for demo purposes)
# Format: [(city_name, longitude, latitude, pollution_level)]
pollution_data = [
    ("City1", -74.006, 40.7128, 90),  # New York, highly polluted
    ("City2", 2.3522, 48.8566, 60),   # Paris, medium pollution
    ("City3", 139.6917, 35.6895, 30), # Tokyo, less polluted
    ("City4", 77.1025, 28.7041, 80),  # Delhi, highly polluted
    ("City5", -43.1729, -22.9068, 50),# Rio de Janeiro, medium pollution
]

# Define dimensions for the image (must match your image size)
img_width, img_height = earth_image.size

# Function to convert geographic coordinates to pixel positions
def lat_lon_to_pixels(lat, lon, width, height):
    # The provided map is equirectangular projection
    x = (lon + 180) * (width / 360)
    y = (90 - lat) * (height / 180)
    return int(x), int(y)

# Draw on the image
draw = ImageDraw.Draw(earth_image)

# Define thresholds for pollution levels
high_pollution = 75
medium_pollution = 50

# Iterate over each city and plot it on the map
for city, lon, lat, pollution_level in pollution_data:
    # Convert lat/lon to pixel coordinates
    x, y = lat_lon_to_pixels(lat, lon, img_width, img_height)
    
    # Determine the color based on pollution level
    if pollution_level >= high_pollution:
        color = (255, 0, 0)  # Red for high pollution
    elif pollution_level >= medium_pollution:
        color = (255, 165, 0)  # Orange for medium pollution
    else:
        color = (0, 0, 255)  # Blue for low pollution

    # Draw a small circle for the city on the map
    radius = 5
    draw.ellipse((x-radius, y-radius, x+radius, y+radius), fill=color)

# Save the new image
output_image_path = "./textures/earth_with_pollution.png"
earth_image.save(output_image_path)

# Show the new image
earth_image.show()
