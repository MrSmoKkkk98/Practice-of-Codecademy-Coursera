weight = 41.8

# Ground Shipping
if weight <= 2:
    cost_ground = weight * 1.5 + 20
elif weight >= 2 and weight <= 6:
    cost_ground = weight * 3 + 20
elif weight >= 6 and weight <= 10:
    cost_ground = weight * 4 + 20
elif weight > 10:
    cost_ground = weight * 4.75 + 20

print("Ground Shipping cost:", cost_ground, "$")

# Ground Premium
cost_ground_premium = 125

print("Ground Premium Shipping cost:", cost_ground_premium, "$")

# Drone Shipping
if weight <= 2:
    cost_drone = weight * 4.5
elif weight >= 2 and weight <= 6:
    cost_drone = weight * 9
elif weight >= 6 and weight <= 10:
    cost_drone = weight * 12
elif weight > 10:
    cost_drone = weight * 14.25

print("Drone Shipping cost:", cost_drone, "$")
