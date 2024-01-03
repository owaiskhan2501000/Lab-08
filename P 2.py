from datetime import datetime

class Author:
    def __init__(self, author_id, name, email):
        self.author_id = author_id
        self.name = name
        self.email = email

    def __str__(self):
        return f"Author ID: {self.author_id}, Name: {self.name}, Email: {self.email}"


class Post:
    def __init__(self, post_id, title, content, author, timestamp=None):
        self.post_id = post_id
        self.title = title
        self.content = content
        self.author = author
        self.timestamp = timestamp or datetime.now()

    def __str__(self):
        return f"Post ID: {self.post_id}, Title: {self.title}, Author: {self.author.name}, Timestamp: {self.timestamp}"

class Blog:
    def __init__(self, blog_id, name):
        self.blog_id = blog_id
        self.name = name
        self.posts = []

    def add_post(self, post):
        self.posts.append(post)
        print(f"Post '{post.title}' added to the blog.")

    def display_posts_by_author(self, author):
        author_posts = [post for post in self.posts if post.author == author]
        if not author_posts:
            print(f"No posts found for author {author.name}.")
        else:
            print(f"Posts by {author.name}:")
            for post in author_posts:
                print(post)

    def display_latest_posts(self, num_posts=5):
        latest_posts = sorted(self.posts, key=lambda post: post.timestamp, reverse=True)[:num_posts]
        if not latest_posts:
            print("No posts available.")
        else:
            print(f"Latest {num_posts} posts:")
            for post in latest_posts:
                print(post)

author1 = Author(1, "John Doe", "john.doe@example.com")
author2 = Author(2, "Jane Smith", "jane.smith@example.com")

post1 = Post(101, "Introduction to Python", "Python is a versatile programming language.", author1)
post2 = Post(102, "Web Development with Django", "Django is a popular web framework for Python.", author1)
post3 = Post(103, "Data Science Basics", "An overview of data science concepts and techniques.", author2)

blog = Blog(1, "Tech Blog")

blog.add_post(post1)
blog.add_post(post2)
blog.add_post(post3)

blog.display_posts_by_author(author1)

blog.display_latest_posts()
