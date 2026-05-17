import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.patches as patches

try:
    import imageio_ffmpeg

    plt.rcParams["animation.ffmpeg_path"] = imageio_ffmpeg.get_ffmpeg_exe()
except ImportError:
    pass


# ----------------------------
# General settings
# ----------------------------
fps = 30
duration = 10.0
total_frames = int(fps * duration)

bg_color = "#F4F6F9"
fig, ax = plt.subplots(figsize=(12, 6.75), dpi=150)
fig.patch.set_facecolor(bg_color)
ax.set_facecolor(bg_color)
ax.set_xlim(-8.4, 8.4)
ax.set_ylim(-4.75, 4.75)
ax.axis("off")
plt.subplots_adjust(left=0, right=1, bottom=0, top=1)


# ----------------------------
# Colors
# ----------------------------
colors_Mo = {
    "TL": "#E89076",
    "TR": "#D96C4A",
    "BL": "#BE5535",
    "BR": "#A34326",
}

colors_B = {
    "TL": "#74A7D3",
    "TR": "#4B8BBE",
    "BL": "#3B719E",
    "BR": "#2A557D",
}

c_X = "#20B34A"
c_X_hl = "#87F5A5"
c_A = "#F9E076"
c_A_hl = "#FFF4C2"

c_amine_line = "#6C757D"
c_amine_N = "#118AB2"
c_shared_face = "#85B86B"


# ----------------------------
# Helper functions
# ----------------------------
def ease(p):
    return p * p * (3.0 - 2.0 * p)


def get_progress(t, t_start, t_end):
    return np.clip((t - t_start) / (t_end - t_start), 0.0, 1.0)


def make_octahedron(color_dict, z=4):
    faces = []

    for key in ["TL", "TR", "BL", "BR"]:
        p = patches.Polygon(
            np.zeros((3, 2)),
            closed=True,
            facecolor=color_dict[key],
            edgecolor="white",
            lw=0.35,
            zorder=z,
        )
        ax.add_patch(p)
        faces.append(p)

    halides = []
    for _ in range(4):
        bg = patches.Circle((0, 0), 0.14, facecolor=c_X, edgecolor="none", zorder=z + 1)
        hl = patches.Circle((0, 0), 0.05, facecolor=c_X_hl, edgecolor="none", zorder=z + 2)
        ax.add_patch(bg)
        ax.add_patch(hl)
        halides.append((bg, hl))

    return {"faces": faces, "halides": halides}


def set_octahedron(
    artist,
    cx,
    cy,
    r=0.82,
    alpha=1.0,
    visible_halides=(1, 1, 1, 1),
):
    top = np.array([cx, cy + r])
    bottom = np.array([cx, cy - r])
    left = np.array([cx - r, cy])
    right = np.array([cx + r, cy])
    center = np.array([cx, cy])

    tl = np.array([center, top, left])
    tr = np.array([center, top, right])
    bl = np.array([center, bottom, left])
    br = np.array([center, bottom, right])

    for face, pts in zip(artist["faces"], [tl, tr, bl, br]):
        face.set_xy(pts)
        face.set_alpha(alpha)

    h_positions = [top, bottom, left, right]

    for i, ((bg, hl), pos) in enumerate(zip(artist["halides"], h_positions)):
        bg.center = tuple(pos)
        hl.center = (pos[0] - 0.04, pos[1] + 0.04)

        h_alpha = alpha if visible_halides[i] else 0.0
        bg.set_alpha(h_alpha)
        hl.set_alpha(h_alpha)


def create_amine(kind="long"):
    if kind == "long":
        y_pts = np.linspace(-0.85, 0.85, 7)
        x_pts = np.array([0.00, 0.14, -0.14, 0.14, -0.14, 0.14, 0.00])

        line, = ax.plot([], [], color=c_amine_line, lw=2.4, zorder=2)

        n1 = patches.Circle((0, 0), 0.11, facecolor=c_amine_N, edgecolor="white", lw=0.2, zorder=3)
        n2 = patches.Circle((0, 0), 0.11, facecolor=c_amine_N, edgecolor="white", lw=0.2, zorder=3)

        ax.add_patch(n1)
        ax.add_patch(n2)

        return {
            "line": line,
            "nodes": [n1, n2],
            "x_pts": x_pts,
            "y_pts": y_pts,
            "node_ids": [0, -1],
        }

    y_pts = np.linspace(-0.22, 0.22, 3)
    x_pts = np.array([0.00, 0.10, -0.10])

    line, = ax.plot([], [], color=c_amine_line, lw=2.0, zorder=2)

    n1 = patches.Circle((0, 0), 0.09, facecolor=c_amine_N, edgecolor="white", lw=0.2, zorder=3)
    ax.add_patch(n1)

    return {
        "line": line,
        "nodes": [n1],
        "x_pts": x_pts,
        "y_pts": y_pts,
        "node_ids": [0],
    }


