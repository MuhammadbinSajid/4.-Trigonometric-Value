import math

def calculate_trig_values(angle_degrees):
    # Convert angle from degrees to radians
    angle_radians = math.radians(angle_degrees)
    
    # Calculate sin, cos, and tan
    sin_value = math.sin(angle_radians)
    cos_value = math.cos(angle_radians)
    tan_value = math.tan(angle_radians)

    return sin_value, cos_value, tan_value

# Input angle from the user
angle = float(input("Enter the angle in degrees: "))

# Get the trigonometric values
sin_value, cos_value, tan_value = calculate_trig_values(angle)

# Display the results
print(f"For angle {angle} degrees:")
print(f"sin: {sin_value}")
print(f"cos: {cos_value}")
print(f"tan: {tan_value}")
