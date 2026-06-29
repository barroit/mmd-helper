# SPDX-License-Identifier: GPL-3.0-or-later

import bpy

def apply_rotation(frame, bone, arm, act):
	if bone.rotation_mode == 'QUATERNION':
		prop = 'rotation_quaternion'
		vals = ( 1.0, 0.0, 0.0, 0.0 )
	elif bone.rotation_mode == 'AXIS_ANGLE':
		prop = 'rotation_axis_angle'
		vals = ( 0.0, 0.0, 1.0, 0.0 )
	else:
		prop = 'rotation_euler'
		vals = ( 0.0, 0.0, 0.0 )

	path = bone.path_from_id(prop)

	for idx, val in enumerate(vals):
		fc = act.fcurve_ensure_for_datablock(arm, path,
						     index = idx,
						     group_name = bone.name)
		key = None

		for point in fc.keyframe_points:
			if point.co[0] == frame:
				key = point
				break

		if key is None:
			fc.keyframe_points.insert(frame, val)
		else:
			key.co[1] = val

		fc.update()

class ANIM_OT_insert_neutral_rotation(bpy.types.Operator):
	bl_idname = 'anim.insert_neutral_rotation'
	bl_label = 'Insert neutral rotation'
	bl_description = 'Insert neutral rotation for selected pose bones'
	bl_options = { 'REGISTER', 'UNDO' }

	def execute(self, context):
		arm = context.object
		act = arm.animation_data.action
		frame = context.scene.frame_current

		for bone in arm.pose.bones:
			if bone.select:
				apply_rotation(frame, bone, arm, act)

		return { 'FINISHED' }

def enable_item(self, context):
	self.layout.operator(ANIM_OT_insert_neutral_rotation.bl_idname)

def register():
	bpy.utils.register_class(ANIM_OT_insert_neutral_rotation)

	bpy.types.DOPESHEET_MT_key.append(enable_item)
	bpy.types.DOPESHEET_MT_context_menu.append(enable_item)
	bpy.types.GRAPH_MT_context_menu.append(enable_item)

def unregister():
	bpy.types.GRAPH_MT_context_menu.remove(enable_item)
	bpy.types.DOPESHEET_MT_context_menu.remove(enable_item)
	bpy.types.DOPESHEET_MT_key.remove(enable_item)

	bpy.utils.unregister_class(ANIM_OT_insert_neutral_rotation)
