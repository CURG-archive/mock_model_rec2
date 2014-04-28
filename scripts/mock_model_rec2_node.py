#!/usr/bin/env python

import geometry_msgs.msg
import model_rec2.srv
import rospy
import sensor_msgs.msg

class fake_model_rec_node():

    def __init__(self):
        rospy.init_node("fake_model_rec2")
        self.model_rec_service = rospy.Service("recognize_objects", model_rec2.srv.FindObjects, self.handle_recognize_objects)

    def handle_recognize_objects(self, req):
        #response:
        # string[] object_name
        # geometry_msgs/Pose[] object_pose
        # string reason
        # sensor_msgs/PointCloud2[] pointcloud

        response = model_rec2.srv.FindObjectsResponse()

        response.object_name = ["garnier_shampoo_bottle"]
        garnier_shampoo_bottle_pose = geometry_msgs.msg.Pose()
        garnier_shampoo_bottle_pose.position.x = 0.066363998
        garnier_shampoo_bottle_pose.position.y = -0.089734
        garnier_shampoo_bottle_pose.position.z = 1.033533

        garnier_shampoo_bottle_pose.orientation.x = 0.69429055280717
        garnier_shampoo_bottle_pose.orientation.y = -.5179138189319789
        garnier_shampoo_bottle_pose.orientation.z = 0.20627250068909891
        garnier_shampoo_bottle_pose.orientation.w = 0.45516761736911104

        response.object_pose = [garnier_shampoo_bottle_pose]
        response.pointcloud = [sensor_msgs.msg.PointCloud2()]

        response.reason = "no reason"
        return response

if __name__ == "__main__":

    try:
        fake_model_rec_node()

        loop = rospy.Rate(10)
        while not rospy.is_shutdown():
            loop.sleep()
    except rospy.ROSInterruptException:
        pass