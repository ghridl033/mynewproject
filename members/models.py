from django.db import models

# Create your models here.
class Members(models.Model):
    username = models.CharField(max_length=64, verbose_name="사용자")
    useremail = models.EmailField(max_length=128, verbose_name="사용자 이메일")
    password = models.CharField(max_length=64, verbose_name="비밀번호")
    created = models.DateTimeField(auto_now_add=True, verbose_name="가입일시")
    update  = models.DateTimeField(auto_now_add=True, verbose_name="수정일시")
    class Meta:
        db_table = "myfirstproject_users"
        verbose_name = '첫 프로젝트 사용자'
        verbose_name_plural = 'myfirstproject 사용자'

