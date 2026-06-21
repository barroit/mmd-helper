#!/bin/sh
# SPDX-License-Identifier: GPL-3.0-or-later

set -s

id=org.blender.Blender

flatpak override --user --reset $id
flatpak override --user --filesystem=$PWD/blender:ro $id
flatpak override --user --filesystem=xdg-run/discord-ipc-0 $id

./blender/ln-scripts.sh $(flatpak run --command=sh $id \
				      -c 'printf %s/blender $XDG_CONFIG_HOME')
