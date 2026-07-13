import math
import matplotlib.pyplot as plt

# --- CONFIGURATION ---
MODE = "STABLE" # "STABLE" or "CHAOTIC"

G = 6.674e-11
dt = 3600 
if MODE == "STABLE":
    # Sun - Earth - Moon
    m1, x1, y1, vx1, vy1 = 1.989e30, 0, 0, 0, 0
    m2, x2, y2, vx2, vy2 = 5.972e24, 1.496e11, 0, 0, 29780
    m3, x3, y3, vx3, vy3 = 7.348e22, 1.496e11 + 3.844e8, 0, 0, 29780 + 1022
    steps, title = 24 * 365, "Stable (Procedural)"
else:
    # 3 Stars (High speed to fly off)
    m = 1.989e30
    m1, x1, y1, vx1, vy1 = m, 1e11, 0, 0, 30000
    m2, x2, y2, vx2, vy2 = m, -1e11, 0, 0, -30000
    m3, x3, y3, vx3, vy3 = m, 0, 1e11, -30000, 0
    steps, title = 24 * 365, "Chaotic (Procedural - Fly Off)"

hist1_x, hist1_y = [], []
hist2_x, hist2_y = [], []
hist3_x, hist3_y = [], []

# --- SIMULATION LOOP ---
for _ in range(steps):
    # 1. Forces on Body 1
    d12 = math.sqrt((x2-x1)**2 + (y2-y1)**2)
    f12 = G * m1 * m2 / d12**2
    d13 = math.sqrt((x3-x1)**2 + (y3-y1)**2)
    f13 = G * m1 * m3 / d13**2
    fx1 = f12*(x2-x1)/d12 + f13*(x3-x1)/d13
    fy1 = f12*(y2-y1)/d12 + f13*(y3-y1)/d13

    # 2. Forces on Body 2
    d21 = d12
    f21 = G * m2 * m1 / d21**2
    d23 = math.sqrt((x3-x2)**2 + (y3-y2)**2)
    f23 = G * m2 * m3 / d23**2
    fx2 = f21*(x1-x2)/d21 + f23*(x3-x2)/d23
    fy2 = f21*(y1-y2)/d21 + f23*(y3-y2)/d23

    # 3. Forces on Body 3
    d31 = d13; d32 = d23
    f31 = G * m3 * m1 / d31**2
    f32 = G * m3 * m2 / d32**2
    fx3 = f31*(x1-x3)/d31 + f32*(x2-x3)/d32
    fy3 = f31*(y1-y3)/d31 + f32*(y2-y3)/d32

    # Update state
    vx1 += (fx1/m1)*dt; vy1 += (fy1/m1)*dt
    vx2 += (fx2/m2)*dt; vy2 += (fy2/m2)*dt
    vx3 += (fx3/m3)*dt; vy3 += (fy3/m3)*dt
    x1 += vx1*dt; y1 += vy1*dt
    x2 += vx2*dt; y2 += vy2*dt
    x3 += vx3*dt; y3 += vy3*dt
    
    hist1_x.append(x1); hist1_y.append(y1)
    hist2_x.append(x2); hist2_y.append(y2)
    hist3_x.append(x3); hist3_y.append(y3)

# --- PLOTTING ---
plt.figure(figsize=(8, 8)); plt.style.use('dark_background')
plt.plot(hist1_x, hist1_y, 'r', label="Body 1")
plt.plot(hist2_x, hist2_y, 'g', label="Body 2")
plt.plot(hist3_x, hist3_y, 'b', label="Body 3")
plt.title(title); plt.axis("equal"); plt.legend(); plt.show()
