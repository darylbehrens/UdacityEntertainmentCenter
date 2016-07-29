import media
import fresh_tomatoes

# Create Movie instances
toy_story = media.Movie("Toy Story",
                        "A Story of a boy and his toys",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/"
                        "Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=vwyZH85NQC4",
                        "G")

avatar = media.Movie("Avatar",
                     "A Marine on an alien planet",
                     "https://upload.wikimedia.org/wikipedia/"
                     "en/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY",
                     "PG-13")

magnolia = media.Movie("Magnolia",
                       "Fucking Crazy Movie",
                       "https://upload.wikimedia.org/wikipedia/en"
                       "/4/4b/Magnolia_poster.png",
                       "www.youtube.com/watch?v=cxcegktcxSM",
                       "NC-17")

eternalSunshine = media.Movie("Eternal Sunshine of the Spotless Mind",
                              "A man and women fall back in love, after "
                              "forgetting their past relationship",
                              "https://upload.wikimedia.org/wikipedia/en/6/62/"
                              "Eternal_sunshine_of_the_spotless_mind_ver3.jpg",
                              "https://www.youtube.com/watch?v=rb9a00bXf-U",
                              "R")

machinist = media.Movie("The Machinist",
                        "A man slowly loses his mind due to insomnia",
                        "https://upload.wikimedia.org/wikipedia/en/b/"
                        "b9/The_Machinist_poster.JPG",
                        "https://www.youtube.com/watch?v=H0fuHY4U1UA",
                        "R")

memento = media.Movie("Memento",
                      "A man wakes up each day with no memory"
                      ", and tries to solve a mystery",
                      "https://upload.wikimedia.org/wikipedia/en"
                      "/c/c7/Memento_poster.jpg",
                      "https://www.youtube.com/watch?v=0vS0E9bBSL0",
                      "R")

# Add Movies To A List
movies = [toy_story, avatar, magnolia, eternalSunshine, machinist, memento]

# using provided class, create HTML page with movies
fresh_tomatoes.open_movies_page(movies)
