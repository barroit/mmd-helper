# SPDX-License-Identifier: GPL-3.0-or-later

import bpy

id = 'scene.custom_calc_to_frame'
label = 'Calculate to Frame'

class calc_to_frame(bpy.types.Operator):
	bl_idname = id
	bl_label = label

	def invoke(self, context, event):
		scene = context.scene
		cache = scene.rigidbody_world.point_cache
		override = context.temp_override(point_cache = cache)

		override.__enter__()
		res = bpy.ops.ptcache.bake('INVOKE_DEFAULT', bake=False)
		override.__exit__(None, None, None)

		return res

class panel(bpy.types.Panel):
	bl_space_type = 'DOPESHEET_EDITOR'
	bl_region_type = 'UI'
	bl_category = 'Action'
	bl_label = 'Rigid Body Cache'

	def draw(self, context):
		self.layout.operator(id)

bpy.utils.register_class(calc_to_frame)
bpy.utils.register_class(panel)
