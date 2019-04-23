Basic Update Event Example
==========================

This sample creates a new event on a MISP server via the MISP ``Events`` API.
The sample then performs several updates to the stored event:

* Via a request to the MISP ``Attributes`` API, adds an internal comment
  attribute to the event.
* Via a request to the MISP ``Tag`` API, applies a tag to the internal comment
  attribute.
* Via a request to the MISP ``Sighting`` API, adds a
  `sighting <https://misp.gitbooks.io/misp-book/content/sightings/#sightings>`__
  to the internal comment attribute.

The sample then retrieves the contents of the stored event — including the
associated attribute, tag, and sighting — via a call to the MISP
``Search`` API.

The sample displays the results of the calls made to each of the MISP APIs.

For more information on the MISP APIs used by this sample, see the following
links:

* New Event: `PyMISP new_event API <https://media.readthedocs.org/pdf/pymisp/master/pymisp.pdf>`__
  and `MISP REST Event API <https://misp.gitbooks.io/misp-book/content/automation/#post-events>`__
  documentation.
* Attribute: `PyMISP add_named_attribute API <https://media.readthedocs.org/pdf/pymisp/master/pymisp.pdf>`__
  and `MISP REST Attribute API <https://misp.gitbooks.io/misp-book/content/automation/#attribute-management>`__.
* Tag: `PyMISP tag API <https://media.readthedocs.org/pdf/pymisp/master/pymisp.pdf>`__ and
  `MISP REST Tag API <https://misp.gitbooks.io/misp-book/content/automation/#tag-management>`__.
* Sighting: `PyMISP sighting API <https://media.readthedocs.org/pdf/pymisp/master/pymisp.pdf>`__ and
  `MISP REST Sighting API <https://misp.gitbooks.io/misp-book/content/automation/#sightings-api>`__.
* Search: `PyMISP search API <https://media.readthedocs.org/pdf/pymisp/master/pymisp.pdf>`__ and
  `MISP REST Search API <https://misp.gitbooks.io/misp-book/content/automation/#restful-searches-with-json-result>`__.

Prerequisites
*************

* The samples configuration step has been completed (see :doc:`sampleconfig`).
* The MISP DXL service is running (see
  `MISP DXL Service <https://github.com/opendxl/opendxl-misp-service-python>`__).
* In order to enable the use of the various APIs that this sample uses, each of
  the API names need to be listed in the ``apiNames`` setting under the
  ``[General]`` section in the "dxlmispservice.config" file that the service
  uses:

    .. code-block:: ini

        [General]
        apiNames=new_event,add_named_attribute,tag,sighting,search,...

  For more information on the configuration, see the
  `MISP DXL Python Service configuration documentation <https://opendxl.github.io/opendxl-misp-service-python/pydoc/configuration.html#misp-dxl-python-service-dxlmispservice-config>`__.

Running
*******

