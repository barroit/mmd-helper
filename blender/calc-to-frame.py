# SPDX-License-Identifier: GPL-3.0-or-later

import bpy

id = 'scene.custom_calc_to_frame'
label = 'Calculate to Frame'

def enable_item(self, context):
	self.layout.operator(id)

class calc_to_frame(bpy.types.Operator):
	bl_idname = id
	bl_label = label

	def execute(self, context):
		scene = context.scene
		cache = scene.rigidbody_world.point_cache
		override = context.temp_override(point_cache = cache)

		override.__enter__()
		bpy.ops.ptcache.bake(bake = False)
		override.__exit__(None, None, None)

		return { 'FINISHED' }

bpy.utils.register_class(calc_to_frame)
bpy.types.DOPESHEET_MT_channel.append(enable_item)
