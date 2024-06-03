from dataclasses import dataclass
from src.data.post import Post

@dataclass
class Store:
    posts: []
    
    # def postAppend(self, title, context, fileName):
    #     posts.append(Post(len(posts)+1, title=title, context=context, fileName=fileName))