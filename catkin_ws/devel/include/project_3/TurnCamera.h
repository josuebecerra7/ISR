// Generated by gencpp from file project_3/TurnCamera.msg
// DO NOT EDIT!


#ifndef PROJECT_3_MESSAGE_TURNCAMERA_H
#define PROJECT_3_MESSAGE_TURNCAMERA_H

#include <ros/service_traits.h>


#include <project_3/TurnCameraRequest.h>
#include <project_3/TurnCameraResponse.h>


namespace project_3
{

struct TurnCamera
{

typedef TurnCameraRequest Request;
typedef TurnCameraResponse Response;
Request request;
Response response;

typedef Request RequestType;
typedef Response ResponseType;

}; // struct TurnCamera
} // namespace project_3


namespace ros
{
namespace service_traits
{


template<>
struct MD5Sum< ::project_3::TurnCamera > {
  static const char* value()
  {
    return "d2bd6d55eaa6b367037dff843fa7a83c";
  }

  static const char* value(const ::project_3::TurnCamera&) { return value(); }
};

template<>
struct DataType< ::project_3::TurnCamera > {
  static const char* value()
  {
    return "project_3/TurnCamera";
  }

  static const char* value(const ::project_3::TurnCamera&) { return value(); }
};


// service_traits::MD5Sum< ::project_3::TurnCameraRequest> should match
// service_traits::MD5Sum< ::project_3::TurnCamera >
template<>
struct MD5Sum< ::project_3::TurnCameraRequest>
{
  static const char* value()
  {
    return MD5Sum< ::project_3::TurnCamera >::value();
  }
  static const char* value(const ::project_3::TurnCameraRequest&)
  {
    return value();
  }
};

// service_traits::DataType< ::project_3::TurnCameraRequest> should match
// service_traits::DataType< ::project_3::TurnCamera >
template<>
struct DataType< ::project_3::TurnCameraRequest>
{
  static const char* value()
  {
    return DataType< ::project_3::TurnCamera >::value();
  }
  static const char* value(const ::project_3::TurnCameraRequest&)
  {
    return value();
  }
};

// service_traits::MD5Sum< ::project_3::TurnCameraResponse> should match
// service_traits::MD5Sum< ::project_3::TurnCamera >
template<>
struct MD5Sum< ::project_3::TurnCameraResponse>
{
  static const char* value()
  {
    return MD5Sum< ::project_3::TurnCamera >::value();
  }
  static const char* value(const ::project_3::TurnCameraResponse&)
  {
    return value();
  }
};

// service_traits::DataType< ::project_3::TurnCameraResponse> should match
// service_traits::DataType< ::project_3::TurnCamera >
template<>
struct DataType< ::project_3::TurnCameraResponse>
{
  static const char* value()
  {
    return DataType< ::project_3::TurnCamera >::value();
  }
  static const char* value(const ::project_3::TurnCameraResponse&)
  {
    return value();
  }
};

} // namespace service_traits
} // namespace ros

#endif // PROJECT_3_MESSAGE_TURNCAMERA_H
