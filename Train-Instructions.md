Train Instructions:

- Setup of training machine on Amazon 
-> Version of AMI (Deep Learning Base AMI (Ubuntu) Version 3.0 (ami-07c2a77e)
-> Version of Amazon Instance > p3.2xlarge

- Follow the intruction of SSD to create the lmdb of WIDER FACE.
(Detail these steps here)

- Modify the data augmentation code of SSD to make sure that it does not change the image ratio.
(Detail these steps here including which source files and what lines of code)

- Modify the anchor match code of SSD to implement the 'scale compensation anchor matching strategy'.
(Detail these steps here including which source files and what lines of code)

- Train the model.
(Provide train script including amount of training time and validation loss curves and anything else useful)
