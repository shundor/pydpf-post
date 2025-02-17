==========
PyDPF-Post
==========

The Data Processing Framework (DPF) provides numerical simulation 
users and engineers with a toolbox for accessing and transforming simulation 
data. With DPF, you can perform complex preprocessing or postprocessing of
large amounts of simulation data within a simulation workflow.

DPF is an independent, physics-agnostic tool that you can plug into many 
apps for both data input and data output, including visualization and 
result plots. It can access data from solver result files and other neutral
formats, such as CSV, HDF5, and VTK files.

Using the many DPF operators that are available, you can manipulate and
transform this data. You can also chain operators together to create simple
or complex data-processing workflows that you can reuse for repeated or
future evaluations.

The data in DPF is defined based on physics-agnostic mathematical quantities 
described in self-sufficient entities called *fields*. This allows DPF to be 
a modular and easy-to-use tool with a large range of capabilities. 

.. image:: images/dpf-flow.png
  :width: 670
  :alt: DPF flow

The ``ansys.dpf.post`` package leverages the ``ansys.dpf.core`` package, which
is available at `PyDPF-Core GitHub <https://github.com/pyansys/DPF-Core>`_. With
PyDPF-Core, you can build more advanced and customized DPF workflows.


Brief demo
~~~~~~~~~~
Here is how you open and plot a result file generated by Ansys Workbench or
MAPDL:

.. code:: python

    >>> from ansys.dpf import post
    >>> from ansys.dpf.post import examples
    >>> solution = post.load_solution(examples.multishells_rst)
    >>> stress = solution.stress()
    >>> stress.xx.plot_contour(show_edges=False)


.. figure:: ./images/main_example.png
    :width: 300pt

    Basic stress contour plot

Here is how you extract the raw data as a :class:`numpy.ndarray` array:

.. code:: python

   >>> stress.xx.get_data_at_field(0)
   array([-3.37871094e+10, -4.42471752e+10, -4.13249463e+10, ...,
           3.66408342e+10,  1.40736914e+11,  1.38633557e+11])


For comprehensive demos, see :ref:`gallery`.


Key features
~~~~~~~~~~~~

**Computational efficiency**

PyDPF-Post is based on DPF, whose data framework localizes loading and
postprocessing on the DPF server, enabling rapid postprocessing workflows
because they are written in C and FORTRAN. Because DPF-Post presents results
in a Pythonic manner, you can rapidly develop simple or complex postprocessing
scripts.


**Easy to use**

The PyDPF-Post API automates the use of DPF's chained operators to make
postprocessing easier. The PyDPF-Post documentation describes how you can
use operators to compute results. This allows you to build your own custom,
low-level scripts to enable fast postprocessing of potentially multi-gigabyte
models using `PyDPF-Core <https://github.com/pyansys/pydpf-core>`_.


.. toctree::
   :maxdepth: 2
   :caption: Getting Started
   :hidden:

   getting_started/index
   user_guide/index
   api/index
   examples/index
   contributing
