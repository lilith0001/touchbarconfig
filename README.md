# touchbarconfig
<img width="1004" alt="image" src="https://user-images.githubusercontent.com/90871823/133862059-3563767e-ef09-412a-999f-86c478265402.png">

# What does it do?

The icons labelled I-X will move you to desktops 1-10 when you press them. 

Square brackets will indicate the current desktop.

Quotation marks indicate how many windows are in each desktop (NOT FULLY WORKING, SEE LIMITATIONS)
<img width="1004" alt="image" src="https://user-images.githubusercontent.com/90871823/133889836-d8a90df7-b311-4b6e-aaac-61bb3b72a893.png">


When you hold them, they will send your focused window to the specified desktop.

Drag 2 fingers to adjust volume.

Drag 3 fingers to adjust screen brightness.

The screenshot button will open a submenu:
<img width="1004" alt="image" src="https://user-images.githubusercontent.com/90871823/133690771-4546eaf5-ffb6-4537-992a-bb5bd26f1bad.png">

  
Standard multimedia controls.

Forward delete, home, and end keys.

# What are the limitations?

The quotations indicating how many windows exist in a given workspace only track when you are moving existing windows between workspaces.

Basically you can hold the current workspace to remove a quotation and hold a different workspace to add a quotation. Until I can make it better using swift or objc.

Further development is needed to get system updates to script window monitoring upon opening and closing applications.

# How to Set up:

1. Open spotlight and search "Mission Control" and add desktops until you have 10
2. Go to System Preferences > Keyboard > Shortcuts > Mission Control and make it look like this:
<img width="646" alt="image" src="https://user-images.githubusercontent.com/90871823/133690437-90670d3d-e017-4fe1-b44c-5588c9253044.png">

3. Install MTMR https://github.com/toxblh/mtmr
4. Install Amethyst https://github.com/ianyh/Amethyst
5. Clone my repository to ~
6. check if you have python by running the command `python3 -V` If not installed, get it from https://www.python.org/downloads/release/python-397/

7. run the command `python3 ~/touchbarconfig/setup.py`
8. start Amethyst
9. start MTMR

Enjoy :)