def set_amine(amine, cx, cy, alpha=1.0):
    x_data = amine["x_pts"] + cx
    y_data = amine["y_pts"] + cy

    amine["line"].set_data(x_data, y_data)
    amine["line"].set_alpha(alpha)

    for node, idx in zip(amine["nodes"], amine["node_ids"]):
        node.center = (x_data[idx], y_data[idx])
        node.set_alpha(alpha)


def hide_amine(amine):
    amine["line"].set_alpha(0.0)
    for node in amine["nodes"]:
        node.set_alpha(0.0)


# ----------------------------
# 1D face-sharing chain
# ----------------------------
def make_1d_chain(n_units, z_base=6):
    """Construct a face-sharing halide octahedral chain."""
    planes = []
    for i in range(n_units + 1):
        p_type = "down" if i % 2 == 0 else "up"
        halides = []
        for _ in range(3):
            bg = patches.Circle((0, 0), 0.12, facecolor=c_X, edgecolor="none")
            hl = patches.Circle((0, 0), 0.04, facecolor=c_X_hl, edgecolor="none")
            ax.add_patch(bg)
            ax.add_patch(hl)
            halides.append((bg, hl))

        tri = patches.Polygon(
            np.zeros((3, 2)),
            facecolor=c_shared_face,
            edgecolor="#4F7D38",
            lw=1.0,
            alpha=0.0,
        )
        ax.add_patch(tri)
        planes.append({"halides": halides, "tri": tri, "type": p_type})

    octahedra = []
    for _ in range(n_units):
        body_bg = patches.Polygon(np.zeros((6, 2)), facecolor="#243338", edgecolor="none", alpha=0.0)
        f_mid = patches.Polygon(np.zeros((3, 2)), facecolor="white", edgecolor="white", lw=0.4)
        f_left = patches.Polygon(np.zeros((3, 2)), facecolor="white", edgecolor="white", lw=0.4)
        f_right = patches.Polygon(np.zeros((3, 2)), facecolor="white", edgecolor="white", lw=0.4)

        ax.add_patch(body_bg)
        ax.add_patch(f_mid)
        ax.add_patch(f_left)
        ax.add_patch(f_right)

        octahedra.append(
            {
                "body_bg": body_bg,
                "f_mid": f_mid,
                "f_left": f_left,
                "f_right": f_right,
            }
        )

    return {"planes": planes, "octahedra": octahedra, "z_base": z_base}


