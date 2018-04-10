from __future__ import absolute_import
from dxlclient.message import Request
from dxlbootstrap.util import MessageUtils
from dxlbootstrap.client import Client


class MispClient(Client):
    """
    The "MISP DXL Python client library" client wrapper class.
    """

    #: The DXL service type for the MISP API.
    _SERVICE_TYPE = "/opendxl-misp/service/misp-api"

    #: The DXL topic fragment for the MISP "add_name_attribute" method.
    _REQ_TOPIC_ADD_NAMED_ATTRIBUTE = "add_named_attribute"
    #: The DXL topic fragment for the MISP "new_event" method.
    _REQ_TOPIC_NEW_EVENT = "new_event"
    #: The DXL topic fragment for the MISP "search" method.
    _REQ_TOPIC_SEARCH = "search"
    #: The DXL topic fragment for the MISP "sighting" method.
    _REQ_TOPIC_SIGHTING = "sighting"
    #: The DXL topic fragment for the MISP "tag" method.
    _REQ_TOPIC_TAG = "tag"

    #: The id parameter.
    _PARAM_ID = "id"
    #: The event info parameter.
    _PARAM_INFO = "info"
    #: The event (id) parameter.
    _PARAM_EVENT = "event"
    #: The tag parameter.
    _PARAM_TAG = "tag"
    #: The attribute type value parameter.
    _PARAM_TYPE_VALUE = "type_value"
    #: The uuid parameter.
    _PARAM_UUID = "uuid"
    #: The value parameter.
    _PARAM_VALUE = "value"

    def __init__(self, dxl_client, misp_service_unique_id=None):
        """
        Constructor parameters:

        :param dxl_client: The DXL client to use for communication with the
            fabric
        :param str misp_service_unique_id: Unique id to use as part of the
            request topic names for the MISP DXL service.
        """
        super(MispClient, self).__init__(dxl_client)
        self._misp_service_unique_id = misp_service_unique_id

    def add_named_attribute(self, event, type_value, value, **kwargs):
        """
        Adds one or more attributes to an existing event. See the documentation
        for the
        `MISP REST Attribute Management API <https://misp.gitbooks.io/misp-book/content/automation/#attribute-management>`__
        and the "add_named_attribute" method in the
        `pymisp.PyMISP class <https://media.readthedocs.org/pdf/pymisp/latest/pymisp.pdf>`__
        for more information on the full set of available parameters and data
        format.

        :param str event: The id of the event to add the attribute to.
        :param str type_value: The type to associate with the attribute.
        :param value: The attribute value.
        :param dict kwargs: Dictionary of additional parameters to pass along
            to the MISP Python API.
        :return: Result of the attribute addition attempt.
        :rtype: dict
        """
        kwargs[self._PARAM_EVENT] = event
        kwargs[self._PARAM_TYPE_VALUE] = type_value
        kwargs[self._PARAM_VALUE] = value
        return self._invoke_service(self._REQ_TOPIC_ADD_NAMED_ATTRIBUTE, kwargs)

    def new_event(self, info, **kwargs):
        """
        Create and add a new event. See the documentation for the
        `MISP REST Event Management API <https://misp.gitbooks.io/misp-book/content/automation/#events-management>`__
        and the "new_event" method in the
        `pymisp.PyMISP class <https://media.readthedocs.org/pdf/pymisp/latest/pymisp.pdf>`__
        for more information on the full set of available parameters and data
        format.

        :param str info: Info to include in the event.
        :param dict kwargs: Dictionary of additional parameters to pass along
            to the MISP Python API.
        :return: Result of the event creation attempt.
        :rtype: dict
        """
        kwargs[self._PARAM_INFO] = info
        return self._invoke_service(self._REQ_TOPIC_NEW_EVENT, kwargs)

    def sighting(self, uuid=None, id=None, **kwargs): # pylint: disable=invalid-name,redefined-builtin
        """
        Set a single sighting. See the documentation for the
        `MISP REST Sighting API <https://misp.gitbooks.io/misp-book/content/automation/#sightings>`__
        and the "search" method in the
        `pymisp.PyMISP class <https://media.readthedocs.org/pdf/pymisp/latest/pymisp.pdf>`__
        for more information on the full set of available parameters and data
        format.

        :param str uuid: UUID of the attribute to update
        :param str id: ID of the attribute to update
        :param dict kwargs: Dictionary of additional parameters to pass along
            to the MISP Python API.
        :return: Result of the attribute addition attempt.
        :rtype: dict
        """
        kwargs[self._PARAM_UUID] = uuid
        kwargs[self._PARAM_ID] = id
        return self._invoke_service(self._REQ_TOPIC_SIGHTING, kwargs)

    def search(self, **kwargs):
        """
        Search via the MISP REST API. See the documentation for the
        `MISP REST Search API <https://misp.gitbooks.io/misp-book/content/automation/#restful-searches-with-json-result>`__
        and the "search" method in the
        `pymisp.PyMISP class <https://media.readthedocs.org/pdf/pymisp/latest/pymisp.pdf>`__
        for more information on the full set of available parameters and data
        format.

        :param dict kwargs: Dictionary of additional parameters to pass along
            to the MISP Python API.
        :return: Result of the search attempt.
        :rtype: dict
        """
        return self._invoke_service(self._REQ_TOPIC_SEARCH, kwargs)

    def tag(self, uuid, tag):
        """
        Tag an object (event or attribute). See the documentation for the
        `MISP REST Tag Management API <https://misp.gitbooks.io/misp-book/content/automation/#tag-management>`_
        and the "tag" method in the
        `pymisp.PyMISP class <https://media.readthedocs.org/pdf/pymisp/latest/pymisp.pdf>`__
        for more information on the full set of available parameters and data
        format.

        :param str uuid: UUID of the object to update
        :param str id: ID of the object to update
        :return: Result of the tag attempt.
        :rtype: dict
        """
        kwargs = dict()
        kwargs[self._PARAM_UUID] = uuid
        kwargs[self._PARAM_TAG] = tag
        return self._invoke_service(self._REQ_TOPIC_TAG, kwargs)

    def _invoke_service(self, request_method, request_dict):
        """
        Invokes a request method on the MISP DXL service.

        :param str request_method: The request method to append to the
            topic for the request.
        :param dict request_dict: Dictionary containing request information.
        :return: Results of the service invocation.
        :rtype: dict
        """
        if self._misp_service_unique_id:
            request_service_id = "/{}".format(
                self._misp_service_unique_id)
        else:
            request_service_id = ""

        # Create the DXL request message.
        request = Request("{}{}/{}".format(
            self._SERVICE_TYPE,
            request_service_id,
            request_method))

        # Set the payload on the request message (Python dictionary to JSON
        # payload).
        MessageUtils.dict_to_json_payload(request, request_dict)

        # Perform a synchronous DXL request.
        response = self._dxl_sync_request(request)

        # Convert the JSON payload in the DXL response message to a Python
        # dictionary and return it.
        return MessageUtils.json_payload_to_dict(response)
