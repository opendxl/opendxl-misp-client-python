from __future__ import absolute_import
import os
import sys

from dxlbootstrap.util import MessageUtils
from dxlclient.client_config import DxlClientConfig
from dxlclient.client import DxlClient

root_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(root_dir + "/../..")
sys.path.append(root_dir + "/..")

from dxlmispclient.client import MispClient

# Import common logging and configuration
from common import *

# Configure local logger
logging.getLogger().setLevel(logging.ERROR)
logger = logging.getLogger(__name__)

# Create DXL configuration from file
config = DxlClientConfig.create_dxl_config_from_file(CONFIG_FILE)

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

    # Invoke the search method to get the latest data for the event
    search_response_dict = client.search(
        eventid=new_event_response_dict["Event"]["id"]
    )

    # Print out the response (convert dictionary to JSON for pretty printing)
    print("Response to the search request for the new MISP event:\n{0}".format(
        MessageUtils.dict_to_json(search_response_dict, pretty_print=True)))
