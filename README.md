# [CNC Sinumerik 840D language support][home]
[![The MIT License](https://img.shields.io/badge/license-MIT-orange.svg?style=flat-square)](http://opensource.org/licenses/MIT)
[![Package Control](https://packagecontrol.herokuapp.com/downloads/CNC SINUMERIK 840D language support.svg?style=flat-square)](https://packagecontrol.io/packages/CNC SINUMERIK 840D language support)

This package provides syntax highlighting support for the
SINUMERIK 840D Computerized Numerical Control to the [SublimeText 3 Editor][1].

## Screenshot:
![gcode](example.jpg)

## Features:

### NC cycles
* file extensions: MPF, SPF, DEF, TEA
* syntax highlighting
  - ISO G-Code
  - SINUMERIK highlevel commands
  - known NC cycles, functions and commands
  - known NC variables and machine data (NC-Version 04.07.02.01)
  - Highlight illegal usage of control keywords.
* indention rules
* code-snippets for most common control functions
* commands to ``Minify``, ``Beautify``, ``Add/Update block numbers``
* Goto Definition
  - Show labels in local symbol list
  - Show PROC names in indexed symbol list
* Context sensitive auto completions for:
  - variable attributes in definitions (access rights, unit)
  - ISO parameters (e.g.: SPOS= , FP=, ...)
  - ISO commands (e.g.: TRANS, ROT, ...)
  - functions (e.g.: COUPDEF(...))
* tooltip support
  - *.mdat *.svar files from CreateMyConfig

### EasyScreen / RunMyHmi
* file extensions: COM
* syntax highlighting
* indention rules
* code-snippets for
  - classes: ``ARRAY``, ``BLOCK``, ``DIALOG``, ``MENU``
  - methods: ``LOAD``, ``UNLOAD``, ``PRESS``, ...
  - functions: ``RNP``, ``WNP``, ``CP``, ``DP``, ``EP``, ...
* Goto Definition for classes.

### NC archives (text)
* file extensions: ARC
* embedds NC cycles and RunMyHmi syntax highlighting

## Installing

### Using [Package Control][2]

For all Sublime Text 3 users install via [Package Control][2] is recommended.
1. [Install][3] Package Control if you haven't yet.
2. Use <kbd>ctrl+shift+P</kbd> then `Package Control: Install Package`
3. Look for `CNC SINUMERIK 840D language support` and install it.


### Using Git

Clone the repository in your Sublime Text Packages directory, located somewhere in user's "Home" directory:

    git clone git://github.com/deathaxe/sublime-s840d.git "CNC Sinumerik 840D language support"


### Manual Install
Download the latest source from GitHub [https://github.com/deathaxe/sublime-s840d][zip] and extract the whole content into the _"Packages/CNC Sinumerik 840D language support"_ directory.


### Setup

If ``s840d_arc.sublime-settings``, ``s840d_gcode.sublime-settings`` or ``s840d_hmi.sublime-settings`` don't exist in the user folder they will be automatically created to ensure the following essential syntax specific settings:

- "ensure_newline_at_eof_on_save": true
- "translate_tabs_to_spaces": true
- "use_tab_stops": false

They are all required to ensure NC will read the resulting file correctly.
You can override these settings by creating your own syntax specific setting ``Preferences->Settings - Syntax Specific``

## License
The code is available at [GitHub][home] under [MIT licence][lic].

[home]: <https://github.com/deathaxe/sublime-s840d>
[zip]:  <https://github.com/deathaxe/sublime-s840d/archive/master.zip>
[lic]:  <https://github.com/deathaxe/sublime-s840d/blob/master/LICENSE>
[1]:    <http://www.sublimetext.com>
[2]:    <https://packagecontrol.io>
[3]:    <https://packagecontrol.io/installation>