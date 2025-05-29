
#ifndef OBSTACLE_DETECTOR_OBSTACLE_TRANSFORMER_H
#define OBSTACLE_DETECTOR_OBSTACLE_TRANSFORMER_H

#include <rclcpp/rclcpp.hpp>
#include <tf2_ros/transform_listener.h>
#include <tf2_ros/buffer.h>
#include <tf2_geometry_msgs/tf2_geometry_msgs.hpp>
#include "obstacle_detector/msg/obstacles.hpp"

namespace obstacle_detector {

class ObstacleTransformer {
public:
    ObstacleTransformer(std::shared_ptr<rclcpp::Node> nh, std::shared_ptr<rclcpp::Node> nh_local);
    ~ObstacleTransformer();

    void initialize() { updateParamsUtil(); }

private:
    void updateParamsUtil();
    void updateParams(const std::shared_ptr<rmw_request_id_t> request_header,
                     const std::shared_ptr<std_srvs::srv::Empty::Request> &req, 
                     const std::shared_ptr<std_srvs::srv::Empty::Response> &res);
    
    void obstaclesCallback(const obstacle_detector::msg::Obstacles::ConstSharedPtr& msg);
    
    std::shared_ptr<rclcpp::Node> nh_;
    std::shared_ptr<rclcpp::Node> nh_local_;
    
    // Parameters
    bool p_active_;
    std::string p_target_frame_;
    std::string p_source_frame_;
    double p_timeout_duration_;
    
    std::unique_ptr<tf2_ros::Buffer> tf_buffer_;
    std::shared_ptr<tf2_ros::TransformListener> tf_listener_;
    
    rclcpp::Subscription<obstacle_detector::msg::Obstacles>::SharedPtr obstacles_sub_;
    rclcpp::Publisher<obstacle_detector::msg::Obstacles>::SharedPtr obstacles_pub_;
};

} // namespace obstacle_detector

#endif // OBSTACLE_DETECTOR_OBSTACLE_TRANSFORMER_H