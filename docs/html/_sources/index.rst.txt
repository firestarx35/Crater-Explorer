Moonshot: Automatic Impact Crater Detection on the Moon
=======================================================

Synopsis:
---------
Impact craters are the most ubiquitous surface feature on rocky
planetary bodies. Crater number density can be used to estimate the
age of the surface: the more densely cratered the terrain, the older
the surface. When independent absolute ages for a surface are
available for calibration of crater counts, as is the case for some
lava flows and regions of the Moon, crater density can be used to
estimate an absolute age of the surface.

Crater detection and counting has traditionally been done by laborious
manual interrogation of images of a planetary surface taken by
orbiting spacecraft. However,
the size frequency distribution of impact craters is a steep negative
power-law, implying that there are many small craters for each larger
one. For example, for each 1-km crater on Mars, there are more than
a thousand 100-m craters. With the increased fidelity
of cameras on orbiting spacecraft, the number of craters visible in
images of remote surfaces has become so large that manual counting is
unfeasible. Furthermore, manual counting can be time consuming and
subjective.
This motivates the need for automated crater detection and counting algorithms.


Task definition
------------------
The aim of this project is to develop a software tool for automatically detecting impact craters in images of planetary surfaces and deriving from this a crater-size frequency distribution that can be used for dating. 
The whole project can be separated into three main subtasks.

Crater Detection Model
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Develop a module for automatically locating craters
in images based on YOLO. Then, train and test the CDM with a dataset of images of the surface of Mars, taken by the THEMIS camera (100-m/px),
together with labels that provide the bounding boxes of any craters in
the image larger than ~1-2 km in diameter. 

Develop a training dateset for the Moon
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
A training dataset is needed to train the crater detection model for moon. To develop this dataset we have been provided with four images of
portions of the lunar surface and a csv file containing the location
and size of all manually counted craters on this part of the Moon with the parts of the crater database.

The four images provided are for the regions:

- A: -180 to -90 longitude, -45 to 0 latitude;

- B: -180 to -90 longitude, 0 to 45 latitude; 

- C: -90 to 0 longitude, -45 to 0 latitude; 

- D: -90 to 0 longitude, 0 to 45 latitude.


A tool for analysis of craters
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
The purpose of this tool is to allow a user to quickly and
automatically identify all craters in the image and from this generate
a size-frequency distribution of the craters for the purpose of dating
the planetary surface. It provides the
functionality to calculate physical, real-world crater sizes and
locations if the image location, size and resolution is provided and identify craters in each image, as
well as the number of true positives and false negatives.

Model Performance metric
========================
We will calculate the Intersection over Union
index (IoU) for every crater bounding box in your model detection set
against every crater in our ground truth crater bounding box list

We will then pair each bounding box :math:`g_i` in the ground truth list with a
detected crater, :math:`c_i` in your list, with the pairings chosen to
maximise the sum :math:`\sum_i \textrm{IoU}(g_i, c_i)`

We will calculate a crater recall index using the formula 

.. math:: R=\frac{\textrm{number of crater pairs with IoU>0.5 and area of }g_i>A_R}{\textrm{number of ground truth bounding boxes with area of }g_i>A_R}

where :math:`A_R` is the fractional area of the image that corresponds to a crater size :math:`D_R`.

We calculate a crater precision index using the formula

.. math:: P=\frac{\textrm{number of crater pairs with IoU>0.5 and area of }c_i>A_P}{\textrm{number of detected bounding boxes with area of }c_i>A_P},

where :math:`A_P` is the fractional area of the image that corresponds to a crater size
:math:`D_P`.

Finally we will calculate the crater $F1$ score via the usual formula

.. math:: F1 =\frac{2}{\frac{1}{P}+\frac{1}{R}}.


