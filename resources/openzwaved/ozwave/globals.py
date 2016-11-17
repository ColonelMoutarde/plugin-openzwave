import utils,network_utils,controller_utils,node_utils
#Various mappings
CONVERSION = {'Int': 'int',\
	'Decimal': 'float',\
	'Bool':'bool',\
	'Byte':'int',\
	'Short':'int',\
	'Button':'bool',\
	'Raw':'binary',\
	40 : 'error',\
	20 : 'debug',\
	10 : 'info',\
	'None': 0,\
	'ProtocolInfo': 1,\
	'Probe': 2,\
	'WakeUp': 3,\
	'ManufacturerSpecific1': 4,\
	'NodeInfo': 5,\
	'NodePlusInfo': 5,\
	'SecurityReport': 6,\
	'ManufacturerSpecific2': 7,\
	'Versions': 8,\
	'Instances': 9,\
	'Static': 10,\
	'CacheLoad': 11,\
	'Associations': 12,\
	'Neighbors': 13,\
	'Session': 14,\
	'Dynamic': 15,\
	'Configuration': 16,\
	'Complete': 17,\
	}

NETWORK_REST_MAPPING = {'start' : network_utils.start_network,\
	'stop' : network_utils.graceful_stop_network, \
	'writeZWConfig' : utils.write_config,\
	'manualBackup' : network_utils.manual_backup,\
	'getStatus': network_utils.get_status,\
	'getHealth' : network_utils.get_health,\
	'getNodesList' : network_utils.get_nodes_list,\
	'getZWConfig' : network_utils.get_oz_config,\
	'getOZBackups' : network_utils.get_oz_backups,\
	'getNeighbours' : network_utils.get_neighbours,\
	}

NODE_REST_MAPPING = {'all' : node_utils.get_all_info,\
	'getNodeStatistics' : node_utils.get_statistics, \
	'getPendingChanges' : node_utils.get_pending_changes,\
	'getHealth' : node_utils.get_health,\
	'requestNodeNeighbourUpdate': node_utils.request_neighbour_update,\
	'removeFailedNode': node_utils.remove_failed,\
	'healNode': node_utils.heal,\
	'replaceFailedNode': node_utils.replace_failed,\
	'sendNodeInformation': node_utils.send_information,\
	'hasNodeFailed': node_utils.has_failed,\
	'testNode': node_utils.test,\
	'refreshAllValues': node_utils.refresh_all_values,\
	'ghostKiller': node_utils.ghost_killer,\
	'requestNodeDynamic': node_utils.refresh_dynamic,\
	'refreshNodeInfo': node_utils.refresh_info,\
	'assignReturnRoute': node_utils.assign_return_route,\
	}

CONTROLLER_REST_MAPPING = {'hardReset' : controller_utils.hard_reset,\
	'receiveConfiguration' : controller_utils.receive_configuration, \
	'transferPrimaryRole' : controller_utils.transfer_primary_role,\
	'createNewPrimary' : controller_utils.create_new_primary,\
	'testNetwork' : controller_utils.test_network,\
	'serialAPISoftReset': controller_utils.serial_api_soft_reset,\
	'healNetwork': controller_utils.heal_network,\
	'cancelCommand': controller_utils.cancel_command,\
	}

#Various message
MSG_CHECK_DEPENDENCY = 'The dependency of openzwave plugin are not installed. Please check the plugin openzwave configuration page for instructions'

#Init Daemon
device = "auto"
# noinspection PyRedeclaration
log_level = "error"
port_server = 8083
config_folder = None
data_folder = None
pidfile = '/tmp/openzwaved.pid'
apikey = ''
callback = ''
assumeAwake = False
disabled_nodes = []
cycle = 0.3

# default_poll_interval = 1800000  # 30 minutes
default_poll_interval = 300000  # 5 minutes
maximum_poll_intensity = 1
controller_state = -1
maximum_number_notifications = 25
ghost_removal_delay = 15.0
not_supported_nodes = [0, 255]
network = None
network_information = None
ghost_node_id = None
pending_configurations = {}
pending_associations = {}
node_notifications = {}
dispatcher_is_connect = False
network_is_running = False
files_manager = None

#Daemon Globals
know_sticks = [{'idVendor': '0658', 'idProduct': '0200', 'name': 'Sigma Designs, Inc'},{'idVendor': '10c4', 'idProduct': 'ea60', 'name': 'Cygnal Integrated Products, Inc. CP210x UART Bridge'}]
jeedom_com = ''
options = ''
app = ''
