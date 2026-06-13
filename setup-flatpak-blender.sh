#!/bin/sh
# SPDX-License-Identifier: GPL-3.0-or-later

set -s

trap 'rm -f .tmp-$$' EXIT

id=org.blender.Blender

flatpak override --user --reset $id
flatpak override --user --filesystem=$PWD/blender:ro $id
flatpak run $id --version >.tmp-$$

config=$(flatpak run --command=sh $id -c 'printf %s $XDG_CONFIG_HOME')

for blender in $config/blender/*; do
	prefix=$blender/scripts/startup

	mkdir -p $prefix

	for script in blender/*; do
		ln -sf $PWD/$script $prefix
	done
done
