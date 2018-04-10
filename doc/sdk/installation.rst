Library Installation
====================

Prerequisites
*************

* OpenDXL Python Client library installed
   `<https://github.com/opendxl/opendxl-client-python>`_

* The OpenDXL Python Client prerequisites must be satisfied
   `<https://opendxl.github.io/opendxl-client-python/pydoc/installation.html>`_

* The MISP DXL service is running and available on the DXL fabric
    `<https://github.com/opendxl/opendxl-misp-service-python>`_

* Python 2.7.9 or higher in the Python 2.x series or 3.4.0 or higher in the
  Python 3.x series installed within a Windows or Linux environment.

Installation
************

Use ``pip`` to automatically install the library:

    .. parsed-literal::

        pip install dxlmispclient-\ |version|\-py2.py3-none-any.whl

Or with:

    .. parsed-literal::

        pip install dxlmispclient-\ |version|\.zip

As an alternative (without PIP), unpack the dxlmispclient-\ |version|\.zip (located in the lib folder) and run the setup
script:

    .. parsed-literal::

        python setup.py install
