import maya.cmds as cmds
#using re to get access the re.sub() function which replaces recurring strings
import re

#REMEMBER PYTOHON USES INDENTS INSTEAD OF BRACKETS
# previous assignment code tweaked to be loopable so the loop can be done all 
# at once rather than 2 separate times
def autoGroupTool(obj):
    position = cmds.xform(obj, query=True, worldSpace=True, translation=True)
    rotation = cmds.xform(obj, query=True, worldSpace=True, rotation=True)
    
    groupName = obj + "_Grp"
    group = cmds.group(empty=True, name=groupName)
    
    #move and rot grp to match joints
    cmds.xform(group, worldSpace=True, translation=position)
    cmds.xform(group, worldSpace=True, rotation=rotation)
    
    cmds.parent(obj, group)
    
    return groupName


def singleJointCreate(joint):
    #get name and remove suffixx
    base_name = re.sub(r'(_Jnt | _Geo)$', '', joint)
    
    #make NURBS
    control_name = base_name + "_Ctrl"
    control = cmds.circle(name=control_name, normal=[1, 0, 0])[0]
    
    position = cmds.xform(joint, query=True, worldSpace=True, translation=True)
    rotation = cmds.xform(joint, query=True, worldSpace=True, rotation=True)
    
    #move + rot nurbs
    cmds.xform(control, worldSpace=True, translation=position)
    cmds.xform(control, worldSpace=True, rotation=rotation)
    #name retrieved from group tool
    groupName = autoGroupTool(control)
    
    #patrent the grp to the joint itself
    cmds.parent(groupName, joint)

def allJointsCreate():
    selectedObjs = cmds.ls(selection=True, type='joint')
    
    #`if not` checks for empty value
    if not selectedObjs:
        cmds.warning("nothing selected, pls select some joints")
        return
    #loop simplified into one executiion :]
    for joint in selectedObjs:
        singleJointCreate(joint)

    cmds.select(clear=True)
    print("controls created")

#some reason the center cog is rotated in a way that makes the nurb generate so
#this is a rudimentary fix for this assignments requirement
def fixCOGRot():
    cmds.setAttr("COG_Jnt_Ctrl.rotateZ", 90)

#execution
allJointsCreate()
fixCOGRot()