#!/bin/sh
# SPDX-License-Identifier: GPL-3.0-or-later

set -s

trap 'rm -f .tmp-$$' EXIT

id=org.blender.Blender

flatpak override --user --reset $id
flatpak override --user --filesystem=$PWD/blender:ro $id
flatpak override --user --filesystem=xdg-run/discord-ipc-0 $id
flatpak run $id --version >.tmp-$$

./blender/ln-scripts.sh $(flatpak run --command=sh $id \
				      -c 'printf %s/blender $XDG_CONFIG_HOME')
