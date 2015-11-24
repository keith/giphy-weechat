# -*- coding: utf-8 -*-
#
# Insert a random giphy URL based on a search
#
# Usage: /giphy search
#
# History:
#
# Version 1.0.0: initial release
#

import requests
import weechat

URL = "http://api.giphy.com/v1/gifs/random?api_key=dc6zaTOxFJmzC&tag=%s"


def giphy(data, buf, args):
    search = args.replace(" ", "+")
    response = requests.get(URL % search)
    data = response.json()
    image_url = data["data"]["image_url"]

    weechat.buffer_set(buf, "input", image_url)
    weechat.buffer_set(buf, "input_pos", str(len(image_url)))

    return weechat.WEECHAT_RC_OK


def main():
    if not weechat.register("giphy", "Keith Smiley", "1.0.0", "MIT",
                            "Insert a random giphy URL", "", ""):
        return weechat.WEECHAT_RC_ERROR

    weechat.hook_command("giphy", "Insert a random giphy URL", "",
                         "", "", "giphy", "")

if __name__ == "__main__":
    main()
