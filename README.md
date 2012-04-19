tiddlyapp
=========

a commandline tool for developing TiddlyWeb single page applications (SPAs). It is modeled after [CouchApp]

Language: Python, because the TiddlyWeb serverside ecosystem is mostly Python. Javascript is another good possiblity, since the users of the tool will be working primarily in Javascript.

## Functionality

The tool should initially support these modes:

`tiddlyapp push URL [options]`

Push contents of current directory to URL.

`tiddlyapp watch URL [options]`

Monitor the current directory for changes and immediately upload any changed files to URL.

`tiddlyapp proxy URL [options]`

Start a SOCKS proxy which serves local files when they are present and falls through to the remote server for other files. 

The last two modes both enable realtime testing of changes, so it isn't critical that both be implemented right away.