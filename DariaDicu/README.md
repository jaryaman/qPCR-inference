# qPCR-inference
Data analysis project - modelling errors in qPCR using Bayesian inference

Command to run C code for inference:
```bash
# Compile and link to the GSL library (used for Cholesky decomposition).
gcc -std=gnu99 -Wall -c -I/usr/local/include inference.c | gcc -L /usr/local/lib -lgsl -lblas -std=gnu99 inference.c
# Run code (the argument is the seed for the random number generator).
./a.out 1 

```
A typical workflow:
```bash
#Modify the script to select the well/experiment file, then run it:
python exponential_phase_extraction_single_experiment.py

#Compile & link the inference code, then run it with ./a.out.
gcc -Wall -c -I/usr/local/include inference.c | gcc -L /usr/local/lib -lgsl -lblas inference.c
./a.out 1

#Plot results
python plot_scripts/plot_qpcr_results.py
```

JA: The following gcc command works on Ubuntu 14.04:
```bash
$ gcc -std=gnu99 inference.c `pkg-config --cflags --libs gsl` -o inference.ce
$ ./inference.ce 1
```

## Important directories
`experimental_data` : Raw data from qPCR
`inference_data` : Processed data from `experimental_data` ready for performing inference (exponential phase extraction)
