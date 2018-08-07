from api import models, serializers
from rest_framework.views import APIView
from api.untils.reponse import ResponseDict
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination


class CourseListView(APIView):
    def get(self, request, *args, **kwargs):
        ret = ResponseDict()
        try:
            course_queryset = models.Course.objects.all()
            page = PageNumberPagination()
            course_list = page.paginate_queryset(course_queryset, request, self)
            course_new = serializers.CourseSerializer(course_list, many=True)
            ret.data = course_new.data
        except Exception as e:
            ret.code = 500
            ret.error = '获取数据失败'
        # return Response(ret.dict)

        response = Response(ret.dict)

        response['Access-Control-Allow-Origin'] = "*"

        return response


class DegreeCourseView(APIView):
    def get(self, request, *args, **kwargs):
        ret = ResponseDict()
        try:
            page = PageNumberPagination()
            degree_queryset = models.DegreeCourse.objects.all()
            degree_list = page.paginate_queryset(degree_queryset, request, self)
            degree_new = serializers.DegreeCourseSerializer(degree_list, many=True)
            ret.data = degree_new.data
        except Exception as e:
            ret.code = 500
            ret.error = '获取数据失败'
        return Response(ret.dict)


class DegreeCourseDetailView(APIView):

    def get(self, request, pk, *args, **kwargs):
        ret = ResponseDict()
        try:
            degree = models.DegreeCourse.objects.filter(id=pk).first()
            degree_new = serializers.DegreeCourseDetailSerializer(degree)
            ret.data = degree_new.data
        except Exception as e:
            ret.code = 500
            ret.error = '获取数据失败'
        return Response(ret.dict)


class CourseDetailView(APIView):

    def get(self, request, pk, *args, **kwargs):
        ret = ResponseDict()
        try:
            course = models.Course.objects.filter(id=pk).first()
            course_new = serializers.CourseDetailSerializer(course)
            ret.data = course_new.data
        except Exception as e:
            ret.code = 500
            ret.error = '获取数据失败'
        return Response(ret.dict)