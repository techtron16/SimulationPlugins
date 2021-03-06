//+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
// Author: Jim Jing
// Description: This is the world plugin that used by simulation
//              controller. It basically inherit all the functions from
//              world plugin template. However there are several main
//              differences.
//+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#ifndef _GAZEBO_SIMULATION_CONTROLLER_HH_
#define _GAZEBO_SIMULATION_CONTROLLER_HH_

#include "WorldServer.hh"
#include "sim_control_message.pb.h"

#define SMORES_LIBRARY_PATH_FILE "SMORES_LIBRARY_PATH_FILE"

typedef const boost::shared_ptr
    <const sim_control_message::msgs::SimControlMessage> SimControlMessagePtr;

namespace gazebo{
class SimulationController: public WorldServer
{
 public:
  SimulationController();
  ~SimulationController();
  /// The function that perform extra initialization
  /// In the base class, configuration wil be built in this function
  /// Which means we need to diable it here
  virtual void ExtraInitializationInLoad(physics::WorldPtr _parent,
      sdf::ElementPtr _sdf);
  virtual void OnSystemRunningExtra(const common::UpdateInfo & _info);
  /// Need to be set to empty so the world plugin will not read in gaits
  void ExtraWorkWhenModelInserted(CommandMessagePtr &msg);
 private:
  /// Insert a set of modules if they are not inserted already,
  /// Otherwise reset them to initial position
  void ResetAllModulesPos(void);
  /// Call back when receiving simulation control message
  void SimControlMessageDecoding(SimControlMessagePtr &msg);
  /// Load SMORES_LIBRARY_PATH_FILE
  void ReadLibraryPathFile(const char* filename);
  /// Recursively find the location of a file on a given directory
  bool FindFile( const boost::filesystem::path& directory, boost::filesystem::path& path, const std::string& filename );
  /// Record the position of the existing configuration
  void UpdatePose(void);
 private:
  transport::SubscriberPtr simControlSub;
  transport::PublisherPtr simControlPub;
  bool need_to_load;
  string current_configuration_file;
  bool need_to_execute;
  string current_gait_file;
  common::Timer delete_time;
  string smores_library_path;
  math::Vector3 configuration_pose;
};
} // namespace gazebo

/// A class for comparing the name of two files
class FileEquals: public std::unary_function<boost::filesystem::path, bool>
{
 public:
    explicit FileEquals( const boost::filesystem::path& fname ) : file_name(fname) {}
    bool operator()( const boost::filesystem::directory_entry& entry ) const
    {
      return entry.path().filename() == file_name;
    }
 private:
  boost::filesystem::path file_name;
};
#endif
