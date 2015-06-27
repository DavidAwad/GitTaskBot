# GitTaskBot

### 80% Done. Forgive me friends.

This is a python app to run against your projects, if you have TODO's running
rampant in your codebase, you might miss something!

You can run this script and turn any of your `TODO` notes into github issues
for you to deal with on your own.

For that matter you can use any keyword you want, and you'll get an alert about
it.


Feel free to try the command line utility!!
```shell
(venv)➜  PyTaskBot git:(master) python bot.py --help
Usage: bot.py [OPTIONS]

  Small CLI to lint your code for keywords and create GitHub issues. You can
  specift a -key TODO or -key ??? and create issues for the ocurrences of any
  string.

Options:
  -key TEXT   Trigger Keyword.
  -user TEXT  The GitHub Username
  -repo TEXT  The name of the Repository
  --help      Show this message and exit.
```

# Notes
## Messing with issues
You may find it helpful to see the full formatting of a curl request to the git
api, as it was somewhat annoying to get it to actually create the damn things.

```shell

# will return your issue as defined.
curl https://api.github.com/repos/DavidAwad/insightweets/issues/1

# needs to authenticate you as a user, and can then create issues
curl -X POST -u DavidAwad -i -d '{ "title" :"my cool title", "body","body of my request"}' https://api.github.com/repos/DavidAwad/insightweets/issues/

```