To run this sample execute the ``sample/basic/basic_update_event_example.py``
script as follows:

    .. code-block:: shell

        python sample/basic/basic_update_event_example.py

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
                "id": "189",
                "info": "OpenDXL MISP update event example",
                "locked": false,
                "org_id": "1",
                "orgc_id": "1",
                "proposal_email_lock": false,
                "publish_timestamp": "0",
                "published": false,
                "sharing_group_id": "0",
                "threat_level_id": "3",
                "timestamp": "1523377669",
                "uuid": "5acce605-f338-42d6-9f08-003aac110002"
            }
        }
        Response to the add internal comment request:
        [
            {
                "Attribute": {
                    "category": "Internal reference",
                    "comment": "This is only a test",
                    "deleted": false,
                    "disable_correlation": false,
                    "distribution": "5",
                    "event_id": "189",
                    "id": "53",
                    "object_id": "0",
                    "object_relation": null,
                    "sharing_group_id": "0",
                    "timestamp": "1523377669",
                    "to_ids": false,
                    "type": "comment",
                    "uuid": "5acce605-dad8-4286-add3-0141ac110002",
                    "value": "Added by the OpenDXL update event example",
                    "value1": "Added by the OpenDXL update event example",
                    "value2": ""
                }
            }
        ]
        Response to the tag request:
        {
            "message": "Tag Tagged by the OpenDXL MISP update event example(1) successfully attached to Attribute(53).",
            "name": "Tag Tagged by the OpenDXL MISP update event example(1) successfully attached to Attribute(53).",
            "url": "/tags/attachTagToObject"
        }
        Response to the sighting request:
        {
            "message": "Sighting added.",
            "name": "1 sighting successfully added.",
            "url": "/sightings/add/5acce605-dad8-4286-add3-0141ac110002"
        }
        Response to the search request for the new MISP event:
        {
            "response": [
                {
                    "Event": {
                        "Attribute": [
                            {
                                "ShadowAttribute": [],
                                "Sighting": [
                                    {
                                        "Organisation": {
                                            "id": "1",
                                            "name": "ORGNAME",
                                            "uuid": "5ac3c55a-41a4-4294-adf3-00f8ac110003"
                                        },
                                        "attribute_id": "53",
                                        "date_sighting": "1523377670",
                                        "event_id": "189",
                                        "id": "39",
                                        "org_id": "1",
                                        "source": "Seen by the OpenDXL MISP update event example",
                                        "type": "0",
                                        "uuid": "5acce606-dfd0-4b77-8f37-0142ac110002"
                                    }
                                ],
                                "Tag": [
                                    {
                                        "colour": "#75705b",
                                        "exportable": true,
                                        "hide_tag": false,
                                        "id": "1",
                                        "name": "Tagged by the OpenDXL MISP update event example",
                                        "user_id": false
                                    }
                                ],
                                "category": "Internal reference",
                                "comment": "This is only a test",
                                "deleted": false,
                                "disable_correlation": false,
                                "distribution": "5",
                                "event_id": "189",
                                "id": "53",
                                "object_id": "0",
                                "object_relation": null,
                                "sharing_group_id": "0",
                                "timestamp": "1523377669",
                                "to_ids": false,
                                "type": "comment",
                                "uuid": "5acce605-dad8-4286-add3-0141ac110002",
                                "value": "Added by the OpenDXL update event example"
                            }
                        ],
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
                        "attribute_count": "1",
                        "date": "2018-04-10",
                        "disable_correlation": false,
                        "distribution": "3",
                        "event_creator_email": "admin@admin.test",
                        "id": "189",
                        "info": "OpenDXL MISP update event example",
                        "locked": false,
                        "org_id": "1",
                        "orgc_id": "1",
                        "proposal_email_lock": false,
                        "publish_timestamp": "0",
                        "published": false,
                        "sharing_group_id": "0",
                        "threat_level_id": "3",
                        "timestamp": "1523377669",
                        "uuid": "5acce605-f338-42d6-9f08-003aac110002"
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
                info="OpenDXL MISP update event example",
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

        # Extract the id of the new event from the results of the new event request
        misp_event_id = new_event_response_dict

        # Invoke the add named attribute method to add an internal comment to the
        # event
        add_internal_comment_response_dict = client.add_named_attribute(
            event=misp_event_id,
            type_value="comment",
            value="Added by the OpenDXL MISP update event example",
            category="Internal reference",
            comment="This is only a test"
        )

        # Print out the response (convert dictionary to JSON for pretty printing)
        print("Response to the add internal comment request:\n{0}".format(
            MessageUtils.dict_to_json(add_internal_comment_response_dict,
                                      pretty_print=True)))


Next, the :meth:`dxlmispclient.client.MispClient.add_named_attribute`
method is invoked with some parameters to store in a new attribute for the MISP
event. Note that the ``event`` id value is extracted from the response received
for the prior "new_event" request.

The next step is to display the contents of the returned dictionary (``dict``)
which contains the results of the attempt to create the new attribute.

    .. code-block:: python

        # Extract the id of the internal comment from the results of the add
        # internal comment request
        internal_comment_attribute_id = \
            add_internal_comment_response_dict[0]["Attribute"]["uuid"]

        # Invoke the tag method to add a tag to the event
        tag_response_dict = client.tag(
            uuid=internal_comment_attribute_id,
            tag="Tagged by the OpenDXL MISP update event example"
        )

        # Print out the response (convert dictionary to JSON for pretty printing)
        print("Response to the tag request:\n{0}".format(
            MessageUtils.dict_to_json(tag_response_dict, pretty_print=True)))


Next, the :meth:`dxlmispclient.client.MispClient.tag` method is invoked with
some parameters to store in a new tag for the MISP event's attribute. Note that
the ``uuid`` value is extracted from the response received for the prior
"add_named_attribute" request.

The next step is to display the contents of the returned dictionary (``dict``)
which contains the results of the attempt to create the new tag.

    .. code-block:: python

        # Invoke the sighting method to add a sighting to the event
        sighting_response_dict = client.sighting(
            uuid=internal_comment_attribute_id,
            type=0,
            source="Seen by the OpenDXL MISP update event example"
        )

        # Print out the response (convert dictionary to JSON for pretty printing)
        print("Response to the sighting request:\n{0}".format(
            MessageUtils.dict_to_json(sighting_response_dict, pretty_print=True)))


Next, the :meth:`dxlmispclient.client.MispClient.sighting` method is invoked
with some parameters to store in a new sighting for the MISP event's attribute.
Note that the ``uuid`` id value is extracted from the response received for the
prior "add_named_attribute" request.

The next step is to display the contents of the returned dictionary (``dict``)
which contains the results of the attempt to create the new tag.

    .. code-block:: python

        # Invoke the search method to get the latest data for the event
        search_response_dict = client.search(
            eventid=new_event_response_dict["Event"]["id"]
        )

        # Print out the response (convert dictionary to JSON for pretty printing)
        print("Response to the search request for the new MISP event:\n{0}".format(
            MessageUtils.dict_to_json(search_response_dict, pretty_print=True)))


To confirm that the event, add internal comment attribute, tag, and sighting
were all stored properly, the :meth:`dxlmispclient.client.MispClient.search`
method is invoked to retrieve the information stored for the event.

The final step is to display the contents of the returned dictionary (``dict``)
which contains information for the stored event.
