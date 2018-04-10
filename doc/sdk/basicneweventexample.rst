Basic New Event Example
=======================

This sample creates a new event on a MISP server via the MISP ``Events`` API.
The sample then retrieves the contents of the stored event via a call to the
MISP ``Search`` API. The sample displays the results of the calls to the
``Events`` and ``Search`` APIs.

For more information on the MISP ``Events`` API, see the
`PyMISP new_event API <https://media.readthedocs.org/pdf/pymisp/master/pymisp.pdf>`__
and `MISP REST Event API <https://misp.gitbooks.io/misp-book/content/automation/#post-events>`__
documentation.

Prerequisites
*************

* The samples configuration step has been completed (see :doc:`sampleconfig`).
* The MISP DXL service is running (see
  `MISP DXL Service <https://github.com/opendxl/opendxl-misp-service-python>`__).
* In order to enable the use of the ``new_event`` and ``search`` APIs, both API
  names need to be listed in the ``apiNames`` setting under the ``[General]``
  section in the "dxlmispservice.config" file that the service uses:

    .. code-block:: ini

        [General]
        apiNames=new_event,search,...

  For more information on the configuration, see the
  `MISP DXL Python Service configuration documentation <https://opendxl.github.io/opendxl-misp-service-python/pydoc/configuration.html#misp-dxl-python-service-dxlmispservice-config>`__.

Running
*******

To run this sample execute the ``sample/basic/basic_new_event_example.py``
script as follows:

    .. code-block:: shell

        python sample/basic/basic_new_event_example.py

The output should appear similar to the following:

    .. code-block:: shell

        Response to the new event request:
        {
            "Event": {
                "Attribute": [],
                "Galaxy": [],
                "Object": [],
                "Org": {
                    "id": "1",
                    "name": "ORGNAME",
                    "uuid": "5ac3c55a-41a4-4294-adf3-00f8ac110003"
                },
                "Orgc": {
                    "id": "1",
                    "name": "ORGNAME",
                    "uuid": "5ac3c55a-41a4-4294-adf3-00f8ac110003"
                },
                "RelatedEvent": [],
                "ShadowAttribute": [],
                "analysis": "1",
                "attribute_count": "0",
                "date": "2018-04-10",
                "disable_correlation": false,
                "distribution": "3",
                "event_creator_email": "admin@admin.test",
                "id": "188",
                "info": "OpenDXL MISP new event example",
                "locked": false,
                "org_id": "1",
                "orgc_id": "1",
                "proposal_email_lock": false,
                "publish_timestamp": "0",
                "published": false,
                "sharing_group_id": "0",
                "threat_level_id": "3",
                "timestamp": "1523377618",
                "uuid": "5acce5d2-2258-41cf-a1e3-0039ac110002"
            }
        }
        Response to the search request for the new MISP event:
        {
            "response": [
                {
                    "Event": {
                        "Attribute": [],
                        "Galaxy": [],
                        "Object": [],
                        "Org": {
                            "id": "1",
                            "name": "ORGNAME",
                            "uuid": "5ac3c55a-41a4-4294-adf3-00f8ac110003"
                        },
                        "Orgc": {
                            "id": "1",
                            "name": "ORGNAME",
                            "uuid": "5ac3c55a-41a4-4294-adf3-00f8ac110003"
                        },
                        "RelatedEvent": [],
                        "ShadowAttribute": [],
                        "analysis": "1",
                        "attribute_count": "0",
                        "date": "2018-04-10",
                        "disable_correlation": false,
                        "distribution": "3",
                        "event_creator_email": "admin@admin.test",
                        "id": "188",
                        "info": "OpenDXL MISP new event example",
                        "locked": false,
                        "org_id": "1",
                        "orgc_id": "1",
                        "proposal_email_lock": false,
                        "publish_timestamp": "0",
                        "published": false,
                        "sharing_group_id": "0",
                        "threat_level_id": "3",
                        "timestamp": "1523377618",
                        "uuid": "5acce5d2-2258-41cf-a1e3-0039ac110002"
                    }
                }
            ]
        }

Details
*******

The majority of the sample code is shown below:

    .. code-block:: python

        # Create the client
        with DxlClient(config) as dxl_client:

            # Connect to the fabric
            dxl_client.connect()

            logger.info("Connected to DXL fabric.")

            # Create client wrapper
            client = MispClient(dxl_client)

            # Invoke the new event method
            new_event_response_dict = client.new_event(
                distribution=3,
                info="OpenDXL MISP new event example",
                analysis=1,
                threat_level_id=3
            )

            # Print out the response (convert dictionary to JSON for pretty printing)
            print("Response to the new event request:\n{0}".format(
                MessageUtils.dict_to_json(new_event_response_dict, pretty_print=True)))


Once a connection is established to the DXL fabric, a
:class:`dxlmispclient.client.MispClient` instance is created
which will be used to invoke remote commands on the MISP DXL service.

Next, the :meth:`dxlmispclient.client.MispClient.new_event` method is invoked
with some parameters to store for the new MISP event.

The next step is to display the contents of the returned dictionary (``dict``)
which contains the results of the attempt to create the new MISP event.

    .. code-block:: python

        # Invoke the search method to get the latest data for the event
        search_response_dict = client.search(
            eventid=new_event_response_dict["Event"]["id"]
        )

        # Print out the response (convert dictionary to JSON for pretty printing)
        print("Response to the search request for the new MISP event:\n{0}".format(
            MessageUtils.dict_to_json(search_response_dict, pretty_print=True)))


To confirm that the event was stored properly, the
:meth:`dxlmispclient.client.MispClient.search` method is invoked to retrieve the
information stored for the event. The method is invoked with the ``eventid`` of
the event to retrieve. Note that the ``eventid`` used in the search request is
extracted from the response received for the prior "new_event" request.

The final step is to display the contents of the returned dictionary (``dict``)
which contains information for the stored event.
