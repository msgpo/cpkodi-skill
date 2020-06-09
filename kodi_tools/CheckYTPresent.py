from mycroft.util.log import LOG
import json
import requests


# check if the youtube addon exists
def check_yt_present(kodi_path):
    json_header = {'content-type': 'application/json'}
    method = "Addons.GetAddons"
    addon_video = "xbmc.addon.video"
    kodi_payload = {
        "jsonrpc": "2.0",
        "method": method,
        "id": "1",
        "params": {
            "type": addon_video
        }
    }
    try:
        kodi_response = requests.post(kodi_path, data=json.dumps(kodi_payload), headers=json_header)
    except Exception as e:
        LOG.info(e)
        return False
    if "plugin.video.youtube" in kodi_response.text:
        return True
    else:
        return False
