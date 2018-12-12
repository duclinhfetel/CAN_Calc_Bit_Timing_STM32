import numpy as np

prescale = np.arange(1,1025)  # 1 -> 1024
seg1 = np.arange(1,17)        # 1 -> 16
seg2 = np.arange(1,9)         # 1 -> 8

clock = 36     # Mhz clock input module CAN (APB1 peripheral)
bitrate = 500  # kbps

ratio = (clock*10**6)/(bitrate*1000)

print()
print ("bit_rate: ", bitrate, "kbps")
print()
for i in range(int(ratio)):
    if (ratio)%prescale[i] == 0:
        for j in seg1:
            out2 = ((ratio)/prescale[i] - 1) - j
            if out2 > 0 and out2 <= max(seg2) and (j/(j+out2) >= 0.8):
                print ("prescale: ", prescale[i], "segment_1: ", j , "segment_2: ", out2, "sample_point: ", j/(j+out2))