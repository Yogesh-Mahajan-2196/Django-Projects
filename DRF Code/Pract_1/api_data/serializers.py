from .models import Employee
from rest_framework import serializers
def sal_validation(value):
    if value % 1000 != 0:
        raise serializers.ValidationError('Salary should be multiple of 1000.')
    return value

class EmployeeSerializer(serializers.ModelSerializer):
    esal = serializers.FloatField(validators=[sal_validation,])
    class Meta:
        model = Employee
        fields = '__all__'

    def validate_esal(self, value):
        if value < 10000:
            raise serializers.ValidationError('Salary should be greater than 10000.')
        return value
    
    def validate(self, data):
        eadd = data.get('eadd')
        if eadd.endswith('g.com') != True:
            raise serializers.ValidationError('Domain name should be g.com only.')
        return data
'''
class EmployeeSerializer(serializers.Serializer):

    eid = serializers.IntegerField()
    ename = serializers.CharField()
    eadd = serializers.CharField()
    esal = serializers.FloatField()

    def create(self,validated_data):
        return Employee.objects.create(**validated_data)

    def update(self,instance, validated_data):
        instance.eid = validated_data.get('eid', instance.eid)
        instance.ename = validated_data.get('ename', instance.ename)
        instance.eadd = validated_data.get('eadd', instance.eadd)
        instance.esal = validated_data.get('esal', instance.esal)

        instance.save()
        return instance

'''