m = 1500
dc = 0.31 #drag coefficient
rrc = 0.015 #rolling resistance coefficient
v = 80/3.6 #in [km/h]
cs = 1.97 #cross-section [m]
p = 100000 #[pa]

F = (3/2 * dc * cs * v**3 + m * 9.81 * v * rrc)/1000

print(F, end="")
print("[kW]")
