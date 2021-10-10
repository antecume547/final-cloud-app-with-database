from django.contrib import admin
# <HINT> Import any new Models here
from .models import Course, Lesson, Instructor, Learner, Question, Choice
import nested_admin
# <HINT> Register QuestionInline and ChoiceInline classes here



class ChoiceInline(nested_admin.NestedStackedInline):
    model = Choice
    extra = 3
    classes = ['collapse']
class LessonInline(nested_admin.NestedStackedInline):
    model = Lesson
    extra = 3

class QuestionInline(nested_admin.NestedTabularInline):
    model = Question
    extra = 3
    inlines = [ChoiceInline]
    classes = ['collapse','wide']
class ChoiceAdmin(nested_admin.NestedModelAdmin):
    list_display = ('choice_content', 'correct')
    extra = 3

class CourseAdmin(nested_admin.NestedModelAdmin):
    inlines = [LessonInline]
    list_display = ('name', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['name', 'description']
    extra = 3

class LessonAdmin(nested_admin.NestedModelAdmin):
    list_display = ['title']
    inlines = [QuestionInline]
    extra = 3
class QuestionAdmin(nested_admin.NestedModelAdmin):
    inlines = [ChoiceInline] 
    list_display = ('lesson_title','question_content', 'question_grade')
    extra = 3
    #readonly_fields =['get_lesson_title']
    






# <HINT> Register Question and Choice models here

admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Question, QuestionAdmin)
#admin.site.register(Choice, ChoiceAdmin)
admin.site.register(Instructor)
admin.site.register(Learner)
