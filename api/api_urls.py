from django.conf.urls import url
from api.views import course
urlpatterns = [
    url(r'degreecourse/$', course.DegreeCourseView.as_view()),
    url(r'course/$', course.CourseListView.as_view()),
    url(r'degreecoursedetail/(?P<pk>\d+)/$', course.DegreeCourseDetailView.as_view()),
    url(r'coursedetail/(?P<pk>\d+)/$', course.CourseDetailView.as_view()),

]
