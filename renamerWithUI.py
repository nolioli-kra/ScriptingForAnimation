import maya.cmds as cmds

class SequentialRenamerUI:
    def __init__(self):
        self.window = "sequentialRenamerUI"
        self.title = "Sequential Renamer"
        self.size = (300, 100)
        self.nameFormat = ""

    def create(self):
        # Check if the window exists
        if cmds.window(self.window, exists=True):
            cmds.deleteUI(self.window, window=True)
        
        # Create the window
        self.window = cmds.window(self.window, title=self.title, widthHeight=self.size)
        
        # Create the layout
        cmds.columnLayout(adjustableColumn=True)
        
        # Text field
        self.nameFormatField = cmds.textFieldGrp(label="Name Format:", text="")
        
        # Button to rename
        cmds.button(label="Rename", command=self.rename_objects)
        
        # Show the window
        cmds.showWindow(self.window)

    def rename_objects(self, *args):
        # Get the value from the text field
        self.nameFormat = cmds.textFieldGrp(self.nameFormatField, query=True, text=True)
        
        # Call the rename function from the script
        self.rename(self.nameFormat)

    def rename(self, nameFormat):
        # Ensure the format contains at least one '#'
        if '#' not in nameFormat:
            cmds.warning("The naming format must contain at least one '#' character.")
            return

        # Partition the format into pre, sep, and post
        pre, sep, post = nameFormat.partition('#' * nameFormat.count('#'))

        # Get the number of '#' characters for padding
        paddingCount = len(sep)

        # Get the current selection
        selectedObjs = cmds.ls(sl=True)

        # Empty selection check
        if not selectedObjs:
            cmds.warning("Please select objects.")
            return

        # Iterate through the selected objects and rename them
        for selectedObjNum, obj in enumerate(selectedObjs, start=1):
            # Create the sequential number with the required padding
            sequentialNumber = str(selectedObjNum).zfill(paddingCount)
            
            # Replace the '#' characters with the sequential number
            newName = nameFormat.replace(sep, sequentialNumber)
            
            # Rename the object
            cmds.rename(obj, newName)
            print(f"Renamed {obj} to {newName}")

# Create an instance of the UI and show it
ui = SequentialRenamerUI()
ui.create()
