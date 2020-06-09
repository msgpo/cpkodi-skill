from mycroft.util.log import LOG
import requests
import json


def resume_play(kodi_path, player_id=1):
    """
     Must perform a GetActivePlayer to retrieve player_id
    """
    json_header = {'content-type': 'application/json'}
    method = "Player.PlayPause"
    kodi_payload = {
        "jsonrpc": "2.0",
        "method": method,
        "params": {
            "playerid": int(player_id),
            "play": True
        },
        "id": 1
    }
    try:
        kodi_response = requests.post(kodi_path, data=json.dumps(kodi_payload), headers=json_header)
        LOG.info(kodi_response.text)
        return kodi_response
    except Exception as e:
        LOG.error(e)
