import os
import shutil
import sys
import time

input_datadir = './train_img'
output_datadir = './pre_img'

def startPreprocessing(cwd):
    os.chdir(cwd + '/FaceRecognition/')
    if not hasattr(sys, 'argv'):
        sys.argv  = ['']
    sys.path.append('.')

    if os.path.isdir(os.getcwd() + '/pre_img/'):
        shutil.rmtree(os.getcwd() + '/pre_img/')
        time.sleep(.3) # making sure the folder is completely deleted before trying to create it again
        os.mkdir(os.getcwd() + '/pre_img/')

    from preprocess import preprocesses

    obj = preprocesses(input_datadir,output_datadir)
    nrof_images_total, nrof_successfully_aligned = obj.collect_data()

    return 'Total number of images: {}. Number of successfully aligned images: {}'.format(nrof_images_total, nrof_successfully_aligned)
