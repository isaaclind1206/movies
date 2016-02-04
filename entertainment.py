import fresh_tomatoes
import media


prisoners= media.Movie("Prisoners",
                       "A taut thriller about a father's quest to save his daughter, and his own soul",
                       "https://en.wikipedia.org/wiki/Prisoners_(2013_film)#/media/File:Prisoners2013Poster.jpg",
                       "https://www.youtube.com/watch?v=bpXfcTF6iVk")
#print (prisoners.storyline)

great_gatsby= media.Movie ("Great Gatsby",
                           "A young man is pulled into a tragic love triangle in the late 20's",
                           "https://en.wikipedia.org/wiki/The_Great_Gatsby_(2013_film)#/media/File:TheGreatGatsby2012Poster.jpg",
                           "https://www.youtube.com/watch?v=rARN6agiW7o")
#print (great_gatsby.storyline)
#great_gatsby.show_trailer() 

anchorman= media.Movie = ("Anchorman",
                        "A side splitting following the misadeventures of Ron Burgundy and his news team",
                        "https://en.wikipedia.org/wiki/Anchorman:_The_Legend_of_Ron_Burgundy#/media/File:Movie_poster_Anchorman_The_Legend_of_Ron_Burgundy.jpg",
                        "https://www.youtube.com/watch?v=NJQ4qEWm9lU")

the_perks_of_being_a_wallflower= ("The Perks of Being a Wallflower",
                                 "A tender coming of age story where a boy deals with the trials of growing up",
                                 "https://en.wikipedia.org/wiki/The_Perks_of_Being_a_Wallflower_(film)#/media/File:The_Perks_of_Being_a_Wallflower_Poster.jpg",
                                 "https://www.youtube.com/watch?v=n5rh7O4IDc0")

midnight_in_paris = ("Midnight in Paris",
                     "A frustrated author is thrilled when he is thrown back in time to rub elbows with his favorite authors",
                     "https://en.wikipedia.org/wiki/Midnight_in_Paris#/media/File:Midnight_in_Paris_Poster.jpg",
                     "https://www.youtube.com/watch?v=FAfR8omt-CY")

no_direction_home = ("No Direction Home",
                     "A documentary following Bob Dylan during the first three years of his career as a musician",
                     "https://en.wikipedia.org/wiki/No_Direction_Home#/media/File:Bobdylannodirectionhome.jpg",
                     "https://www.youtube.com/watch?v=QOUtzHizr9A")

movies= [prisoners, great_gatsby, anchorman, the_perks_of_being_a_wallflower, midnight_in_paris, no_direction_home]
fresh_tomatoes.open_movies_page(movies) 
                     
