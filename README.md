# CAN_Calc_Bit_Timing_STM32
- Code generate prescale, segment1, segment2 for config CAN in STM32. 
- You just only change value at variable clock and bitrate on this file.
- Formula : 
  - prescaler*(Seg1 + Seg2 + 1) = Clock/bitrate
  - sample_point = Seg1/(Seg1+Seg2)
