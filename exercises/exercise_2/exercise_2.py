'''m = 1500
dc = 0.31 #drag coefficient
rrc = 0.015 #rolling resistance coefficient
v = 80/3.6 #in [km/h]
cs = 1.97 #cross-section [m]
p = 100000 #[pa]'''

#F = (3/2 * dc * cs * v**3 + m * 9.81 * v * rrc)/1000

vehicle1 = {
    m: 1500,
    "dc": 0.31, #drag coefficient
    "rrc": 0.015, #rolling resistance coefficient
    "v": 80/3.6, #in [km/h]
    "cs": 1.97, #cross-section [m]
    "p": 100000 #[pa]
}


v1_m = vehicle1["m"]
v1_dc = vehicle1["dc"]
v1_rrc = vehicle1["rrc"]
v1_v = vehicle1["v"]
v1_cs = vehicle1["cs"]
v1_p = vehicle1["p"]


vehicle2 = [
    "m": 1300,
    "dc":0.41, #drag coefficient
    "rrc": 0.018, #rolling resistance coefficient
    "v": 85/3.6, #in [km/h]
    "cs": 1.61, #cross-section [m]
    "p":100000 #[pa]
]

v2_m = vehicle2["m"]
v2_dc = vehicle2["dc"]
v2_rrc = vehicle2["rrc"]
v2_v = vehicle2["v"]
v2_cs = vehicle2["cs"]
v2_p = vehicle2["p"]

F1 = (3/2 * v1_dc * v1_cs * v1_v**3 + v1_m * 9.81 * v1_v * v1_rrc)/1000

print(F1, end="")
print("[kW]")