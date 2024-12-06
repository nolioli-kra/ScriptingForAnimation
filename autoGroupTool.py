import maya.cmds as cmds

def create_control_groups():
    selected_objects = cmds.ls(selection=True)
    
    if not selected_objects:
        cmds.warning("No objects selected. Please select the controls to group.")
        return

    #loop thru selected objs
    for obj in selected_objects:
        position = cmds.xform(obj, query=True, worldSpace=True, translation=True)
        rotation = cmds.xform(obj, query=True, worldSpace=True, rotation=True)
        
        group_name = obj + "_Grp"
        group = cmds.group(empty=True, name=group_name)
        #move + rot grp
        cmds.xform(group, worldSpace=True, translation=position)
        cmds.xform(group, worldSpace=True, rotation=rotation)
        #parent to grp
        cmds.parent(obj, group)
        #zero transform
        cmds.makeIdentity(obj, apply=True, translate=True, rotate=True, scale=True, normal=False)

    cmds.select(clear=True)
    print("Groups created and controls parented successfully.")

create_control_groups()