def set_1d_chain(chain_dict, cx, cy_start, chain_idx, w=0.65, h=0.48, d=0.28, alpha=1.0):
    planes = chain_dict["planes"]
    octahedra = chain_dict["octahedra"]
    z_base = chain_dict["z_base"]

    for i, plane in enumerate(planes):
        py = cy_start - i * (2 * h)
        plane["y"] = py

        if plane["type"] == "down":
            p0 = np.array([cx - w, py])
            p1 = np.array([cx + w, py])
            p2 = np.array([cx, py - d])
            z0 = z_base
            z1 = z_base
            z2 = z_base + 2.0
        else:
            p0 = np.array([cx - w, py])
            p1 = np.array([cx + w, py])
            p2 = np.array([cx, py + d])
            z0 = z_base + 2.0
            z1 = z_base + 2.0
            z2 = z_base

        plane["pts"] = [p0, p1, p2]
        plane["tri"].set_xy([p0, p1, p2])
        plane["tri"].set_alpha(alpha * 0.75)
        plane["tri"].set_zorder(z_base + 0.4)

        for j, (bg, hl) in enumerate(plane["halides"]):
            pos = plane["pts"][j]
            z_target = [z0, z1, z2][j]

            bg.center = tuple(pos)
            hl.center = (pos[0] - 0.03, pos[1] + 0.03)
            bg.set_alpha(alpha)
            hl.set_alpha(alpha)
            bg.set_zorder(z_target)
            hl.set_zorder(z_target + 0.1)

    for i, oct_dict in enumerate(octahedra):
        p_top = planes[i]
        p_bot = planes[i + 1]
        c_dict = colors_Mo if (i + chain_idx) % 2 == 0 else colors_B

        if p_top["type"] == "down":
            tl, tr, tf = p_top["pts"]
            bfl, bfr, bb = p_bot["pts"]

            bg_pts = [tl, tr, bfr, bb, bfl]
            f_mid_pts = [tf, bfl, bfr]
            f_left_pts = [tl, bfl, tf]
            f_right_pts = [tr, tf, bfr]

            oct_dict["f_mid"].set_facecolor(c_dict["BL"])
            oct_dict["f_left"].set_facecolor(c_dict["TL"])
            oct_dict["f_right"].set_facecolor(c_dict["TR"])
        else:
            tfl, tfr, tb = p_top["pts"]
            bl, br, bf = p_bot["pts"]

            bg_pts = [tb, tfr, br, bf, bl, tfl]
            f_mid_pts = [tfl, tfr, bf]
            f_left_pts = [tfl, bf, bl]
            f_right_pts = [tfr, br, bf]

            oct_dict["f_mid"].set_facecolor(c_dict["TR"])
            oct_dict["f_left"].set_facecolor(c_dict["BL"])
            oct_dict["f_right"].set_facecolor(c_dict["BR"])

        oct_dict["body_bg"].set_xy(bg_pts)
        oct_dict["body_bg"].set_alpha(alpha * 0.8)
        oct_dict["body_bg"].set_zorder(z_base + 0.2)

        oct_dict["f_mid"].set_xy(f_mid_pts)
        oct_dict["f_mid"].set_alpha(alpha)
        oct_dict["f_mid"].set_zorder(z_base + 1.0)

        oct_dict["f_left"].set_xy(f_left_pts)
        oct_dict["f_left"].set_alpha(alpha)
        oct_dict["f_left"].set_zorder(z_base + 1.0)

        oct_dict["f_right"].set_xy(f_right_pts)
        oct_dict["f_right"].set_alpha(alpha)
        oct_dict["f_right"].set_zorder(z_base + 1.0)


# ----------------------------
# 3D / 2D framework
# ----------------------------
grid_w, grid_h = 6, 4
d_grid = 1.55
r_grid = 0.80

grid_elements = []

for row in range(grid_h):
    for col in range(grid_w):
        c_dict = colors_Mo if (row + col) % 2 == 0 else colors_B
        art = make_octahedron(c_dict, z=4)

        x_3d = (col - 2.5) * d_grid
        y_3d = (row - 1.5) * d_grid
        layer_y = [-4.1, -1.35, 1.35, 4.1][row]

        grid_elements.append(
            {
                "artist": art,
                "x_3d": x_3d,
                "y_3d": y_3d,
                "x_2d": x_3d,
                "y_2d": layer_y,
                "row": row,
                "col": col,
            }
        )

a_sites = []

for row in range(grid_h - 1):
    for col in range(grid_w - 1):
        cx = (col - 2.0) * d_grid
        cy = (row - 1.0) * d_grid

        base = patches.Circle((cx, cy), 0.23, facecolor=c_A, edgecolor="none", zorder=3)
        hl = patches.Circle((cx - 0.04, cy + 0.04), 0.09, facecolor=c_A_hl, edgecolor="none", zorder=4)

        ax.add_patch(base)
        ax.add_patch(hl)
        a_sites.append({"base": base, "hl": hl})


# ----------------------------
# Long amines for 3D -> 2D
# ----------------------------
long_amines = []
gap_y_positions = [-2.75, 0.0, 2.75]

x_gap_positions = []
shift_right = 0.18

for c in range(grid_w - 1):
    x_left = (c - 2.5) * d_grid
    x_right = ((c + 1) - 2.5) * d_grid
    x_mid = 0.5 * (x_left + x_right) + shift_right
    x_gap_positions.append(x_mid)

for gy in gap_y_positions:
    for i, gx in enumerate(x_gap_positions):
        am = create_amine("long")
        am["target_x"] = gx
        am["target_y"] = gy
        am["start_y"] = 7.0 if (i % 2 == 0) else -7.0
        long_amines.append(am)


# ----------------------------
# 1D chains and short amines
# ----------------------------
chains_1d = []
chain_xs = [-4.8, -1.6, 1.6, 4.8]

for chain_idx, cx in enumerate(chain_xs):
    chain = make_1d_chain(n_units=5, z_base=6)
    chain["cx"] = cx
    chain["cy_start"] = 2.2
    chain["chain_idx"] = chain_idx
    chains_1d.append(chain)

short_amines = []
gap_x_positions_short = [-3.2, 0.0, 3.2]
short_y_positions = [-2.1, -0.7, 0.7, 2.1]

