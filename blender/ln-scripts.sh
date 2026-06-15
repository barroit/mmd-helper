#!/bin/sh
# SPDX-License-Identifier: GPL-3.0-or-later

set -e

for blender in "$1"/*; do
	prefix=$blender/scripts/startup

	mkdir -p "$prefix"

	for script in blender/*.py; do
		ln -sf $PWD/$script "$prefix"
	done
done
