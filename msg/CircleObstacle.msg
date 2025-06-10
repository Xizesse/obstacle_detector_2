uint64 uid                      # Unique identifier
geometry_msgs/Point center      # Central point [m]
geometry_msgs/Vector3 velocity  # Linear velocity [m/s]
float64 radius                  # Radius with added margin [m]
float64 true_radius             # True measured radius [m]
float64 radius_std              # Radius uncertainty (standard deviation) [m]
float64 position_x_std          # Position uncertainty in x-direction [m]
float64 position_y_std          # Position uncertainty in y-direction [m]
float64 position_z_std          # Position uncertainty in z-direction [m]
string semclass                  # Semantic class
float64 confidence              # Confidence in semantic class
