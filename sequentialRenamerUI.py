# !!! HOW TO USE !!!
# run command `renamerUI.create()` in the pYTHON input field in maya
# AFTER script has been placed in the `documents/maya/scripts` folder along with the userSetup.py included in the ZIP.

import maya.cmds as cmds

class SequentialRenamerUI:
    def __init__(self):
        self.window = "sequentialRenamerUI"
        self.title = "Sequential Renamer"
        self.size = (300, 100)
        self.nameFormat = ""

    def create(self):
        # delete old window
        if cmds.window(self.window, exists=True):
            cmds.deleteUI(self.window, window=True)
        
        self.window = cmds.window(self.window, title=self.title, widthHeight=self.size)
        cmds.columnLayout(adjustableColumn=True)
        cmds.text(label="Type the desired naming convention. Type `#` where you want numbers.", height = 50)
        self.nameFormatField = cmds.textFieldGrp(label="Name Format:", text="")
        cmds.button(label="Rename", command=self.renameObjects)
        
        cmds.showWindow(self.window)

    def renameObjects(self, *args):
        # get string
        self.nameFormat = cmds.textFieldGrp(self.nameFormatField, query=True, text=True)
        #use string
        self.rename(self.nameFormat)

    def rename(self, nameFormat):
        # check for correct format (#)
        if '#' not in nameFormat:
            cmds.warning("The naming format should contain at least one '#' where you want numbers")
            return

        # define the partition of the string with #
        pre, sep, post = nameFormat.partition('#' * nameFormat.count('#'))

        # get the length of the # sep
        paddingCount = len(sep)

        # get selected
        selectedObjs = cmds.ls(sl=True)

        # empty value check
        if not selectedObjs:
            cmds.warning("Plz select grouped objects to rename")
            return

        # loop and rename
        for selectedObjNum, obj in enumerate(selectedObjs, start=1):
            # create heiarchy number with padding
            sequentialNumber = str(selectedObjNum).zfill(paddingCount)
            newName = nameFormat.replace(sep, sequentialNumber)
            
            # rename
            cmds.rename(obj, newName)
            print("Renamed selected objects")

# create ui then show it
#ui = SequentialRenamerUI()
#ui.create()
