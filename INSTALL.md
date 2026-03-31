# Prerequisites

- Install Python 3 on your system
- Install pipx on your system
- Install git on your system

# Why use pipx?

`pipx` installs Python applications in isolated environments, which prevents dependency conflicts with your system or other projects.  
It also allows you to run CLI tools globally without polluting your Python installation.  
This makes it safer and cleaner than using `pip` or `pip3` for installing standalone tools.

# Clean old versions

If you have installed an old version with `pip` or `pip3` (depending on your system), use one of the following commands:

```
pip3 uninstall pytntprog
pip uninstall pytntprog
pip3 uninstall pytntprog --break-system-packages
pip uninstall pytntprog --break-system-packages
```

# Installation

```
pipx install pytntprog
```

# Upgrade

Use one of the following commands: 
```
pipx upgrade pytntprog #to update pytntprog
pipx reinstall pytntprog #to force update dependencies
```

# Uninstall

```
pipx uninstall pytntprog
```
