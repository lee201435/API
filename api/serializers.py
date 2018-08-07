from rest_framework import serializers
from api import models


class CourseSerializer(serializers.ModelSerializer):

    course_type = serializers.CharField(source='get_course_type_display')

    class Meta:
        model = models.Course
        fields = ['id', 'name', 'course_type']


class DegreeCourseSerializer(serializers.ModelSerializer):
    teachers = serializers.SerializerMethodField()
    scholarship = serializers.SerializerMethodField()

    class Meta:
        model = models.DegreeCourse
        fields = ['id', 'name', 'teachers', 'scholarship']

    def get_teachers(self, obj):
            obj_list = obj.teachers.all()
            return [item.name for item in obj_list]

    def get_scholarship(self, obj):
            obj_list = obj.scholarship_set.all()
            return [item.value for item in obj_list]


class DegreeCourseDetailSerializer(serializers.ModelSerializer):
    module_name = serializers.SerializerMethodField()

    class Meta:
        model = models.DegreeCourse
        fields = ['name', 'module_name']

    def get_module_name(self, obj):
        obj_list = obj.course_set.all()
        return [item.name for item in obj_list]


class CourseDetailSerializer(serializers.ModelSerializer):
    level = serializers.CharField(source='get_level_display')
    why_study = serializers.CharField(source='coursedetail.why_study')
    learn_content = serializers.CharField(source='coursedetail.what_to_study_brief')
    recommend_courses = serializers.SerializerMethodField()

    class Meta:
        model = models.Course
        fields = ['name', 'level', 'why_study', 'learn_content', 'recommend_courses']

    def get_recommend_courses(self,row):
        recommend_list = row.coursedetail.recommend_courses.all()
        return [{'id': item.id, 'name': item.name} for item in recommend_list]
