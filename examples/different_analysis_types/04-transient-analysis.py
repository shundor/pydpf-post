"""
.. _ref_trasient_analysis:

ANSYS DPF Computes transient anaysis
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This tutorial shows how post-process a transient 
analysis result file using API of the POST module.
"""

###############################################################################
# Get started
# ~~~~~~~~~~~
from ansys.dpf import post


###############################################################################
# Get the solution object
# ~~~~~~~~~~~~~~~~~~~~~~~
import os
path = os.getcwd()
# the following file is the result of a transient analysis computed 
# using Mechanical
path += "/../../tests/testfiles/msup_transient/plate1.rst"
# here we load the solution
solution = post.load_solution(path)
print(solution)

###############################################################################
# Get result objects
# ~~~~~~~~~~~~~~~~~~

###############################################################################
# Get a displacement result and compute data
# ==========================================

###############################################################################
# **Get the result**
disp_result = solution.displacement()
disp = disp_result.vector

###############################################################################
# **Check the number of fields**
disp.num_fields

###############################################################################
# **Get data from a field**
disp.get_data_at_field(0)

###############################################################################
# **Get maximum data value over all fields**
disp.max_data

###############################################################################
# **Get minimum data value over all fields**
disp.min_data

###############################################################################
# **Get maximum data value over a targeted field**
disp.get_max_data_at_field(0)

###############################################################################
# **Get minimum data value over all fields**
disp.get_min_data_at_field(0)

###############################################################################
# Get a stress result and plot a contour
# ======================================

###############################################################################
# **Get the result**
stress_result = solution.stress()
stress = stress_result.tensor
# shell and solid elements are in distinct fields. 
stress.num_fields

###############################################################################
# **Get the shell field**
shell_field = stress[0]
shell_field.shell_layers

###############################################################################
# **Get the solid field field**
solid_field = stress[1]

###############################################################################
# **Plot the contour**
stress.plot_contour()

###############################################################################
# **Plot a min/max value over time_freq_support chart**
stress_over_time_result = solution.stress(time_scoping = list(range(1, len(solution.time_freq_support.frequencies) + 1)))
stress_over_time = stress_over_time_result.tensor
stress_over_time.plot_chart()

###############################################################################
# Get an elastic_strain result and plot a chart
# =============================================

###############################################################################
# **Get the result**
elastic_strain_result = solution.elastic_strain()
elastic_strain = elastic_strain_result.tensor
# shell and solid elements are in distinct fields. 
elastic_strain.num_fields

###############################################################################
# **It is also possible to deal with plastic_strain and temperature this way.**
# The result file must contain those results.

