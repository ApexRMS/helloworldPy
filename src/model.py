import pysyncrosim as ps     # Load SyncroSim python package
import pandas as pd          # Load pandas python package
myScenario = ps.Scenario()   # Get the SyncroSim scenario that is currently running

# Load Scenario's input Datasheet from SyncroSim Library into pandas DataFrame
my_input_dataframe = myScenario.datasheets(name="helloworldPy_InputDatasheet")

# Extract model inputs from this pandas DataFrame and then do calculations
x = my_input_dataframe.x
a = my_input_dataframe.a
y = x * a

# Setup an empty pandas DataFrame ready to accept output in SyncroSim Datasheet format
my_output_dataframe = myScenario.datasheets(name="helloworldPy_OutputDatasheet")

# Copy output into this pandas DataFrame
my_output_dataframe['y'] = y

# Save this pandas DataFrame back to the SyncroSim Library's output Datasheet
myScenario.save_datasheet(data=my_output_dataframe,
                          name="helloworldPy_OutputDatasheet")