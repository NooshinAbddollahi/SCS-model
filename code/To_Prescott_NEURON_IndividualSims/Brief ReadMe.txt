This directories includes .txt and .dat files containing the waveform ("Active_50Hz..." and "Active_1000Hz..."), extracellular potentials along the 10 node modified MRG fiber, an example noise file, the .mod file of a modified McIntyre-Richardson-Grill axon containing a potassium AHP current, the NEURON script used to run the simulation (note: parameters shown and set in the NEURON script should be taken as the “golden” values, as these override the .mod file values).  So long as a .dll file is generated for the axnode_ahp.mod file using "mknrndll", the directory contains everything needed to simulate one dorsal column fiber paired with the single OU Noise file.

A script called “OUNoise_NoPlot” used to generate Ornstein-Uhlenbeck noise traces is also included and can be used to generate (e.g. the other required 30) noise traces needed to simulate a population of individual fibers.

ECAPs were generated using the same axon NEURON model, except that axons were lengthened to fit an established finite element model of the spinal cord (Lee et al., Med. Biol. Eng. Comput., 2010).  Following explicit simulation of a population of such longer fibers distributed over the white matter of the cord, ECAPs were generated using Helmholtz recirprocity, as described in Anaya et al., Neuromodulation, 2020.

Tianhe Zhang
Boston Scientific Neuromodulation
As of 06/27/2023

Anaya, C.J., Zander, H.J., Graham, R.D., Sankarasubramanian, V. and Lempka, S.F., 2020. Evoked potentials recorded from the spinal cord during neurostimulation for pain: a computational modeling study. Neuromodulation: Technology at the Neural Interface, 23(1), pp.64-73.

Yearwood, T.L., Hershey, B., Bradley, K. and Lee, D., 2010. Pulse width programming in spinal cord stimulation: a clinical study. Pain Physician, 13(4), p.321.