for gx in gap_x_positions_short:
    for gy in short_y_positions:
        am = create_amine("short")
        am["target_x"] = gx
        am["target_y"] = gy
        am["start_y"] = 7.0 if gy >= 0 else -7.0
        short_amines.append(am)


# ----------------------------
# Smaller scissor
# ----------------------------
sc_blade1, = ax.plot([], [], color="#6E7B86", lw=2.0, zorder=10)
sc_blade2, = ax.plot([], [], color="#6E7B86", lw=2.0, zorder=10)
sc_pivot = patches.Circle((0, 0), 0.08, facecolor="#4F5962", edgecolor="none", zorder=11)
ax.add_patch(sc_pivot)


def update_scissor(progress):
    if progress <= 0 or progress >= 1:
        sc_blade1.set_alpha(0.0)
        sc_blade2.set_alpha(0.0)
        sc_pivot.set_alpha(0.0)
        return

    sx = -8.1 + 2.2 * progress
    sy = 0.0

    snip = np.sin(progress * np.pi * 3.0) * 10.0
    ang = np.radians(18 - snip)

    length = 0.75
    c = np.cos(ang)
    s = np.sin(ang)

    sc_blade1.set_data([sx - length * c, sx + length * c], [sy - length * s, sy + length * s])
    sc_blade2.set_data([sx - length * c, sx + length * c], [sy + length * s, sy - length * s])

    alpha = 0.65 * ease(1 - abs(progress - 0.5) * 2)

    sc_blade1.set_alpha(alpha)
    sc_blade2.set_alpha(alpha)
    sc_pivot.center = (sx, sy)
    sc_pivot.set_alpha(alpha)


# ----------------------------
# Initialize hidden objects
# ----------------------------
for chain in chains_1d:
    set_1d_chain(chain, chain["cx"], chain["cy_start"], chain["chain_idx"], alpha=0.0)

for am in long_amines:
    hide_amine(am)

for am in short_amines:
    hide_amine(am)


# ----------------------------
# Animation update
# ----------------------------
def update(frame):
    t = frame / fps

    p_2d = ease(get_progress(t, 1.3, 4.0))
    p_1d = ease(get_progress(t, 5.8, 8.4))

    update_scissor(get_progress(t, 1.1, 2.0))

    framework_alpha = 1.0 - p_1d

    for el in grid_elements:
        cx = el["x_3d"] * (1 - p_2d) + el["x_2d"] * p_2d
        cy = el["y_3d"] * (1 - p_2d) + el["y_2d"] * p_2d

        if p_2d > 0.02:
            visible_halides = (1, 1, 1 if el["col"] == 0 else 0, 1)
        else:
            visible_halides = (1, 1, 1, 1)

        set_octahedron(
            el["artist"],
            cx,
            cy,
            r=r_grid,
            alpha=framework_alpha,
            visible_halides=visible_halides,
        )

    a_alpha = np.clip(1.0 - 2.5 * p_2d, 0.0, 1.0) * framework_alpha

    for a in a_sites:
        a["base"].set_alpha(a_alpha)
        a["hl"].set_alpha(a_alpha)

    p_long = ease(get_progress(t, 1.6, 4.0))
    long_alpha = p_long * (1.0 - p_1d)

    for am in long_amines:
        curr_y = am["start_y"] * (1 - p_long) + am["target_y"] * p_long
        set_amine(am, am["target_x"], curr_y, alpha=long_alpha if long_alpha > 0.01 else 0.0)

    for chain in chains_1d:
        set_1d_chain(
            chain,
            cx=chain["cx"],
            cy_start=chain["cy_start"],
            chain_idx=chain["chain_idx"],
            w=0.65,
            h=0.48,
            d=0.28,
            alpha=p_1d,
        )

    p_short = ease(get_progress(t, 6.0, 8.4))

    for am in short_amines:
        curr_y = am["start_y"] * (1 - p_short) + am["target_y"] * p_short
        set_amine(am, am["target_x"], curr_y, alpha=p_short if p_short > 0.01 else 0.0)

    return []


ani = animation.FuncAnimation(fig, update, frames=total_frames, blit=False)

ani.save(
    "perovskite_transition.mp4",
    writer=animation.FFMpegWriter(fps=fps, bitrate=3000),
)

ani.save(
    "perovskite_transition.gif",
    writer=animation.PillowWriter(fps=fps),
)

plt.close(fig)

print("Done.")
print("Files created:")
print("1. perovskite_transition.mp4")
print("2. perovskite_transition.gif")
