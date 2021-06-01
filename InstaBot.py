from instabot import Bot
bot = Bot()
bot.login(username="", password="")

######   upload a picture ######
bot.upload_photo("image.jpg",caption="Type your caption here")

######   Follow someone ######
bot.follow("elonmusk")

###### send a message ######
bot.send_message("Hello from techy",['user1','user2'])

###### get follower info ######
my_followers = bot.get_user_followers("yash.py")
for follower in my_followers:
    print(follower)

bot.unfollow_everyone()

