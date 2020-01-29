"""定义learning_logs的URL模式"""
from django.urls import path
from . import views

app_name = 'learning_logs'

urlpatterns = [
    # 主页
    path('', views.index, name='index'),
    # 显示所有主题
    path('topics/', views.topics, name='topics'),
    # 特定主题的详细页面
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    # 用于添加新主题的网页
    path('new_topic/', views.new_topic, name='new_topic'),
    # 用于添加新条目的页面
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
    # 用于编辑条目
    path('edit_entry/<int:entry_id>/',views.edit_entry,name='edit_entry'),
]

# regex正则表达式r'^$'。其中的r让Python将接下来的字符串视为原始字符串，
# 而引号告诉Python正则表达式始于和终于何处。脱字符（^）让Python查看字符串的开头，
# 而美元符号让Python查看字符串的末尾。
