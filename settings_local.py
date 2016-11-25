# Define critical settings and/or override defaults specified in
# settings.py. Copy this file to settings_local.py in the same
# directory as settings.py and edit. Any settings defined here
# will override those defined in settings.py



# Set this to point to your compiled checkout of caffe
caffevis_caffe_root      = '/usr/local/caffe/'

# Load model: caffenet-yos
# Path to caffe deploy prototxt file. Minibatch size should be 1.
PATH = '/Users/johmathe/code/enmi/rhd'
caffevis_deploy_prototxt = PATH + '/rhd_classifier_deploy.prototxt'

# Path to network weights to load.
caffevis_network_weights = PATH + '/rhd_classifier.caffemodel'

# Other optional settings; see complete documentation for each in settings.py.
caffevis_data_mean       = PATH + '/rhd_classifier_mean.npy'
caffevis_labels          = PATH + '/rhd_classifier_labels.txt'
caffevis_label_layers    = ('fc8_rhd', 'prob')
caffevis_prob_layer      = 'prob'
caffevis_unit_jpg_dir    = '%DVT_ROOT%/models/caffenet-yos/unit_jpg_vis'
caffevis_jpgvis_layers   = ['conv1', 'conv2', 'conv3', 'conv4', 'conv5', 'fc6_rhd', 'fc7_rhd', 'fc8_rhd', 'prob']
caffevis_jpgvis_remap    = {'pool1': 'conv1', 'pool2': 'conv2', 'pool5': 'conv5'}
def caffevis_layer_pretty_name_fn(name):
    return name.replace('pool','p').replace('norm','n')

# Use GPU? Default is True.
caffevis_mode_gpu = False
# Display tweaks.
# Scale all window panes in UI by this factor
#global_scale = 1.0
# Scale all fonts by this factor
#global_font_size = 1.0
