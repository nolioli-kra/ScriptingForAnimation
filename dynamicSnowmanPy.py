import maya.cmds as cmds

scale = 3
#base
cmds.polySphere(r = scale, sx=20, sy=20, ax=[0,1,0], cuv=2, ch=1)
cmds.move(0, scale, 0)
#mid
cmds.polySphere(r = (scale * 0.7), sx=20, sy=20, ax=[0,1,0], cuv=2, ch=1)
cmds.move(0, ((scale * 0.7) + (scale *1.85)), 0)
#head
topSphereRef = cmds.polySphere(r = (scale * 0.4), sx=20, sy=20, ax=[0,1,0], cuv=2, ch=1)
topSphereY = ((scale * 0.4) + ((scale * 0.7) * 1.85) + (scale * 1.85))
cmds.move(0, topSphereY, 0)
#head position
topPos = cmds.xform(topSphereRef[0], q=True, ws=True, t=True)
#hat brim
cmds.polyCylinder(r=(scale * 0.45), h=(scale * 0.05), sx=20, sy=1, sz=1, ax=[0,1,0], cuv=3, ch=1)
cmds.move(topPos[0], topPos[1] + (scale * 0.3), topPos[2], a=True)
#hat top
cmds.polyCylinder(r=(scale * 0.3), h=(scale * 0.5), sx=20, sy=1, sz=1, ax=(0, 1, 0), cuv=3, ch=1)
cmds.move(topPos[0], topPos[1] + (scale * 0.55), topPos[2], a=True)
#carrot
cmds.polyCone(r=(scale/scale), h=(scale * 2), sx=20, sy=1, sz=0, ax=[0,1,0], rcp=0, cuv=3, ch=1)
cmds.move(topPos[0], topPos[1], (topPos[2] + (scale * 0.5)))
cmds.rotate(90, 0, 0, os=True, fo=True)
cmds.scale(scale * 0.1, scale * 0.1, scale * 0.1, r=True)
#eyes
#left
cmds.polySphere(r=(scale * 0.06), sx=20, sy=20, ax=[0,1,0], cuv=2, ch=1)
cmds.move((topPos[0] + (scale * 0.2)), (topPos[1] + (scale * 0.1)), (topPos[2] + (scale * 0.35)))
#right
cmds.polySphere(r=(scale * 0.06), sx=20, sy=20, ax=[0,1,0], cuv=2, ch=1)
cmds.move((topPos[0] - (scale * 0.2)), (topPos[1] + (scale * 0.1)), (topPos[2] + (scale * 0.35)))
