from imdbpie import Imdb
import json

imdb = Imdb(anonymize=True, cache=True)

for i in xrange(0, 9999999):
	cnt = 0
	movie_id = "tt" + str(i).zfill(7)
	with open('reviews.json', 'w') as fp:
		if imdb.title_exists(movie_id):
			cnt += 1
			title = imdb.get_title_by_id(movie_id)
			print movie_id, title.title
			reviews = imdb.get_title_reviews(movie_id)
			# if reviews == None:
			# 	reviews = []
			# else:
			# 	reviews = [review.__dict__ for review in reviews]
			json.dump([title, reviews], fp, indent=2, default=lambda o: o.__dict__)
			if cnt > 10:
				break