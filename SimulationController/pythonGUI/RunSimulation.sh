echo "$(pwd)/SmoresLibrary" > ~/.gazebo/models/SMORES8Jack/SMORES_LIBRARY_PATH_FILE
cd ~/.gazebo/models/SMORES8Jack/
gzserver World_sim.sdf
