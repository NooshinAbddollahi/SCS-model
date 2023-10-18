To run it the instructions should be:

Before simulation: Install NetPyNE

In Bash Terminal:

1. Change directories (cd) to model directory (../SCS-Circuit-Model)

2. Compile .mod files using >> nrnivmodl

3. Enter into interactive python (>> ipython)

4. Run the model using the command:

>> run init.py

Which will call the other files within the directory to simulate the model.


the model code is simulating the async input (1 kHz), but the data is also there to simulate 50 Hz.