# Lesson 3.4: Make Classes
# Mini-Project: Movies Website

# In this file, you will define instances of the class Movie defined
# in media.py. After you follow along with Kunal, make some instances
# of your own!

# After you run this code, open the file fresh_tomatoes.html to
# see your webpage!

import media
import fresh_tomatoes

poster_folder = "poster_images\\"

brick = media.Movie("Brick",
											"Film noir/gumshoe. A high school student works to find and rescue a friend.\nUnder-rated; art-house.",
											poster_folder + "brick.jpe",
											"https://www.youtube.com/watch?v=DzvbrhtvK2o",
											"2006")

the_shawshank_redemption = media.Movie("The Shawshank Redemption",
													"A man finds redemption behind prison walls.",
													poster_folder + "the-shawshank-redemption.jpg",
													"https://www.youtube.com/watch?v=NmzuHjWmXOc",
													"1994")

interstellar = media.Movie("Interstellar",
													"Humanity struggles to survive, as the Earth's crops fail.",
													poster_folder + "interstellar.jpg",
													"https://www.youtube.com/watch?v=-gieJQejbHQ",
													"2014")

kill_bill = media.Movie("Kill Bill: Volume 1",
													"Spaghetti western/Kung fu movie/Anime mash up. \nA woman seeks revenge.",
													poster_folder + "kill-bill.jpg",
													"https://www.youtube.com/watch?v=7kSuas6mRpk",
													"2003")

kill_bill_volume_2 = media.Movie("Kill Bill: Volume 2",
													"Spaghetti western/Kung fu movie/Anime mash up. \nA woman seeks revenge.\nPart 2",
													poster_folder + "kill-bill-volume-2.jpg",
													"https://www.youtube.com/watch?v=WTt8cCIvGYI",
													"2004")

a_fistful_of_dollars = media.Movie("A Fistful of Dollars",
													"A man with no name, a town with a bloody feud.\nA boy cries.",
													poster_folder + "a-fistful-of-dollars.jpg",
													"https://www.youtube.com/watch?v=-X2DtiE7VLw",
													"1967")

movies = [brick, the_shawshank_redemption, interstellar, kill_bill, kill_bill_volume_2, a_fistful_of_dollars]
fresh_tomatoes.open_movies_page(movies)

# print media.Movie.__module__
