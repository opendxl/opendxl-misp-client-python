from __future__ import absolute_import
from dxlclient.message import Request
from dxlbootstrap.util import MessageUtils
from dxlbootstrap.client import Client


class MispClient(Client):
    """
    The "MISP DXL Python client library" client wrapper class.
    """

    _SERVICE_TYPE = "/opendxl-misp/service/misp-api"

    _REQ_TOPIC_ADD_NAMED_ATTRIBUTE = "add_named_attribute"
    _REQ_TOPIC_NEW_EVENT = "new_event"
    _REQ_TOPIC_SEARCH = "search"
    _REQ_TOPIC_SIGHTING = "sighting"
    _REQ_TOPIC_TAG = "tag"

    _PARAM_ID = "id"
    _PARAM_INFO = "info"
    _PARAM_EVENT = "event"
    _PARAM_TAG = "tag"
    _PARAM_TYPE_VALUE = "type_value"
    _PARAM_UUID = "uuid"
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
        kwargs[self._PARAM_EVENT] = event
        kwargs[self._PARAM_TYPE_VALUE] = type_value
        kwargs[self._PARAM_VALUE] = value
        return self._invoke_service(self._REQ_TOPIC_ADD_NAMED_ATTRIBUTE, kwargs)

    def new_event(self, info, **kwargs):
        kwargs[self._PARAM_INFO] = info
        return self._invoke_service(self._REQ_TOPIC_NEW_EVENT, kwargs)

    def sighting(self, uuid=None, id=None, **kwargs): # pylint: disable=invalid-name,redefined-builtin
        kwargs[self._PARAM_UUID] = uuid
        kwargs[self._PARAM_ID] = id
        return self._invoke_service(self._REQ_TOPIC_SIGHTING, kwargs)

    def search(self, **kwargs):
        return self._invoke_service(self._REQ_TOPIC_SEARCH, kwargs)

    def tag(self, uuid, tag):
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
