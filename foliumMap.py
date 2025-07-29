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
        "tooltip": "Fisher Y boiler room<br>Capacity: 960 kW<br>Installed: 2012",
        "poly": [
            [142, 184],
            [137, 202],
            [130, 227],
            [119, 270],
            [134, 288],
            [181, 266],
            [211, 250],
            [232, 253],
            [285, 233],
            [366, 184],
            [489, 386],
            [349, 476],
            [319, 452],
            [269, 473],
            [206, 490],
            [192, 519],
            [126, 490],
            [79, 431],
            [55, 385],
            [49, 340],
            [48, 286],
            [65, 233],
            [87, 166],
            [102, 151],
            [137, 153],
        ],
    },
    {
        "loc": [5000, 70],
        "tooltip": "Squash courts",
        "poly": [],
    },
    {
        "loc": [172, 274],
        "tooltip": "Cripps kitchen<br>Capacity: 200 kW<br>Installed: 1987",
        "poly": [
            [329, 66],
            [359, 114],
            [388, 153],
            [345, 185],
            [278, 217],
            [231, 239],
            [163, 151],
        ],
    },
    {
        "loc": [180, 523],
        "tooltip": "Porters' lodge<br>"
        "Heating capacity: 6 kW<br>"
        "Cooling capacity: 6 kW<br>"
        "Installed: 2022",
        "poly": [
            [207, 494],
            [183, 519],
            [175, 511],
            [164, 525],
            [200, 559],
            [227, 546],
            [237, 519],
        ],
    },
    {
        "loc": [448, 167],
        "tooltip": "Gardeners building<br>Capacity: 26 kW<br>Installed: 2009",
        "poly": [
            [413, 85],
            [463, 163],
            [439, 176],
            [397, 102],
        ],
    },
    {
        "loc": [481, 620],
        "tooltip": "President's lodge<br>Capacity: 130 kW<br>Installed 2020",
        "poly": [
            [385, 579],
            [462, 534],
            [498, 638],
            [519, 661],
            [526, 681],
            [505, 686],
            [490, 678],
            [445, 571],
            [402, 595],
        ],
    },
    {
        "loc": [648, 719],
        "tooltip": "Chapel<br>Capacity: 60 kW<br>Installed: 2012",
        "poly": [
            [673, 695],
            [700, 842],
            [667, 846],
            [629, 706],
        ],
    },
    {
        "loc": [644, 841],
        "tooltip": "H staircase<br>Capacity: 35 kW<br>Installed: 2011",
        "poly": [
            [652, 812],
            [607, 822],
            [617, 857],
            [662, 847],
        ],
    },
    {
        "loc": [558, 855],
        "tooltip": "G staircase<br>Capacity: 35 kW<br>Installed: 2011",
        "poly": [
            [603, 821],
            [610, 855],
            [542, 866],
            [541, 830],
        ],
    },
    {
        "loc": [494, 876],
        "tooltip": "E & F staircase<br>Capacity: 50 kW<br>Installed: 2019",
        "poly": [
            [502, 848],
            [511, 874],
            [465, 887],
            [454, 857],
        ],
    },
    {
        "loc": [439, 863],
        "tooltip": "A & B staircase<br>Capacity: 60 kW<br>Installed: 2018",
        "poly": [
            [439, 863],
            [450, 889],
            [388, 908],
            [371, 830],
            [395, 817],
            [411, 867],
        ],
    },
    {
        "loc": [359, 780],
        "tooltip": "C staircase<br>Capacity: 60 kW<br>Installed: 2018",
        "poly": [
            [382, 763],
            [392, 819],
            [374, 824],
            [354, 769],
        ],
    },
    {
        "loc": [356, 726],
        "tooltip": "Old kitchens<br>Capacity: 150 kW<br>Installed: 1990",
        "poly": [
            [343, 682],
            [361, 699],
            [404, 710],
            [412, 756],
            [350, 769],
            [328, 726],
            [276, 667],
            [378, 589],
            [400, 608],
            [360, 627],
            [371, 655],
        ],
    },
    {
        "loc": [517, 756],
        "tooltip": "Old dugout<br>Capacity: 360 kW<br>Installed: 2015",
        "poly": [
            [413, 710],
            [501, 687],
            [528, 739],
            [536, 789],
            [519, 797],
            [540, 869],
            [514, 875],
            [476, 740],
            [423, 749],
        ],
    },
    {
        "loc": [693, 634],
        "tooltip": "Erasmus<br>Heating capacity: 60 kW<br>Cooling capacity: 39 kW<br>Installed: 2025",
        "poly": [
            [630, 569],
            [663, 644],
            [804, 599],
            [793, 564],
            [679, 598],
            [663, 556],
        ],
    },
    {
        "loc": [839, 802],
        "tooltip": "Dokett<br>Capacity: 960 kW<br>Installed: 2012",
        "poly": [
            [718, 844],
            [715, 800],
            [793, 794],
            [798, 774],
            [748, 609],
            [806, 605],
            [857, 756],
            [863, 828],
        ],
    },
]

marker_vars = []
polygon_coords = []
for item in marker_data:
    tip = folium.Tooltip(
        item["tooltip"],
        parse_html=True,
        style=(
            "max-width:250px;"
            "min-width:150px;"
            "padding:8px;"
            "font-size:12px;"
            "background:rgba(255,255,255,0.9);"
        ),
    )
    mkr = folium.Marker(item["loc"], tooltip=tip).add_to(m)
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
    window.location.href = 'https://queens-energy.github.io/Plant-room-map/image' + i + '.png';
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
