# moments
Moments is an application that, upon pressing Ctrl + PrtSc, screenshots your current active window and uploads that image to Google Drive. 

# Usage
Without a `client_secret.json` file and the proper authorizations from Google, the program cannot work. This program was not intended to be for open-use. Nevertheless, refer to https://codelabs.developers.google.com/codelabs/gsuite-apis-intro/#0 to learn more about how to setup applications to work with Google Drive and other Google Suite applications.

From the command line, type:

```python moments.py```

The program runs in the background and can be closed from the system tray by right clicking -> Exit.

# Future Improvements
- Sorting to, and creation of, folders that match the application screenshot. (e.g. `Google Chrome 2021-08-11-12-24-55.png`  get saved to the `Google Chrome` folder. If that folder doesn't exist, create it and save it.)
- Option to keep or delete local copies of screenshots after they're saved to Drive
- Executable instead of command line program
- Icon
- Modification of the system tray notification to stay longer and properly notify of failure via red 'x' instead of the same green checkmark.

# Miscellaneous / About
Moments was developed as a workaround to Window's built-in screenshotting tool, since it (to my current knowledge) does not support screenshotting the current active window *and* **automatically** saving it with a general naming convention. 

Even if Window's built-in tool does support this functionality, it does not support apt naming of files. Moments uses a fairly generic naming convention to make organizing screenshots easier, e.g. 

`Google Chrome 2021-08-11-12-24-55.png`. 

This proves to be more useful in a context where the user utilizes screenshotting multiple different applications and wishes to create a collection or just wants to be organized. A naming convention such as this also enables scripts for sorting, managing, etc. based off of what the application the image is of. 

# License
Moments is intentionally un-licensed.