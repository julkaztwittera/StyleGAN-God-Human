import os

## Pretrained models paths
e4e = './pti/e4e_w+.pt'
stylegan2_ada_shhq = './training_results/sg2/god_human/00010-god_human_dataset-rectangle-mirror-shhq4-noaug-resumecustom/network-snapshot-000120.pkl'
ir_se50 =  '' #'./model_ir_se50.pth' 

## Dirs for output files
checkpoints_dir = './outputs/pti/checkpoints/'
embedding_base_dir = './outputs/pti/embeddings'
experiments_output_dir = './outputs/pti/god_human'

## Input info
### Input dir, where the images reside
input_data_path = './ars_electronica'
### Inversion identifier, used to keeping track of the inversion results. Both the latent code and the generator
input_data_id = 'test'

## Keywords
pti_results_keyword = 'PTI'
e4e_results_keyword = 'e4e'
sg2_results_keyword = 'SG2'
sg2_plus_results_keyword = 'SG2_Plus'
multi_id_model_type = 'multi_id'