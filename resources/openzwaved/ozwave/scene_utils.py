import logging
import time
from utilities.Constants import *
import node_utils

def scene_event(network, node, scene_id):
	logging.info('Scene Activation: %s' % (scene_id,))
	node_utils.save_node_value_event(node.node_id,  COMMAND_CLASS_CENTRAL_SCENE, 0, scene_id, 0)
	node_utils.save_node_value_event(node.node_id,  COMMAND_CLASS_SCENE_ACTIVATION, 0, scene_id, 0)
