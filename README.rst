HTTP/2 Multiplexing
===================

This is the code to accompany an `article
<https://medium.com/@pgjones/http-1-is-dead-81b7588d617e>`_.


Running
-------

Assuming you have at least Python 3.7, firstly to setup:

.. code-block::

    $ python -m venv venv
    $ source venv/bin/activate
    $ cd app
    $ pip install -r requirements.txt

Then you can either run with the HTTP/1.1 (h11) or HTTP/2 (h2)
configuration,

.. code-block::

    $ hypercorn --config="python:h11_config.py" run:app
    $ hypercorn --config="python:h2_config.py" run:app

Performance
-----------

The purpose of this code is to demonstrate the efficiency of HTTP/2
multiplexing by comparing the total time to make all twenty requests
under HTTP/1.1 and HTTP/2. HTTP/2 WebSockets are only possible (as of
early 2019) in Firefox (chrome requires an additional flag change).
