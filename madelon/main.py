# python spearmint_sync.py --method=GPEIOptChooser madelon_sofia_vw_rbf

import sys, subprocess, re, os
from math import exp

def get_validation_loss( data ):
	pattern = 'error: ([0-9.]+)'
	matches = re.search( pattern, data )

	validation_loss = float( matches.group( 1 ))
	return validation_loss
	
def get_validation_acc( data ):
	pattern = 'accuracy: ([0-9.]+)'
	matches = re.search( pattern, data )

	acc = float( matches.group( 1 ))
	return acc	
	

def run_test( params ):

	#debug_o = open( 'debug', 'wb' )
	#print >> debug_o, params
	
	centers = params["centers"][0]
	rbf_param = params["rbf_param"][0]
	#print >> debug_o, parameters

	# find centers
	# dimensionality w/label (+1)
	cmd = "sofia-kmeans --k %s --init_type optimized_kmeans_pp --opt_type mini_batch_kmeans --mini_batch_size 100 --iterations 500 --objective_after_init --objective_after_training --training_file data/all.libsvm.txt --model_out data/model_sofia --dimensionality 13" % ( centers )
	os.system( cmd )
	
	# map train	
	cmd = "sofia-kmeans --model_in data/model_sofia --test_file data/train.libsvm.txt --cluster_mapping_out data/mapped_train.libsvm.txt --cluster_mapping_type rbf_kernel --cluster_mapping_param %s" % ( rbf_param )
	os.system( cmd )

	# map validation
	cmd = "sofia-kmeans --model_in data/model_sofia --test_file data/validation.libsvm.txt --cluster_mapping_out data/mapped_validation.libsvm.txt --cluster_mapping_type rbf_kernel --cluster_mapping_param %s" % ( rbf_param )
	os.system( cmd )	

	# map test
	#cmd = "sofia-kmeans --model_in data/model_sofia --test_file data/test.libsvm.txt --cluster_mapping_out data/mapped_test.libsvm.txt"
	#os.system( cmd )	

	###

	# train 2 vw
	cmd = "python libsvm2vw.py data/mapped_train.libsvm.txt data/mapped_train.vw"
	os.system( cmd )

	# validation 2 vw	
	cmd = "python libsvm2vw.py data/mapped_validation.libsvm.txt data/mapped_validation.vw"
	os.system( cmd )	
	
	###

	# train vw
	cmd = "vw -d data/mapped_train.vw -f data/model_vw -c -k --passes 100 --loss_function logistic"
	os.system( cmd )

	# predict vw
	cmd = "vw -t -d data/mapped_validation.vw -i data/model_vw -p data/p.txt  --loss_function logistic"
	os.system( cmd )

	# python rmse.py data/sparse_validation.vw data/p.txt
	data = subprocess.check_output( ['python', 'auc.py', 'data/mapped_validation.vw', 'data/p.txt' ] )
	validation_loss = get_validation_loss( data )
	
	#data = subprocess.check_output( ['python', 'acc.py', 'data/mapped_validation.vw', 'data/p.txt' ] )
	#validation_acc = get_validation_acc( data )	

	print 'error: ', validation_loss
	#print 'acc: ', validation_acc
	print
	
	return validation_loss

def main( job_id, params ):
	print 'Job id:', str( job_id )
	print "centers: %s" % ( params['centers'][0] )
	print "rbf param: %s" % ( params['rbf_param'][0] )
	
	return run_test( params )
