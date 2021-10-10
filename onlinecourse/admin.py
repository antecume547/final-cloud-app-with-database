from django.contrib import admin
# <HINT> Import any new Models here
from .models import Course, Lesson, Instructor, Learner, Question, Choice
import nested_admin
# <HINT> Register QuestionInline and ChoiceInline classes here


class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('choice_content', 'correct')

class ChoiceInline(nested_admin.NestedStackedInline):
    model = Choice
    extra = 3
class LessonInline(nested_admin.NestedStackedInline):
    model = Lesson
    extra = 5

class QuestionInline(nested_admin.NestedStackedInline):
    model = Question
    extra = 5
    inlines = [ChoiceInline]

# Register your models here.
class CourseAdmin(admin.ModelAdmin):
    inlines = [LessonInline]
    list_display = ('name', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['name', 'description']


class LessonAdmin(admin.ModelAdmin):
    list_display = ['title']
    inlines = [QuestionInline]

class QuestionAdmin(nested_admin.NestedModelAdmin):
    inlines = [ChoiceInline] 
    list_display = ('lesson_title','question_content', 'question_grade')
    #readonly_fields =['get_lesson_title']
    






# <HINT> Register Question and Choice models here

admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)
admin.site.register(Instructor)
admin.site.register(Learner)
