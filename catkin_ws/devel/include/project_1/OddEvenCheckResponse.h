// Generated by gencpp from file project_1/OddEvenCheckResponse.msg
// DO NOT EDIT!


#ifndef PROJECT_1_MESSAGE_ODDEVENCHECKRESPONSE_H
#define PROJECT_1_MESSAGE_ODDEVENCHECKRESPONSE_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace project_1
{
template <class ContainerAllocator>
struct OddEvenCheckResponse_
{
  typedef OddEvenCheckResponse_<ContainerAllocator> Type;

  OddEvenCheckResponse_()
    : answer()  {
    }
  OddEvenCheckResponse_(const ContainerAllocator& _alloc)
    : answer(_alloc)  {
  (void)_alloc;
    }



   typedef std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other >  _answer_type;
  _answer_type answer;





  typedef boost::shared_ptr< ::project_1::OddEvenCheckResponse_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::project_1::OddEvenCheckResponse_<ContainerAllocator> const> ConstPtr;

}; // struct OddEvenCheckResponse_

typedef ::project_1::OddEvenCheckResponse_<std::allocator<void> > OddEvenCheckResponse;

typedef boost::shared_ptr< ::project_1::OddEvenCheckResponse > OddEvenCheckResponsePtr;
typedef boost::shared_ptr< ::project_1::OddEvenCheckResponse const> OddEvenCheckResponseConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::project_1::OddEvenCheckResponse_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::project_1::OddEvenCheckResponse_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::project_1::OddEvenCheckResponse_<ContainerAllocator1> & lhs, const ::project_1::OddEvenCheckResponse_<ContainerAllocator2> & rhs)
{
  return lhs.answer == rhs.answer;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::project_1::OddEvenCheckResponse_<ContainerAllocator1> & lhs, const ::project_1::OddEvenCheckResponse_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace project_1

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsMessage< ::project_1::OddEvenCheckResponse_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::project_1::OddEvenCheckResponse_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::project_1::OddEvenCheckResponse_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::project_1::OddEvenCheckResponse_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::project_1::OddEvenCheckResponse_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::project_1::OddEvenCheckResponse_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::project_1::OddEvenCheckResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "d7e708f879c94bb931716d8f4f130f30";
  }

  static const char* value(const ::project_1::OddEvenCheckResponse_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xd7e708f879c94bb9ULL;
  static const uint64_t static_value2 = 0x31716d8f4f130f30ULL;
};

template<class ContainerAllocator>
struct DataType< ::project_1::OddEvenCheckResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "project_1/OddEvenCheckResponse";
  }

  static const char* value(const ::project_1::OddEvenCheckResponse_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::project_1::OddEvenCheckResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "string answer\n"
" \n"
;
  }

  static const char* value(const ::project_1::OddEvenCheckResponse_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::project_1::OddEvenCheckResponse_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.answer);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct OddEvenCheckResponse_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::project_1::OddEvenCheckResponse_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::project_1::OddEvenCheckResponse_<ContainerAllocator>& v)
  {
    s << indent << "answer: ";
    Printer<std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > >::stream(s, indent + "  ", v.answer);
  }
};

} // namespace message_operations
} // namespace ros

#endif // PROJECT_1_MESSAGE_ODDEVENCHECKRESPONSE_H
