#!/bin/sh
# SPDX-License-Identifier: GPL-3.0-or-later

for d in .assets/*; do
	if [ ! -s $d/.url ]; then
		printf 'missing .url in %s\n' $d
	fi
done
