;; Auto-generated. Do not edit!


(when (boundp 'darknet_ros_msgs::BoundingBox)
  (if (not (find-package "DARKNET_ROS_MSGS"))
    (make-package "DARKNET_ROS_MSGS"))
  (shadow 'BoundingBox (find-package "DARKNET_ROS_MSGS")))
(unless (find-package "DARKNET_ROS_MSGS::BOUNDINGBOX")
  (make-package "DARKNET_ROS_MSGS::BOUNDINGBOX"))

(in-package "ROS")
;;//! \htmlinclude BoundingBox.msg.html


(defclass darknet_ros_msgs::BoundingBox
  :super ros::object
  :slots (_Class _probability _xmin _ymin _xmax _ymax _X _Y _Z _Invalid ))

(defmethod darknet_ros_msgs::BoundingBox
  (:init
   (&key
    ((:Class __Class) "")
    ((:probability __probability) 0.0)
    ((:xmin __xmin) 0)
    ((:ymin __ymin) 0)
    ((:xmax __xmax) 0)
    ((:ymax __ymax) 0)
    ((:X __X) 0.0)
    ((:Y __Y) 0.0)
    ((:Z __Z) 0.0)
    ((:Invalid __Invalid) nil)
    )
   (send-super :init)
   (setq _Class (string __Class))
   (setq _probability (float __probability))
   (setq _xmin (round __xmin))
   (setq _ymin (round __ymin))
   (setq _xmax (round __xmax))
   (setq _ymax (round __ymax))
   (setq _X (float __X))
   (setq _Y (float __Y))
   (setq _Z (float __Z))
   (setq _Invalid __Invalid)
   self)
  (:Class
   (&optional __Class)
   (if __Class (setq _Class __Class)) _Class)
  (:probability
   (&optional __probability)
   (if __probability (setq _probability __probability)) _probability)
  (:xmin
   (&optional __xmin)
   (if __xmin (setq _xmin __xmin)) _xmin)
  (:ymin
   (&optional __ymin)
   (if __ymin (setq _ymin __ymin)) _ymin)
  (:xmax
   (&optional __xmax)
   (if __xmax (setq _xmax __xmax)) _xmax)
  (:ymax
   (&optional __ymax)
   (if __ymax (setq _ymax __ymax)) _ymax)
  (:X
   (&optional __X)
   (if __X (setq _X __X)) _X)
  (:Y
   (&optional __Y)
   (if __Y (setq _Y __Y)) _Y)
  (:Z
   (&optional __Z)
   (if __Z (setq _Z __Z)) _Z)
  (:Invalid
   (&optional __Invalid)
   (if __Invalid (setq _Invalid __Invalid)) _Invalid)
  (:serialization-length
   ()
   (+
    ;; string _Class
    4 (length _Class)
    ;; float64 _probability
    8
    ;; int64 _xmin
    8
    ;; int64 _ymin
    8
    ;; int64 _xmax
    8
    ;; int64 _ymax
    8
    ;; float32 _X
    4
    ;; float32 _Y
    4
    ;; float32 _Z
    4
    ;; bool _Invalid
    1
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _Class
       (write-long (length _Class) s) (princ _Class s)
     ;; float64 _probability
       (sys::poke _probability (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; int64 _xmin
#+(or :alpha :irix6 :x86_64)
       (progn (sys::poke _xmin (send s :buffer) (send s :count) :long) (incf (stream-count s) 8))
#-(or :alpha :irix6 :x86_64)
       (cond ((and (class _xmin) (= (length (_xmin . bv)) 2)) ;; bignum
              (write-long (ash (elt (_xmin . bv) 0) 0) s)
              (write-long (ash (elt (_xmin . bv) 1) -1) s))
             ((and (class _xmin) (= (length (_xmin . bv)) 1)) ;; big1
              (write-long (elt (_xmin . bv) 0) s)
              (write-long (if (>= _xmin 0) 0 #xffffffff) s))
             (t                                         ;; integer
              (write-long _xmin s)(write-long (if (>= _xmin 0) 0 #xffffffff) s)))
     ;; int64 _ymin
#+(or :alpha :irix6 :x86_64)
       (progn (sys::poke _ymin (send s :buffer) (send s :count) :long) (incf (stream-count s) 8))
#-(or :alpha :irix6 :x86_64)
       (cond ((and (class _ymin) (= (length (_ymin . bv)) 2)) ;; bignum
              (write-long (ash (elt (_ymin . bv) 0) 0) s)
              (write-long (ash (elt (_ymin . bv) 1) -1) s))
             ((and (class _ymin) (= (length (_ymin . bv)) 1)) ;; big1
              (write-long (elt (_ymin . bv) 0) s)
              (write-long (if (>= _ymin 0) 0 #xffffffff) s))
             (t                                         ;; integer
              (write-long _ymin s)(write-long (if (>= _ymin 0) 0 #xffffffff) s)))
     ;; int64 _xmax
#+(or :alpha :irix6 :x86_64)
       (progn (sys::poke _xmax (send s :buffer) (send s :count) :long) (incf (stream-count s) 8))
#-(or :alpha :irix6 :x86_64)
       (cond ((and (class _xmax) (= (length (_xmax . bv)) 2)) ;; bignum
              (write-long (ash (elt (_xmax . bv) 0) 0) s)
              (write-long (ash (elt (_xmax . bv) 1) -1) s))
             ((and (class _xmax) (= (length (_xmax . bv)) 1)) ;; big1
              (write-long (elt (_xmax . bv) 0) s)
              (write-long (if (>= _xmax 0) 0 #xffffffff) s))
             (t                                         ;; integer
              (write-long _xmax s)(write-long (if (>= _xmax 0) 0 #xffffffff) s)))
     ;; int64 _ymax
#+(or :alpha :irix6 :x86_64)
       (progn (sys::poke _ymax (send s :buffer) (send s :count) :long) (incf (stream-count s) 8))
#-(or :alpha :irix6 :x86_64)
       (cond ((and (class _ymax) (= (length (_ymax . bv)) 2)) ;; bignum
              (write-long (ash (elt (_ymax . bv) 0) 0) s)
              (write-long (ash (elt (_ymax . bv) 1) -1) s))
             ((and (class _ymax) (= (length (_ymax . bv)) 1)) ;; big1
              (write-long (elt (_ymax . bv) 0) s)
              (write-long (if (>= _ymax 0) 0 #xffffffff) s))
             (t                                         ;; integer
              (write-long _ymax s)(write-long (if (>= _ymax 0) 0 #xffffffff) s)))
     ;; float32 _X
       (sys::poke _X (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _Y
       (sys::poke _Y (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _Z
       (sys::poke _Z (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; bool _Invalid
       (if _Invalid (write-byte -1 s) (write-byte 0 s))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _Class
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _Class (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; float64 _probability
     (setq _probability (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; int64 _xmin
#+(or :alpha :irix6 :x86_64)
      (setf _xmin (prog1 (sys::peek buf ptr- :long) (incf ptr- 8)))
#-(or :alpha :irix6 :x86_64)
      (setf _xmin (let ((b0 (prog1 (sys::peek buf ptr- :integer) (incf ptr- 4)))
                  (b1 (prog1 (sys::peek buf ptr- :integer) (incf ptr- 4))))
              (cond ((= b1 -1) b0)
                     ((and (= b1  0)
                           (<= lisp::most-negative-fixnum b0 lisp::most-positive-fixnum))
                      b0)
                    ((= b1  0) (make-instance bignum :size 1 :bv (integer-vector b0)))
                    (t (make-instance bignum :size 2 :bv (integer-vector b0 (ash b1 1)))))))
   ;; int64 _ymin
#+(or :alpha :irix6 :x86_64)
      (setf _ymin (prog1 (sys::peek buf ptr- :long) (incf ptr- 8)))
#-(or :alpha :irix6 :x86_64)
      (setf _ymin (let ((b0 (prog1 (sys::peek buf ptr- :integer) (incf ptr- 4)))
                  (b1 (prog1 (sys::peek buf ptr- :integer) (incf ptr- 4))))
              (cond ((= b1 -1) b0)
                     ((and (= b1  0)
                           (<= lisp::most-negative-fixnum b0 lisp::most-positive-fixnum))
                      b0)
                    ((= b1  0) (make-instance bignum :size 1 :bv (integer-vector b0)))
                    (t (make-instance bignum :size 2 :bv (integer-vector b0 (ash b1 1)))))))
   ;; int64 _xmax
#+(or :alpha :irix6 :x86_64)
      (setf _xmax (prog1 (sys::peek buf ptr- :long) (incf ptr- 8)))
#-(or :alpha :irix6 :x86_64)
      (setf _xmax (let ((b0 (prog1 (sys::peek buf ptr- :integer) (incf ptr- 4)))
                  (b1 (prog1 (sys::peek buf ptr- :integer) (incf ptr- 4))))
              (cond ((= b1 -1) b0)
                     ((and (= b1  0)
                           (<= lisp::most-negative-fixnum b0 lisp::most-positive-fixnum))
                      b0)
                    ((= b1  0) (make-instance bignum :size 1 :bv (integer-vector b0)))
                    (t (make-instance bignum :size 2 :bv (integer-vector b0 (ash b1 1)))))))
   ;; int64 _ymax
#+(or :alpha :irix6 :x86_64)
      (setf _ymax (prog1 (sys::peek buf ptr- :long) (incf ptr- 8)))
#-(or :alpha :irix6 :x86_64)
      (setf _ymax (let ((b0 (prog1 (sys::peek buf ptr- :integer) (incf ptr- 4)))
                  (b1 (prog1 (sys::peek buf ptr- :integer) (incf ptr- 4))))
              (cond ((= b1 -1) b0)
                     ((and (= b1  0)
                           (<= lisp::most-negative-fixnum b0 lisp::most-positive-fixnum))
                      b0)
                    ((= b1  0) (make-instance bignum :size 1 :bv (integer-vector b0)))
                    (t (make-instance bignum :size 2 :bv (integer-vector b0 (ash b1 1)))))))
   ;; float32 _X
     (setq _X (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _Y
     (setq _Y (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _Z
     (setq _Z (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; bool _Invalid
     (setq _Invalid (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;;
   self)
  )

(setf (get darknet_ros_msgs::BoundingBox :md5sum-) "b7c471f7e43701288329c5fdd129b1f2")
(setf (get darknet_ros_msgs::BoundingBox :datatype-) "darknet_ros_msgs/BoundingBox")
(setf (get darknet_ros_msgs::BoundingBox :definition-)
      "string Class
float64 probability
int64 xmin
int64 ymin
int64 xmax
int64 ymax
float32 X
float32 Y
float32 Z
bool Invalid

")



(provide :darknet_ros_msgs/BoundingBox "b7c471f7e43701288329c5fdd129b1f2")


