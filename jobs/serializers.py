from rest_framework import serializers
import pendulum
from .models import Job


class Job_Get_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = ('id',
                  'recommender',
                  'company',
                  'refer_scope_link',
                  'refer_scope_description',
                  'refer_requirement',
                  'post_date')

    def to_representation(self, instance):
        response_dict = {
            'id': instance.id,
            'recommender': instance.recommender.email,
            'company': instance.company,
            'refer_scope_link': instance.refer_scope_link,
            'refer_scope_description': instance.refer_scope_description,
            'refer_requirement': instance.refer_requirement,
            'post_date': pendulum.parse(str(instance.post_date)).in_tz('America/Los_Angeles').format('YYYY-MM-DD hh:mm:ss A'),
        }
        return response_dict


class Job_Posting(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = (
            'recommender',
            'company',
            'refer_scope_link',
            'refer_scope_description',
            'refer_requirement',
        )