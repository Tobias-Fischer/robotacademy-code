import roboticstoolbox as rtb
import spatialmath as sm
import numpy as np

# 1:05
p560 = rtb.models.DH.Puma560()

TA = sm.SE3.Trans(0.4, 0.2, 0) * sm.SE3.Rx(np.pi)
print(TA, "\n")

TB = sm.SE3.Trans(0.4, -0.2, 0) * sm.SE3.Rx(np.pi/2)
print(TB, "\n")

qA = p560.ikine_a(TA)
print(qA, "\n")

qB = p560.ikine_a(TB)
print(qB, "\n")

tg = rtb.jtraj(qA, qB, 50)

p560.plot(tg)

rtb.qplot(tg)

# 1:28
Ts = rtb.ctraj(TA, TB, 50)

# 1:55
print(Ts[0], "\n")

# 2:02
print(Ts[1], "\n")

# 2:05
print(Ts[2], "\n")

# 2:27
qs = p560.ikine_a(Ts)

# 2:51
p560.plot(qs)

# 3:04
rtb.qplot(qs)