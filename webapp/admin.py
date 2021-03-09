from django.contrib import admin
from .models import AllExam,EngineeringExam, MedicalExam, DefNavArm
# Register your models here.
admin.site.register(EngineeringExam)
admin.site.register(MedicalExam)
admin.site.register(DefNavArm)
admin.site.register(AllExam)

