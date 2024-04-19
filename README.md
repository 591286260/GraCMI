# GraCMI  

GraCMI: a novel model to predict cancer-related circRNA-miRNA interactions based on global graph structure information combined with molecular attribute features
We propose a denoising model for predicting CMI using multi-source features based on graph embedding, known as GraCMI. Firstly, we construct a heterogeneous network by combining the known associations among circRNAs, miRNAs, and cancer. Subsequently, molecular intrinsic attribute information is acquired by calculating the Gaussian kernel and Jaccard similarities between nodes of the same type. These attribute features are then integrated and passed through a Sparse Autoencoder for denoising. The graph embedding method GraRep is employed to mine the global structural features of nodes within the heterogeneous network. Finally, the attribute and structural features of molecules are input into an XGBoost classifier for CMI prediction.

Main dependency:  
python 3.8  
tensorFlow 2.10.0  
numpy 1.24.4  
gensim 4.3.1  
keras 2.4.3  

Usage:  
(1) Use gipk.m and jaccard.py to calculate molecular functional similarity.  
(2) Generate positive and negative samples for further analysis.  
(3) Use grarep.py to extract global structural features of the molecule.  
(4) Match positive and negative samples with features.  
(5) Use xgboost.py to predict CMI.  
