"""
Twitter Bot using Python and Twitter API v2.
This script will post a tweet from the list of tweets every day and start over from the beginning of the list when it reaches the last tweet.
"""

import tweepy
import time

# Add your Twitter API keys and access tokens here
consumer_key = "KJuOILpbDheO3dHwvEMxqNMfj"
consumer_secret = "V8RzbF3BNB52Nm1bU5Rl7doCpRxpDMmZoqkG0LlQe2t5KDIOF8"
access_token = "1520168816952680448-7f2sEYLZzfu8b9SF8sakGot6s54L8l"
access_token_secret = "RlzRxR9YrR2GvUPv5ytysJy8eKOaifGViEDm0rHpVOUAw"

# Authenticate with Twitter API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# List of tweets
tweet_list = [
    "Just as the waters around the bridge piles thrust and accumulate, so power collects around those who stand independently and are unconcerned about it. The power-greedy ego must be conquered and turned to something infinitely greater than itself.",
    "Manage so that what you can do nothing against, also can do nothing against you.",
    "The men of affairs enjoy life, but the virtuous prolongs it.",
    "The only true men are the initiated.",
    "Spirituality alone makes one superior to another.",
    "That your mother and father produced you through mutual desire and you were born in the womb, is merely your coming into existence. But the birth that a teacher produces is real, free from old age and free from death.",
    "The brāhmaṇa who brings about the Vedic birth of an older person and who teaches him his own duties becomes his father, according to law, even if he is himself a child.",
    "Those who are capable of 'fulfilling Heaven's law with calm and imperturbability and no help from the outside' are at the pinnacle, and are 'perfected' and 'transcendent' men.",
    "If there ever was a civilization of slaves on a grand scale, the one in which we are living is it.",
    "Those who are born as men must realize themselves as men, while those who are born as women must realize themselves as women.",
    "Even in regard to the supernatural vocation, man and woman must both have their own distinctive paths to follow, which cannot be altered without them turning into contradictory and inorganic ways of being.",
    "The supreme nobility of a Roman emperor does not consist in being a master of slaves, but in being a lord of free men, who loves freedom even in those who serve him.",
    "Humans must never submit to animals.",
    "You must learn discipline. How can you control others when you cannot control yourself?",
    "Logical thought has its limitations: Deduction and Causality. (Reserve an attitude of questioning distrust for anything that comes in the guise of logic.)",
    "All proofs inevitably lead to propositions which have no proof. All things are known because we want to believe in them.",
    "Inner superiority, rather than simple force, gives rise naturally to the dignity, capacity, and rights of the true aristocracy, who can arouse in others a spontaneous recognition and a pride in following and serving them.",
    "You seldom learn the names of the truly wealthy and powerful.",
    "Any required change may be effected by the application of the proper kind and degree of Force in the proper manner, through the proper medium to the proper object.",
    "What is mobile obeys what is immobile, and the powers of nature become subjected to him who can resist them.",
    "Enjoy nothing until you have first vanquished it within yourself.",
    "A Man whose conscious will is at odds with his True Will is wasting his strength. He cannot hope to influence his environment efficiently.",
    "Man is ignorant of the nature of his own being and powers. Even his idea of his limitations is based on experience of the past, and every step in his progress extends his empire. There is therefore no reason to assign theoretical limits to what he may be or do.",
    "Every force in the Universe is capable of being transformed into any other kind of force by using suitable means. There is thus an inexhaustible supply of any particular kind of force that we may need.",
    "History is written by the victors.",
    "People rarely say what they mean, but they do. (Body language)",
    "A Man who is doing his True Will has the inertia of the Universe to assist him.",
    "That which submits rules. Assimilation and survival.",
    "There is no necessity humans hate more than the unpredictable",
    "Nature is a continuous phenomenon, though we may not know in all cases how things are connected.",
    "The truth: Whose truth? Modified in what way? In what context?",
    "The persistence and power of superstition in modern societies.",
    "Is it large or small, beautiful or ugly, weak or powerful? These are relative terms, and must be understood in their context."
]

current_tweet = 0


def post_tweet():
    global current_tweet
    try:
        api.update_status(tweet_list[current_tweet])
        print("Tweet posted successfully!")
    except Exception as e:
        print("Error: ", e)
        current_tweet += 1

# If last tweet is reached, start over


if current_tweet == len(tweet_list):
    current_tweet = 0

while True:
    post_tweet()


time.sleep(86400)
