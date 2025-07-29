import folium, json
from folium import Element, MacroElement
from folium.raster_layers import ImageOverlay
from folium.utilities import image_to_url
from jinja2 import Template
from PIL import Image


img_path = "RPA - Queen's College Infrastructure_page-0001.jpg"
im = Image.open(img_path)

m = folium.Map(
    location=[0, 0],
    crs="Simple",  # << key: no lat/lon projection, just a plane
    zoom_start=0,
    min_zoom=0,  # allow zooming way out/in if you like
    max_zoom=100,
    tiles=None,  # no default tiles
)
img_url = image_to_url(img_path)  # auto-base64 the file into a data:URL
ImageOverlay(
    image=img_url,
    bounds=[[0, 0], [900, 1273]],
    opacity=1,
    interactive=True,
    cross_origin=False,
    zindex=1,
).add_to(m)

m.fit_bounds([[0, 0], [900, 1273]])

marker_data = [
    {
        "loc": [122, 180],
        "tooltip": "Fisher Y boiler room",
        "poly": [],
    },
    {
        "loc": [326, 70],
        "tooltip": "Squash courts",
        "poly": [],
    },
    {
        "loc": [172, 274],
        "tooltip": "Cripps kitchen",
        "poly": [],
    },
    {
        "loc": [180, 523],
        "tooltip": "Porters' lodge",
        "poly": [],
    },
    {
        "loc": [458, 300],
        "tooltip": "Gardeners building",
        "poly": [],
    },
    {
        "loc": [481, 620],
        "tooltip": "President's lodge",
        "poly": [],
    },
    {
        "loc": [648, 719],
        "tooltip": "Chapel",
        "poly": [],
    },
    {
        "loc": [644, 841],
        "tooltip": "H staircase",
        "poly": [],
    },
    {
        "loc": [558, 855],
        "tooltip": "G staircase",
        "poly": [],
    },
    {
        "loc": [494, 876],
        "tooltip": "E & F staircase",
        "poly": [],
    },
    {
        "loc": [439, 863],
        "tooltip": "A & B staircase",
        "poly": [],
    },
    {
        "loc": [359, 780],
        "tooltip": "C staircase",
        "poly": [],
    },
    {
        "loc": [356, 726],
        "tooltip": "Old kitchens",
        "poly": [],
    },
    {
        "loc": [517, 756],
        "tooltip": "Old dugout",
        "poly": [],
    },
    {
        "loc": [693, 634],
        "tooltip": "Erasmus",
        "poly": [],
    },
    {
        "loc": [839, 802],
        "tooltip": "Dokett",
        "poly": [],
    },
]

marker_vars = []
polygon_coords = []
for item in marker_data:
    mkr = folium.Marker(item["loc"], tooltip=item["tooltip"]).add_to(m)
    marker_vars.append(mkr.get_name())
    polygon_coords.append(item["poly"])

style = {"color": "blue", "weight": 3, "fillColor": "cyan", "fillOpacity": 0.4}
map_var = m.get_name()

script = f"""
<script>
window.addEventListener('load', function() {{
  var map = {map_var};
  var markerVars = {json.dumps(marker_vars)};
  var polyCoords = {json.dumps(polygon_coords)};
  var style = {json.dumps(style)};
  var polygons = [];

  // 1) Create all polygons (but don’t add them yet)
  for (var i = 0; i < polyCoords.length; i++) {{
    var p = L.polygon(polyCoords[i], style);
    polygons.push(p);
  }}

  // 2) Wire up events for each marker↔polygon pair
  markerVars.forEach(function(mName, i) {{
    var marker = window[mName];        // Folium exposes each layer var on window
    var polygon = polygons[i];

    marker.on('mouseover', function() {{
      polygon.addTo(map);
    }});
    marker.on('mouseout', function() {{
      map.removeLayer(polygon);
    }});
    marker.on('click', function() {{
      // Customize per‐marker click URL if you want:
    'https://queens-energy.github.io/Plant-room-map/image' + i + '.jpg';
    }});
  }});
}});
</script>
"""

# 5) Attach your script
m.get_root().html.add_child(Element(script))

# 6) Save and open
m.save("index.html")
print("Open index.html in your browser.")
