# SPDX-License-Identifier: GPL-3.0-or-later

import bpy

class SCENE_OT_calc_to_frame(bpy.types.Operator):
	bl_idname = 'scene.custom_calc_to_frame'
	bl_label = 'Calculate to Frame'

	def invoke(self, context, event):
		scene = context.scene
		cache = scene.rigidbody_world.point_cache
		override = context.temp_override(point_cache = cache)

		override.__enter__()
		res = bpy.ops.ptcache.bake('INVOKE_DEFAULT', bake=False)
		override.__exit__(None, None, None)

		return res

class DOPESHEET_PT_rigid_body_cache(bpy.types.Panel):
	bl_space_type = 'DOPESHEET_EDITOR'
	bl_region_type = 'UI'
	bl_category = 'Action'
	bl_label = 'Rigid Body Cache'

	def draw(self, context):
		self.layout.operator(SCENE_OT_calc_to_frame.bl_idname)

def register():
	bpy.utils.register_class(SCENE_OT_calc_to_frame)
	bpy.utils.register_class(DOPESHEET_PT_rigid_body_cache)

def unregister():
	bpy.utils.unregister_class(DOPESHEET_PT_rigid_body_cache)
	bpy.utils.unregister_class(SCENE_OT_calc_to_frame)
