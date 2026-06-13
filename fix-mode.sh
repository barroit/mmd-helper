#!/bin/sh
# SPDX-License-Identifier: GPL-3.0-or-later

find $1 -type d -exec chmod 755 {} +
find $1 -type f -exec chmod 644 {} +
