
"use strict";

let SetActuatorState = require('./SetActuatorState.js')
let GetKinematicsPose = require('./GetKinematicsPose.js')
let SetJointPosition = require('./SetJointPosition.js')
let SetKinematicsPose = require('./SetKinematicsPose.js')
let SetDrawingTrajectory = require('./SetDrawingTrajectory.js')
let GetJointPosition = require('./GetJointPosition.js')

module.exports = {
  SetActuatorState: SetActuatorState,
  GetKinematicsPose: GetKinematicsPose,
  SetJointPosition: SetJointPosition,
  SetKinematicsPose: SetKinematicsPose,
  SetDrawingTrajectory: SetDrawingTrajectory,
  GetJointPosition: GetJointPosition,
};
