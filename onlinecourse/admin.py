from django.contrib import admin
# <HINT> Import any new Models here
from .models import Course, Lesson, Instructor, Learner, Question, Choice
import nested_admin

class ChoiceInline(nested_admin.NestedStackedInline):
    model = Choice
    extra = 3
    classes = ['collapse']
class LessonInline(nested_admin.NestedStackedInline):
    model = Lesson
    extra = 3
    classes = ['collapse']

class QuestionInline(nested_admin.NestedTabularInline):
    model = Question
    extra = 3
    inlines = [ChoiceInline]
    classes = ['collapse','wide']

class CourseAdmin(nested_admin.NestedModelAdmin):
    inlines = [LessonInline, QuestionInline]
    list_display = ('name', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['name', 'description']
    extra = 3

class LessonAdmin(nested_admin.NestedModelAdmin):
    list_display = ['disp_title_course']
    inlines = [QuestionInline]
    extra = 3
    search_fields = ['title', 'course__name']
    list_filter = ('course__name',)
    def disp_title_course(self, obj):
       return obj.title + " - " + obj.course.name

class QuestionAdmin(nested_admin.NestedModelAdmin):
    inlines = [ChoiceInline] 
    list_display = ('course__name','question_content', 'question_grade')
    extra = 3
    search_fields = ['question_content', 'course__name']
    list_filter = ('course__name',) 

class ChoiceAdmin(nested_admin.NestedModelAdmin):
    list_display = ('choice_content', 'correct')
    extra = 3






# <HINT> Register Question and Choice models here


admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Question, QuestionAdmin)
#admin.site.register(Choice, ChoiceAdmin)
admin.site.register(Instructor)
admin.site.register(Learner)
