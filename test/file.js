all:

run: clean
	python bot.py -repo insightweets -user DavidAwad

test: clean
	python tests.py

clean:
	rm -rf local/
