from django.db import models
from users.models import User
from posts.models import Post, Comment

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True, blank=True)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, null=True, blank=True)
    value = models.IntegerField(choices=[(1, 'Like'), (-1, 'Dislike')])

    class Meta:
        unique_together = ('user', 'post', 'comment')

    def __str__(self):
        if self.post:
            return f'Like by {self.user.username} on post "{self.post.title}"'
        return f'Like by {self.user.username} on comment ID {self.comment.id}'
