# dotfiles
My config files.
This includes all my configuration files for my **nix* systems and a little website to go with it.

Most of this stuff should work on both GNU/Linux, OpenBSD and FreeBSD although not everything has been thouroughly tested.

## Included:

### Configuration Files

* [CWM](https://man.openbsd.org/cwm.1) - My Window Manager
* [Pijulius's Picom](https://github.com/pijulius/picom) - My Composite Manager
* [GTK 2.0](https://www.gtk.org/) - GTK 2 configuration
* [GTK 3.0](https://www.gtk.org/) - GTK 3/4 configuration
* xorg-xinit - manages autostart and environment variables
* Wallpapers - My wallpapers that I've made in GIMP mostly
* [ZSH](https://www.zsh.org) - My shell, zshrc included, shell configuration
* [Alacritty](https://github.com/alacritty/alacritty) - Alacritty terminal configuration
* [Kitty](https://github.com/kovidgoyal/kitty) - Kitty terminal configuration
* [i3](https://i3wm.org) - i3wm configuration

### My own scripts

* Time & Date notification script made by me in python
* Helpful MPlayer FIFO script
* [Pattery](https://github.com/yuckdevchan/pattery) - Python battery tray icon made by me
* Picom launch script
* [Ralculator](https://github.com/yuckdevchan/ralculator) - Ruby calculator
* [Palculator](https://github.com/yuckdevchan/palculator) - Python calculator

## How to guide:

### Get a hold of the files

To clone: ```git clone https://github.com/yuckdevchan/dotfiles```

If you can't use git then click on the ***Downloads ZIP*** button on this repository.

### Apply these to your system

***Make sure if you're using a GUI file manager, switch on hidden files visibility. If you're using a terminal then when listing files then use ```ls -a``` or ```lsd -a```.***

Drag and drop, or ***CTRL+C*** and ***CTRL+V*** or ```mv``` and ```cp``` all of the configurations you want on your system. For example, config files and folders in the ***.config*** folder, drag the ones you want to your ***.config*** file. Do the same with /usr, and any files that are just in the main folder that you downloaded from here, just put the ones you want in your home directory.
