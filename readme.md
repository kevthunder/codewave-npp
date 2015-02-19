# CodeWave

Codewave for Notepad++ : The text editor helper.

Create abbreviation for you own code snippets and expand them with a push of a button, or use those already provided. Write code faster with this tool designed to give you what you need to be more productive without leaving your favorite text editor.

## Installation

1. Install Python Script for Notepad++ http://npppythonscript.sourceforge.net/
2. Get the code : ```sh
cd "~/AppData/Roaming/Notepad++/plugins/config/PythonScript/scripts/"
git clone https://github.com/kevthunder/codewave-npp.git codewave_npp
```
3. In the menu go to ```Plugin > Python Script > configuration```
  * Open the ```codewave_npp``` folder and select ```codewave_activate.py```
  * Press the add button on the left to add it in the menu items
  * Press ok
4. Restart Notepad++
5. In the menu go to ```Settings > Shortcut Mapper```
  * Select the ```Plugin commands``` tab
  * find ```codewave_activate```
  * Assing the shortcut ```Ctrl+Shift+E``` or something of your choice
  * Your may need to remove any conflicting shortcuts

## Getting started

* In any window press ```Ctrl+Shift+E``` 
* Type ```help``` 
* Press ```Ctrl+Shift+E``` again to show help

```
~~help~~
```

## ToDo

* See the main project https://github.com/kevthunder/codewave