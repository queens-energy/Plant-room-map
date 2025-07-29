import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# 1. Load your image
img_path = "RPA - Queen's College Infrastructure_page-0001.jpg"  # ← replace with your image file path
img = mpimg.imread(img_path)

# 2. Display it and collect clicks
fig, ax = plt.subplots()
ax.imshow(img)
ax.set_title("Click to select vertices. Press Enter when done.")

# Unlimited clicks until Enter
coords = plt.ginput(n=-1, timeout=0)

# 3. Draw lines (and close the shape)
if coords:
    xs, ys = zip(*coords)
    ax.plot(xs + (xs[0],), ys + (ys[0],), "-o")  # connects back to the first point

    # Annotate each point with its index
    for i, (x, y) in enumerate(coords):
        ax.annotate(f"{i}", (x, y), color="red")

    plt.draw()

plt.show()

# 4. Print integer pixel coordinates
print("Vertex coordinates (y, x):")
for i, (x, y) in enumerate(coords):
    print(f"[{900 - int(y/3.9)}, {int(x/3.9)}],")
