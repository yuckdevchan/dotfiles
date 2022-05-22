#!/bin/sh

# Use './mplayer-fifo.sh' then type any mplayer slave option like:
#   pause
# Look at the man page for mplayer for more info

echo "$@" > ~/.mplayer/fifo
