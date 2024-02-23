# find user directory
user_directory=$(python3 -m site --user-site)

# find root directory
root_directory=$(sudo python3 -m site --user-site)

# create if it doesn't exist
sudo mkdir -p ${root_directory}

# create new .pth file with our path
echo ${user_directory} | sudo tee ${root_directory}/local_lib.pth
