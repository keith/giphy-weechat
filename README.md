# giphy-weechat

This is a simple [weechat](https://weechat.org/) plugin that inserts
random [giphy](https://giphy.com/) URLs based on a search.

## Usage:

```
/giphy SEARCH QUERY
```

## Installation

Install requests:

```sh
$ pip install requests
```

Copy the script to `~/.weechat/python/autoload`

```sh
mkdir -p ~/.weechat/python/autoload
wget https://raw.githubusercontent.com/keith/giphy-weechat/master/giphy.py ~/.weechat/python/autoload
```
