all:

run: clean
	python bot.py -repo insightweets -user DavidAwad

clean:
	rm -rf local/
