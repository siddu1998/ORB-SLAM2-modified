# ORB-SLAM2-modified

Replace system.cc from original ORB-SLAM2 with the one provided in the link below. This allows you to store the pcd file. To use pcl_viwer Follow the below instructions:

```
sudo add-apt-repository ppa:v-launchpad-jochen-sprickerhof-de/pcl
sudo apt-get update
sudo apt-get install libpcl-all

```
Once the orb_slam2 has finished iterating through all the images, run 

```pcl_viewer pointcloud.pcd```

