import maya.cmds as cmds

#SEND THE CODE TO MAYA AND TYPE THE INPUT IN THE INPUT RPOMPT 
# RATHER THAN SETTING IT AS AN ARGUMENT hERE

def setDrawingOverrideColor(colorIndex):
    if not (0 <= colorIndex <= 31):
        cmds.warning("value must be between 0 - 31, try 13 for red and 14 for green :]")
        return

    # get selected
    selectedObjects = cmds.ls(sl=True)
    #empty selectedObjects value check
    if not selectedObjects:
        cmds.warning("select something, preferably NURBs")
        return

    def applyColorToNurbsShapes(objects):
        shapeNodesColored = 0

        for obj in objects:
            # listRelatives returns a string array of all the children of the selected objects
            # !!!! fullPath uses the hierachal path as the name rather than a generic name that coudl be repeated across children.
            #you can filter by the node type by clicking on the node you want to filter and finding
            #the type at the very top of the attribute editor, to the left of the node's name
            shapeNodes = cmds.listRelatives(obj, allDescendents=True, type='nurbsCurve', fullPath=True) or []

            for shape in shapeNodes:
                # loope nable drawing overraide
                cmds.setAttr(shape + ".overrideEnabled", 1)
                cmds.setAttr(shape + ".overrideColor", colorIndex)
                shapeNodesColored += 1
                print(f"Color applied to {shape}")

        return shapeNodesColored

    # color
    shapeNodesColored = applyColorToNurbsShapes(selectedObjects)

    #report how many controls were colored
    if shapeNodesColored == 0:
        cmds.warning("no nurbs found in the selection.")
    else:
        print("color applied to " + str(shapeNodesColored) + " different NURBs.")

# `variable`(input()) makes setting values easy without having to code a whole ui
#SEND THE CODE TO MAYA AND TYPE THE INPUT IN THE INPUT RPOMPT 
# RATHER THAN SETTING IT AS AN ARGUMENT hERE
colorIndex = int(input())
setDrawingOverrideColor(colorIndex)
