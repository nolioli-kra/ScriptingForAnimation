import maya.cmds as cmds

def rename(nameFormat):
    # check input for `##`
    if '#' not in nameFormat:
        cmds.warning("The naming format must contain at least one '#' character.")
        return
    
    # denote the separator to be the ## part of the input
    # .partition createws the pre and post based on how oyu denote the sep
    (pre, sep, post) = nameFormat.partition('#' * nameFormat.count('#'))

    # len() just get's the length ofd the variable object
    #in this case it's string with ##'s
    paddingCount = len(sep)

    selectedObjs = cmds.ls(sl=True)
    
    #empty value check
    if not selectedObjs:
        cmds.warning("plz select objects.")
        return

    # loop and rename
    # start at 1 so that the joints are not renamed `00`

    # obj gets the orignal name of the object for renaming access

    # enumerate() returns a string based on the array of selected items
    # it writes the string by taking the name of the object (obj) and
    # adding a number to the end of it based on the iteration (selectedObjNum)
    for selectedObjNum, obj in enumerate(selectedObjs, start=1):
        # pad the enumerated string with 0's based on formatting input
        # zfill automatically putsz 0's in front of the string
        sequentialNumber = str(selectedObjNum).zfill(paddingCount)
        
        # replace the ## part of user input with the padded string
        newName = nameFormat.replace(sep, sequentialNumber)
        
        # rename
        cmds.rename(obj, newName)

# example use
nameFormat = input("!! enter the correct naming format (e.g., 'Leg_##_Jnt'): ")
rename(nameFormat)