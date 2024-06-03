from dataclasses import dataclass

@dataclass
class Post: 
    no: int
    title: str
    context: str
    fileName: str

# class Posts(NumValue, title, context, fileName):
#     no: int(NumValue)
#     title: str(title)
#     context: str(context)
#     fileName: str(filename)
# 'number': len(posts) + 1,  # 클래스 내부 변수 self.posts 사용
#         'title': contentTitle,
#         'context': contentText,
#         'fileName': filename
    
    