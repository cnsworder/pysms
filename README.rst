pysms
############

virtualenv
==============

.. code-block:: shell

  virtualenv ./env
  . /env/bin/activate

requirements
======================

.. code-block:: shell

   pip -r requirements.txt


install
======================

.. code-block:: shell

   python setup.py install


use
===============

.. code-block:: python

   from pysms.message import Message

   msg = Message(8899)
   
   data = b"Hello"
   to_addr = ("127.0.0.1", 8899)

   msg.send(data, to_addr)

   recv_data = msg.recv()
