#!/usr/bin/python3
# SPDX-License-Identifier: GPL-3.0-or-later

import bpy

id = 'anim.insert_neutral_rotation'
label = 'Insert neutral rotation'
desc = 'Insert neutral rotation into active action for selected pose bones'

def draw_button(self, context):
	self.layout.operator(id)

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
			if abs(point.co[0] - frame) < 0.000001:
				key = point
				break

		if key is None:
			fc.keyframe_points.insert(frame, val)
		else:
			key.co[1] = val

		fc.update()

class insert_neutral_rotation(bpy.types.Operator):
	bl_idname = id
	bl_label = label
	bl_description = desc
	bl_options = { 'REGISTER', 'UNDO' }

	def execute(self, context):
		arm = context.object
		act = arm.animation_data.action
		frame = context.scene.frame_current

		for bone in arm.pose.bones:
			if bone.select:
				apply_rotation(frame, bone, arm, act)

		return { 'FINISHED' }

bpy.utils.register_class(insert_neutral_rotation)

bpy.types.DOPESHEET_MT_key.append(draw_button)
bpy.types.DOPESHEET_MT_context_menu.append(draw_button)
bpy.types.GRAPH_MT_context_menu.append(draw_button)
