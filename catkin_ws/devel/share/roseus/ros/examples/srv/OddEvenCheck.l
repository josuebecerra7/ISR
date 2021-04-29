;; Auto-generated. Do not edit!


(when (boundp 'examples::OddEvenCheck)
  (if (not (find-package "EXAMPLES"))
    (make-package "EXAMPLES"))
  (shadow 'OddEvenCheck (find-package "EXAMPLES")))
(unless (find-package "EXAMPLES::ODDEVENCHECK")
  (make-package "EXAMPLES::ODDEVENCHECK"))
(unless (find-package "EXAMPLES::ODDEVENCHECKREQUEST")
  (make-package "EXAMPLES::ODDEVENCHECKREQUEST"))
(unless (find-package "EXAMPLES::ODDEVENCHECKRESPONSE")
  (make-package "EXAMPLES::ODDEVENCHECKRESPONSE"))

(in-package "ROS")





(defclass examples::OddEvenCheckRequest
  :super ros::object
  :slots (_number ))

(defmethod examples::OddEvenCheckRequest
  (:init
   (&key
    ((:number __number) 0)
    )
   (send-super :init)
   (setq _number (round __number))
   self)
  (:number
   (&optional __number)
   (if __number (setq _number __number)) _number)
  (:serialization-length
   ()
   (+
    ;; int32 _number
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; int32 _number
       (write-long _number s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; int32 _number
     (setq _number (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;;
   self)
  )

(defclass examples::OddEvenCheckResponse
  :super ros::object
  :slots (_answer ))

(defmethod examples::OddEvenCheckResponse
  (:init
   (&key
    ((:answer __answer) "")
    )
   (send-super :init)
   (setq _answer (string __answer))
   self)
  (:answer
   (&optional __answer)
   (if __answer (setq _answer __answer)) _answer)
  (:serialization-length
   ()
   (+
    ;; string _answer
    4 (length _answer)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _answer
       (write-long (length _answer) s) (princ _answer s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _answer
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _answer (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;;
   self)
  )

(defclass examples::OddEvenCheck
  :super ros::object
  :slots ())

(setf (get examples::OddEvenCheck :md5sum-) "4ff0b0ab1ed04611e3a2b4090af9ee4f")
(setf (get examples::OddEvenCheck :datatype-) "examples/OddEvenCheck")
(setf (get examples::OddEvenCheck :request) examples::OddEvenCheckRequest)
(setf (get examples::OddEvenCheck :response) examples::OddEvenCheckResponse)

(defmethod examples::OddEvenCheckRequest
  (:response () (instance examples::OddEvenCheckResponse :init)))

(setf (get examples::OddEvenCheckRequest :md5sum-) "4ff0b0ab1ed04611e3a2b4090af9ee4f")
(setf (get examples::OddEvenCheckRequest :datatype-) "examples/OddEvenCheckRequest")
(setf (get examples::OddEvenCheckRequest :definition-)
      "int32 number
---
string answer
 
")

(setf (get examples::OddEvenCheckResponse :md5sum-) "4ff0b0ab1ed04611e3a2b4090af9ee4f")
(setf (get examples::OddEvenCheckResponse :datatype-) "examples/OddEvenCheckResponse")
(setf (get examples::OddEvenCheckResponse :definition-)
      "int32 number
---
string answer
 
")



(provide :examples/OddEvenCheck "4ff0b0ab1ed04611e3a2b4090af9ee4f")


