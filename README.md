# dotfiles - *Configuration files at their finest.*

[Website](https://dotfilez.netlify.app/) - (Better for everything beneath.)

My config files.
This includes all my configuration files for my [**nix*](https://en.wikipedia.org/wiki/Unix-like) systems and a little website to go with it.

Most of this stuff should work on both [GNU](https://www.gnu.org)/[Linux](https://www.kernel.org/), [OpenBSD](https://www.openbsd.org/) and [FreeBSD](https://www.freebsd.org/) although not everything has been thouroughly tested.

## Configuration Files
### Desktops
* [i3](https://i3wm.org) - simple and easily configured tiling window manager
* [CWM](https://man.openbsd.org/cwm.1) - a nice and lightweight floating window manager
* [Qtile](http://www.qtile.org) - feature-rich tiling window manager written and configured in python
* [Pijulius's Picom](https://github.com/pijulius/picom) - composite manager I used to use
* [Hyprland](https://hyprland.org/) - wlroots compositor and window manager package with smooth animations and easy configuration

### Other
* [Firefox](https://www.mozilla.org/en-US/firefox/products/) - My browser
* [GTK 2.0](https://www.gtk.org/) - GTK 2 configuration
* [GTK 3.0](https://www.gtk.org/) - GTK 3/4 configuration
* [Dunst](https://dunst-project.org) - Notification Daemon
* [xorg-xinit](https://www.x.org/archive/X11R6.8.1/doc/xinit.1.html) - manages autostart and environment variables
* [Wallpapers](https://github.com/yuckdevchan/dotfiles/tree/main/wallpapers) - My wallpapers that I've made in GIMP mostly
* [ZSH](https://www.zsh.org) - My shell, zshrc included, shell configuration
* [Thunar](https://docs.xfce.org/xfce/thunar/start) - thunar (GTK file manager) custom stuff
* [Kitty](https://github.com/kovidgoyal/kitty) - Kitty terminal configuration
* [Alacritty](https://github.com/alacritty/alacritty) - Alacritty terminal configuration

### My own scripts

* [Time HUD](https://github.com/yuckdevchan/dotfiles/blob/main/scripts/time_hud.py) - Time & Date notification script made by me in python
* [Helpful MPlayer FIFO script](https://github.com/yuckdevchan/dotfiles/blob/main/scripts/mplayer-fifo.sh)
* [Pattery](https://github.com/yuckdevchan/pattery) - Python battery tray icon made by me
* [Picom launch script](https://github.com/yuckdevchan/dotfiles/blob/main/scripts/picom.sh)
* [Ralculator](https://github.com/yuckdevchan/ralculator) - Ruby calculator
* [Palculator](https://github.com/yuckdevchan/palculator) - Python calculator
* [termbar-linux](https://github.com/yuckdevchan/termbar-linux) - Fork of [termbar](github.com/gonzalo-/termbar) ported to Linux from OpenBSD

### My own desktop files

* [nitrofix](https://github.com/yuckdevchan/dotfiles/blob/main/usr/share/applications/nitrofix.desktop) - Nitrogen Restoration desktop file (requires nitrogen to be installed + have a wallpaper set)
* [kickoff](https://github.com/yuckdevchan/dotfiles/blob/main/usr/share/applications/kickoff.desktop) - Desktop file for my startup script

## How to guide:

### Get a hold of the files

To clone: ```git clone https://github.com/yuckdevchan/dotfiles```

If you can't use [git](https://git-scm.com/) then click on the ***[Download ZIP](https://github.com/yuckdevchan/dotfiles/archive/refs/heads/main.zip)*** button on this repository, but think about [downloading git, with your package manager](https://git-scm.com/download/linux) or [building it from source](https://mirrors.edge.kernel.org/pub/software/scm/git/) because it is a very valuable tool.

### Apply these to your system

#### Prerequisites

***Make sure if you're using a GUI file manager, switch on hidden files visibility. If you're using a terminal then when listing files then use ```ls -a``` or [```lsd```](https://github.com/Peltoche/lsd) ```-a```.***

#### Application

Drag and drop, or ***CTRL+C*** and ***CTRL+V*** or ```mv``` and ```cp``` all of the configurations you want on your system. For example, config files and folders in the ***.config*** folder, drag the ones you want to your ***.config*** file. Do the same with /usr, and any files that are just in the main folder that you downloaded from here, just put the ones you want in your home directory.
