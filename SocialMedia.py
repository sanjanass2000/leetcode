

# Design a social media platform that captures interactions between 
# users, posts, and comments
# structure to represent interactions can be a graph => each node, holds

# platform hosts 
#   users -> connected to other users
#       -- standalone posts
#       -- comments directed at other users
# graph with directed edges where edges are comments
# each node is a user mapped and a list of their posts -> User1: ["hello", "wwhats up", "yayy"]


#class User
# class Post
# class Comment

class User:
    def __init__(self, username):
       self.username = username
       self.posts = []
    

    # getter functions
    def get_username(self):
       return self.__username


    #setter functions
    def set_username(self, user):
        self.username = user

    # action fucntions:
    def make_post(self, content):
        
        post  = Post(self, content)

        self.posts.append(post)
        return post
    
    def edit_post(self, post_name):
        pass


# class Post
class Post:
    def __init__(self, user, content):
        self.user = user
        self.content = content
        self.comments = []

    def add_comment(self, comment, user):
        comment = Comment(user, comment)
        self.comments.append(comment)
        return comment
    


class Comment: 
    def __init__(self, user, comment):
        self.user = user
        self.comment = comment


user1 = User("Mary Smith")
post = user1.make_post("Hello, world!")
user2 = User("David Finn")
comment = post.add_comment("Nice post!", user2)
comment2 = post.add_comment("Super nice post!", user2)
comment3 = post.add_comment("I love myself!", user1)

print(f"{comment3.user.username} commented on {post.user.username}'s post: {comment3.comment}")


